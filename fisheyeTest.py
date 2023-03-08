from defisheye import Defisheye
import cv2

dtype = "orthographic"
format = "fullframe"
fov = 132 #May need to change these to fit camera
pfov = 100

image = "/home/capstone403/fisheyecalibration.jpg"
imageOut = f"/home/capstone403/fisheyeBoardFixed_5inch.jpg"

imageDefish = "/home/capstone403/fisheyecalibrationDesfish.jpg"
imageCV = cv2.imread("/home/capstone403/fisheyecalibration.jpg")
img = cv2.resize(imageCV, (1944, 1944))
cv2.imwrite("/home/capstone403/fisheyecalibrationDesfish.jpg", img)



obj = Defisheye(imageDefish, dtype=dtype, format = format, fov = fov, pfov = pfov)
obj.convert(imageOut)
