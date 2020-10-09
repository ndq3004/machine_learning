import cv2
img = cv2.imread("C:/Users/quan.nd166622/Desktop/download (1).png")
#Giấy chứng minh nhân dân
title = [274, 70, 830, 52] 
#Số
no = [274, 115, 830, 54] 
#Họ tên
name = [247, 200, 600, 76] 
#Sinh ngày
dateOfBirth = [247, 284, 600, 54] 
#Nguyên quán
country = [247, 330, 600, 105] 
#địa chỉ thường trú
address = [247, 435, 600, 110] 
x, y, w, h = address
crop_img = img[y:y+h, x:x+w]
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)