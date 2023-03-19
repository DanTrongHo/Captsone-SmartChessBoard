

import cv2
from defisheye import Defisheye
import numpy as np
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import math
import itertools
L2 = []

def deFishey_fxn():
    dtype = "orthographic"
    format = "fullframe"
    fov = 132 #May need to change these to fit camera
    pfov = 100

    image = "final_CameraTest15.jpg"
    imageOut = f"defisheyed.jpg"

    obj = Defisheye(image, dtype=dtype, format = format, fov = fov, pfov = pfov)
    obj.convert(imageOut)


deFishey_fxn()

# For reading/slecting image
img = cv2.imread('defisheyed.jpg')

#img_75 = cv2.resize(img, None, fx = 0.6, fy = 0.6)
img_75 = cv2.resize(img, (1000,1000))
# converting image into a grayscale version of image
gray = cv2.cvtColor(img_75, cv2.COLOR_BGR2GRAY)

# setting threshold of gray image
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# using a findContours() function
contours, _ = cv2.findContours(
    threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

i = 0

# list for storing names of shapes
for contour in contours:
    # Ignores first counter because findcontour function 
    #detects whole image as shape
    if i == 0:
        i = 1
        continue
    # cv2.approxPloyDP() is used to approximate the shape
    approx = cv2.approxPolyDP(
        contour, 0.01 * cv2.arcLength(contour, True), True)
    # using drawContours() to draw the shapes
    cv2.drawContours(img_75, [contour], 0, (0, 0, 255), 5)
    # finding center point of a shape
    M = cv2.moments(contour)
    #print("start Contour if statement")
    if M['m00'] != 0.0:
        x = int(M['m10'] / M['m00'])
        y = int(M['m01'] / M['m00'])
    #print("end Contour if statement")


    def Big_list_of_Pieces(L):
        L2.append(L)
        print(L2)


    def list_of_pieces(str, x_coord, y_coord):
        L = []
        L.append(str)
        L.append(x_coord)
        L.append(y_coord)
        Big_list_of_Pieces(L)
        #print(L)

    def convert_x_to_letter(x_coord):
        if (x_coord == 1):
            return('A')
        elif (x_coord == 2):
            return ('B')
        elif (x_coord == 3):
            return ('C')
        elif (x_coord == 4):
            return ('D')
        elif (x_coord == 5):
            return ('E')
        elif (x_coord == 6):
            return ('F')
        elif (x_coord == 7):
            return ('G')
        elif (x_coord == 8):
            return ('H')



#If statement for calculating total shape length
    if (len(approx) > 2):
        startPointx = int(approx[0][0][0])
        startPointy = int(approx[0][0][1])
        endPointx = int(approx[-1][0][0])
        endPointy = int(approx[-1][0][1])
        distance = ((endPointx - startPointx) ** 2 + (endPointy - startPointy) ** 2) ** (1 / 2)

        squareLength = 100

        xSquare = int(x / squareLength) + 1
        ySquare = int(y / squareLength) + 1

        # if statement for setting shape parameters so square 
        # are ignored
        if distance <= 50 and distance >= 10:
        # where shapes are defined as well determing the location of shape
            if len(approx) == 4:
                shape = cv2.putText(img_75, 'Rook/' + str(xSquare) + ", " + str(ySquare), (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)

                list_of_pieces('Rook',convert_x_to_letter(xSquare),ySquare)
            elif len(approx) == 5:
                shape = cv2.putText(img_75, 'Bishop/' + str(xSquare) + ", " + str(ySquare), (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
                list_of_pieces('Bishop',convert_x_to_letter(xSquare),ySquare)
            elif len(approx) == 6:
               shape = cv2.putText(img_75, 'Knight/' + str(xSquare) + ", " + str(ySquare), (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
               list_of_pieces('Knight',convert_x_to_letter(xSquare),ySquare)
            elif len(approx) == 7:
                shape = cv2.putText(img_75, 'Pawn/' + str(xSquare) + ", " + str(ySquare), (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
                list_of_pieces('Pawn',convert_x_to_letter(xSquare),ySquare)
            elif len(approx) == 8:
                shape = cv2.putText(img_75, 'Queen/' + str(xSquare) + ", " + str(ySquare), (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
                list_of_pieces('Queen',convert_x_to_letter(xSquare),ySquare)
            elif len(approx) == 9:
                shape = cv2.putText(img_75, 'King/' + str(xSquare) + ", " + str(ySquare), (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
                list_of_pieces('King',convert_x_to_letter(xSquare),ySquare)
            elif len(approx) == 10:
                shape = cv2.putText(img_75, '10/' + str(xSquare) + ", " + str(ySquare), (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
            elif len(approx) == 11:
                shape = cv2.putText(img_75, '11/' + str(xSquare) + ", " + str(ySquare), (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
            else:
                shape = cv2.putText(img_75, 'Invalid Shape/' + str(xSquare) + ", " + str(ySquare), (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
                cv2.putText(img_75, str(len(approx)), (x, y + 15),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
        else:
            shape = cv2.putText(img_75, 'Invalid Shape/' + str(xSquare) + ", " + str(ySquare), (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)

#print( 'Image width is', img_75.shape[1])
#print( 'Image width is', img_75.shape[0])


# displaying the image after drawing contours and labeling shapes
cv2.imshow('shapes', img_75)

cv2.waitKey(0)
cv2.destroyAllWindows()
