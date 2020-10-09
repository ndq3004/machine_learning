# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PIL import Image
from imutils import paths
import cv2
import PIL as p 
p.ImageFile.LOAD_TRUNCATED_IMAGES=True

def addMargin(img_path, top, right, bottom, left, color):
    im = Image.open(img_path)
    width, height = im.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(im.mode, (new_width, new_height), color)
    result.paste(im, (left, top))
    return result

pathToFolder = 'C:/Users/quan.nd166622/Downloads/newCrackImage'
savedFolder = 'D:/addmargin'
imagePaths = list(paths.list_images(pathToFolder))
print(imagePaths[0])
for path in imagePaths:
    im_new = addMargin(path, 200, 300, 200, 300, (255,255,255))
    filename = str(path).split('\\')[1]
    ext = 'JPEG'
    if filename.split('.')[1] == 'png' or filename.split('.')[1] == 'PNG':
        ext = 'PNG'
    newPath = savedFolder + '\\' +  filename
    im_new.save(newPath, ext)
    print(filename)

