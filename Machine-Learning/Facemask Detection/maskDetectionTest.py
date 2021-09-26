import cv2
import argparse
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dropout, Dense


def adjust_gamma(image, gamma=1.0):
    # build a lookup table mapping the pixel values [0, 255] to
    # their adjusted gamma values
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")
    # apply gamma correction using the lookup table
    return cv2.LUT(image, table)


def adjust_img(img):

    # -----Converting image to LAB Color model-----------------------------------
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

    # -----Splitting the LAB image to different channels-------------------------
    l, a, b = cv2.split(lab)

    # -----Applying CLAHE to L-channel-------------------------------------------
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)

    # -----Merge the CLAHE enhanced L-channel with the a and b channel-----------
    limg = cv2.merge((cl, a, b))

    # -----Converting image from LAB Color model to RGB model--------------------
    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
    return final


cnn = Sequential([Conv2D(filters=100, kernel_size=(3, 3),
                         activation='relu'),
                  MaxPooling2D(pool_size=(2, 2)),
                  Conv2D(filters=100, kernel_size=(3, 3),
                         activation='relu'),
                  MaxPooling2D(pool_size=(2, 2)),
                  Flatten(),
                  Dropout(0.5),
                  Dense(50),
                  Dense(35),
                  Dense(2)], name='MaskDetection')
cnn.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc'])

labels_dict = {0: 'No mask', 1: 'Mask'}  # Mapping results to output
color_dict = {0: (0, 0, 255), 1: (0, 255, 0)}  # Mapping colors to output
img_size = 8
camera = cv2.VideoCapture(0)  # Camera on

# Identify Face
classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
while True:
    (rval, im) = camera.read()
    im = cv2.flip(im, 1, 1)  # flipping image
    im = adjust_gamma(im)
    imgs = cv2.resize(im, (im.shape[1] // img_size, im.shape[0] // img_size))
    face_rec = classifier.detectMultiScale(imgs)
    for i in face_rec:  # box overlay on face
        (x, y, l, w) = [v * img_size for v in i]
        face_img = im[y:y+w, x:x+l]
        resized = cv2.resize(face_img, (150, 150))
        normalized = resized/255.0
        reshaped = np.reshape(normalized, (1, 150, 150, 3))
        reshaped = np.vstack([reshaped])
        result = cnn.predict(reshaped)
        label = np.argmax(result, axis=1)[0]
        cv2.rectangle(im, (x, y), (x+l, y+w), color_dict[label], 2)
        cv2.rectangle(im, (x, y-40), (x+l, y), color_dict[label], -1)
        cv2.putText(im, labels_dict[label], (x, y -
                                             10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    cv2.imshow('LIVE', im)
    key = cv2.waitKey(10)
    # stop loop by ESC
    if key == 27:  # The Esc key
        break
camera.release()
cv2.destroyAllWindows()
