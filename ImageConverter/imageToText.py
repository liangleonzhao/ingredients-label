#!/usr/bin/python
# import cv2
import numpy as np

from PIL import Image

from pytesseract import image_to_string

img = Image.open('/Users/phoebeshieh/PycharmProjects/cpsc462/image1.jpg')

# convert to grayspace
img = img.convert('L')

# rotate it
# img = img.rotate(90)
# save = img.save('saveimg.jpg')

width = 1224
height = 1632

# resize image for best result
# img = img.resize((width,height), Image.ANTIALIAS)
# img = img.convert('L')

text = image_to_string(img)
# print(text)


if (text.find('INGREDIENTS') != -1):
    isFound = 1
    print("Found")
else:
    isFound = 0
    print("Not found")

while (text.find("INGREDIENTS") == -1 or text == ""):
    print("inside while loop")
    # img = Image.open('/Users/henry/Downloads/image1.jpeg')

    # convert to grayspace
    img = img.convert('L')

    # rotate it
    # img = img.rotate(270)
    img = img.rotate(90)
    save = img.save('saveimg.jpg')

    width = 1224
    height = 1632

    # resize image for best result
    # img = img.resize((width,height), Image.ANTIALIAS)
    # img = img.convert('L')

    text = image_to_string(img)

    if (text.find('INGREDIENTS') != -1):
        print(text)
        break

print(text)

