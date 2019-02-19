from imageToText import Read

filePath = input("Enter file location: ")
ingredients = Read(filePath)
print(ingredients.ocr())
