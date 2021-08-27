#import required Libraries

from typing import Text
import cv2 as cv
import pytesseract
import numpy as np

def ocr_core(img):
    text=pytesseract.image_to_string(img)
    return text

img=cv.imread('https://github.com/ShlokIngle/Team-5/blob/main/test1.png')
#change img path according to requirement

# get_grayscale image
def get_grayscale(image):
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv.medianBlur(image,5)

#thresholding
def thresholding(image):
    return cv.threshold(image, 0,255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]

img = get_grayscale(img)
#img = remove_noise(img)
img = thresholding(img)
img = remove_noise(img)

print(ocr_core(img))
print(eval(ocr_core(img)))
