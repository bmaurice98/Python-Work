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
    # print(image)

    # confirm that image is chosen
    if originalImage is None:
        print("Can't find an image")
        sys.exit()

    ReSized1 = cv2.resize(originalImage, (960, 540))
    # plt.imshow(ReSized1, cmap="gray")

    # converting to grayscale
    grayScaleimage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    ReSized2 = cv2.resize(grayScaleimage, (960, 540))
    # plt.imshow(ReSized2, cmap='gray')
