import argparse
import cv2
 

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image")
ap.add_argument("-p", "--percent", required=False, help="the percent you want to resize")
args = vars(ap.parse_args())
print(args)
src = cv2.imread(args["image"], cv2.IMREAD_UNCHANGED)
#percent by which the image is resized
scale_percent = 50
if args["percent"] is not None:
    scale_percent = int(args["percent"])

#calculate the 50 percent of original dimensions
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

# dsize
dsize = (width, height)

# resize image
output = cv2.resize(src, dsize)

cv2.imwrite('output_' + args["image"],output) 