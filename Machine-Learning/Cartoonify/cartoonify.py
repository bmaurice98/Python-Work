import cv2, easygui, imageio, sys, os
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

# Opens gui allowing us to open choose a file
# and store the path as a string
def upload():
    ImagePath = easygui.fileopenbox()
    cartoonify(ImagePath)


def cartoonify(ImagePath):
    # read in the image
    originalImage = cv2.imread(ImagePath)
    originalImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2RGB)

    # confirm that image is chosen
    if originalImage is None:
        print("Can't find an image")
        sys.exit()

    ReSized1 = cv2.resize(originalImage, (960, 540))
    # plt.imshow(ReSized1, cmap="gray")

    # converting to grayscale
    grayScaleimage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    ReSized2 = cv2.resize(grayScaleimage, (960, 540))
    # plt.imshow(ReSized2, cmap="gray")

    # smoothing GS image
    smoothGrayScale = cv2.medianBlur(grayScaleimage, 5)
    ReSized3 = cv2.resize(smoothGrayScale, (960, 540))
    # plt.imshow(ReSized3, cmap="gray")

    # retrieving cartoon effect edges
    getEdge = cv2.adaptiveThreshold(
        smoothGrayScale, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9
    )
    ReSized4 = cv2.resize(getEdge, (960, 540))
    # plt.imshow(ReSized4, cmap="gray")

    # applying bilateral filter to remove image noise and keep edges sharp
    colorImage = cv2.bilateralFilter(originalImage, 9, 300, 300)
    ReSized5 = cv2.resize(colorImage, (960, 540))
    # plt.imshow(ReSized4, cmap="gray")

    # masking edged image with the beautified image
    cartoonImage = cv2.bitwise_and(colorImage, colorImage, mask=getEdge)
    ReSized6 = cv2.resize(cartoonImage, (960, 540))
    # plt.imshow(ReSized6, cmap="gray")
    # plt.show()

    # plotting the transition
    images = [ReSized1, ReSized2, ReSized3, ReSized4, ReSized5, ReSized6]
    fig, axes = plt.subplots(
        3,
        2,
        figsize=(8, 8),
        subplot_kw={"xticks": [], "yticks": []},
        gridspec_kw=dict(hspace=0.1, wspace=0.1),
    )
    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i], cmap="gray")
    plt.show()


def saveButton(Resized6, ImagePath):
    # saving image with imwrite()
    newName = "cartoon_Image"
    path1 = os.path.dirname(ImagePath)
    extension = os.path.splitext(ImagePath)[1]
    path = os.path.join(path1, newName + extension)
    cv2.imwrite(path, cv2.cvtColor(Resized6, cv2.COLOR_RGB2BGR))
    I = "Image saved by name " + newName + " at " + path
    tk.Messagebox.showinfo(title=None, Message=I)


if __name__ == "__main__":
    upload()
