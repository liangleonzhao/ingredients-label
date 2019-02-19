import numpy as np

from PIL import Image

from pytesseract import image_to_string


class Read():
    def __init__(self, filename):
        self.fileName = filename

    def get_fileName(self):
        fileName = input("Enter file location: ")
        self.fileName = fileName

    def ocr(self):
        # convert to grayspace
        img = Image.open(self.fileName)
        img = img.convert('L')
        text = image_to_string(img)
        if (text.find('INGREDIENTS') != -1):
            isFound = 1
            print("Found")
        else:
            isFound = 0
            print("Not found")

        while (text.find("INGREDIENTS") == -1 or text == ""):
            print("inside while loop")

            # convert to grayspace
            img = img.convert('L')

            # rotate it
            img = img.rotate(90)
            save = img.save('saveimg.jpg')


            text = image_to_string(img)

        return text
