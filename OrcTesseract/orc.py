from PIL import Image
import pytesseract
import argparse
import cv2
# import os
import numpy as np
# os.environ['DISPLAY'] = ':0'

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="Path to input Image")
# ap.add_argument("-p", "--preprocess", type= str, default="thresh", 
#                 help="Type of preprocessing")
# args = vars(ap.parse_args())
args = {'image': '/home/ndquan/machine_learning/OrcTesseract/result.png',
        'copy': '/home/ndquan/machine_learning/OrcTesseract/result (copy).png',
        'preprocess': 'thresh'}
#load the image
image = cv2.imread(args['image'])
filter1 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
sharpen_img_1 = cv2.filter2D(cv2.imread(args['copy']),-1,filter1)
# gray = 
# gray  = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('hihi', gray)
#check the preprocess
# if args['preprocess'] == 'thresh':
#     gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# elif args['preprocess'] == 'blur':
#     gray = cv2.medianBlur(gray, 3)

# filename = "{}.png".format(os.getpid())
# cv2.imwrite(filename, gray)

# text = pytesseract.image_to_string(Image.open(filename), lang='vie')
# os.remove(filename)
# print(text)
cv2.imshow("Image: ", image)
cv2.imshow("Output: ", sharpen_img_1)
cv2.waitKey(0)
