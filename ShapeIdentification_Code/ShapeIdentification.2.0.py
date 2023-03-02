import cv2
import numpy as np
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import math

# For reading/slecting image
img = cv2.imread('/home/capstone403/fisheyeBoardFixed.jpg')

# converting image into a grayscale version of image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# setting threshold of gray image
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# using a findContours() function
contours, _ = cv2.findContours(
    threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

i = 0

# list for storing names of shapes
for contour in contours:
    print("start Contour")
    # Ignores first counter because findcontour function 
    #detects whole image as shape
    if i == 0:
        i = 1
        continue

    # cv2.approxPloyDP() is used to approximate the shape
    approx = cv2.approxPolyDP(
        contour, 0.01 * cv2.arcLength(contour, True), True)

    # using drawContours() to draw the shapes
    cv2.drawContours(img, [contour], 0, (0, 0, 255), 5)

    # finding center point of a shape
    M = cv2.moments(contour)
    print("start Contour if statement")
    if M['m00'] != 0.0:
        x = int(M['m10'] / M['m00'])
        y = int(M['m01'] / M['m00'])
    print("end Contour if statement")

        




#If statement for calculating total shape length
    if (len(approx) > 2):
        startPointx = int(approx[0][0][0])
        startPointy = int(approx[0][0][1])
        endPointx = int(approx[-1][0][0])
        endPointy = int(approx[-1][0][1])
        distance = ((endPointx - startPointx) ** 2 + (endPointy - startPointy) ** 2) ** (1 / 2)

        squareLength = 288

        xSquare = int(x / squareLength) + 1
        ySquare = int(y / squareLength) + 1

        # if statement for setting shape parameters so square 
        # are ignored
        if distance <= 288 and distance >= 10:
        # where shapes are defined as well determing the location of shape
            if len(approx) == 4:
                shape = cv2.putText(img, 'Rook/' + str(xSquare) + ", " + str(ySquare), (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
            elif len(approx) == 5:
                shape = cv2.putText(img, 'Bishop/' + str(xSquare) + ", " + str(ySquare), (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
            elif len(approx) == 6:
               shape = cv2.putText(img, 'Knight/' + str(xSquare) + ", " + str(ySquare), (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
            elif len(approx) == 7:
                shape = cv2.putText(img, 'Pawn/' + str(xSquare) + ", " + str(ySquare), (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
            elif len(approx) == 8:
                shape = cv2.putText(img, 'Queen/' + str(xSquare) + ", " + str(ySquare), (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
            elif len(approx) == 9:
                shape = cv2.putText(img, 'King/' + str(xSquare) + ", " + str(ySquare), (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
            elif len(approx) == 10:
                shape = cv2.putText(img, '10/' + str(xSquare) + ", " + str(ySquare), (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
            elif len(approx) == 11:
                shape = cv2.putText(img, '11/' + str(xSquare) + ", " + str(ySquare), (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
            else:
                shape = cv2.putText(img, 'Invalid Shape/' + str(xSquare) + ", " + str(ySquare), (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
                cv2.putText(img, str(len(approx)), (x, y + 15),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
        else:
            shape = cv2.putText(img, 'Invalid Shape/' + str(xSquare) + ", " + str(ySquare), (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)





# displaying the image after drawing contours and labeling shapes
cv2.imshow('shapes', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
