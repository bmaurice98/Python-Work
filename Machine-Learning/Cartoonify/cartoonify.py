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
    plt.show()


if __name__ == "__main__":
    upload()
