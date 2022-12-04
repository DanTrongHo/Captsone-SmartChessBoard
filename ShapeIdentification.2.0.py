import cv2
import numpy as np
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import math

# reading image/file
img = cv2.imread('PieceTest1.jpg')

# converts the image into grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# setting threshold of gray image
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# using findContours() to finnd and identify contours of shapes
contours, _ = cv2.findContours(
    threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

i = 0

# list for storing definitions of shapes
for contour in contours:

    # here ignore the first counter because
    # findcontour function detects entire image as a shape
    if i == 0:
        i = 1
        continue

    # cv2.approxPloyDP() is used to approximate the shape
    approx = cv2.approxPolyDP(
        contour, 0.01 * cv2.arcLength(contour, True), True)

    # using drawContours() draws contours ontop of the detected contours and
    # sums them and the contours up
    if (len(approx) > 2):
        cv2.drawContours(img, [contour], 0, (0, 0, 255), 5)

    # finds the center point of shape
    # and is where the point that is used to determine location
    M = cv2.moments(contour)
    if M['m00'] != 0.0:
        x = int(M['m10'] / M['m00'])
        y = int(M['m01'] / M['m00'])

    # if statement used to determine the length of the shape
    if (len(approx) > 2):
        startPointx = int(approx[0][0][0])
        startPointy = int(approx[0][0][1])
        endPointx = int(approx[-1][0][0])
        endPointy = int(approx[-1][0][1])
        distance = ((endPointx - startPointx) ** 2 + (endPointy - startPointy) ** 2) ** (1 / 2)
        # length of the square
        squareLength = 51
        # x square length and y square (width)
        xSquare = int(x / squareLength) + 1
        ySquare = int(y / squareLength) + 1

        # putting shape name at center of each shape
        if distance <= 192 and distance >= 10:
            # shape definitions and display location
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
                shape = cv2.putText(img, 'circle/' + str(xSquare) + ", " + str(ySquare), (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
                cv2.putText(img, str(len(approx)), (x, y + 15),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
        else:
            #shape = cv2.putText(img, 'Invalid Shape/' + str(xSquare) + ", " + str(ySquare), (x, y),
             #           cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
            pass





# displaying the image after drawing contours
cv2.imshow('shapes', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
