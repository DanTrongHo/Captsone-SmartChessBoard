

import cv2
from defisheye import Defisheye
import numpy
import matplotlib.pyplot as plt
from numpy import array
import string


# function to defisheye the picture
L2 = []
mainArray = []
RowList = []
ColumnList = []
#def deFishey_fxn():
    #dtype = "orthographic"
    #format = "fullframe"
    #fov = 132 #May need to change these to fit camera
    #pfov = 100

    #image = "final_CameraTest15_Fixed_shape3.jpg"
    #imageOut = f"defisheyed.jpg"

    #obj = Defisheye(image, dtype=dtype, format = format, fov = fov, pfov = pfov)
    #obj.convert(imageOut)


#deFishey_fxn()

# For reading/slecting image
img = cv2.imread('final_CameraTest15_Fixed_shape3.jpg')


#img_75 = cv2.resize(img, None, fx = 0.6, fy = 0.6)
img_75 = cv2.resize(img, (1944,1944))
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

# functions to create list of piece locations
    def Big_list_of_Pieces(L):
        L2.append(L)
        print(L2)

    def list_of_pieces(str, xy_coord):
        L = []
        L.append(str)
        L.append(xy_coord)
        Big_list_of_Pieces(L)
        #print(L)
#convert x coordintes to letters
    def convert_x_to_letter(x_coord):
        if (x_coord == 8):
            return('a')
        elif (x_coord == 7):
            return ('b')
        elif (x_coord == 6):
            return ('c')
        elif (x_coord == 5):
            return ('d')
        elif (x_coord == 4):
            return ('e')
        elif (x_coord == 3):
            return ('f')
        elif (x_coord == 2):
            return ('g')
        elif (x_coord == 1):
            return ('h')

#definitions to make coefficients



    def makeArray():
        f = open("CameraCoordinates.txt", 'r')
        i = 0
        tempArray = []
        for line in f:
            line = line.rstrip()
            if i < 9:  # if not full column then just append to the temp array
                tempArray.append(line)
                i = i + 1
            else:  # Column is full need to reset the i counter, append the temp array to the main array, and append the current readline to a new array
                i = 1
                mainArray.append(tempArray.copy())
                tempArray.clear()
                tempArray.append(line)
        f.close()


    def getY(coord):
        commaPosition = coord.find(',')
        return int(coord[commaPosition + 1:])


    def getX(coord):
        commaPosition = coord.find(',')
        return int(coord[:commaPosition])


    def fillRow():  # top down order
        for i in range(len(mainArray)):
            tempYList = []
            tempXList = []
            for j in range(9):
                tempYList.append(getY(mainArray[i][j]))
                tempXList.append(getX(mainArray[i][j]))
            # Input array and get the equation, append to the row list

            RowList.append(numpy.polyfit(array(tempXList), array(tempYList), 1))


    def fillColumn():  # left to right order
        for i in range(9):
            tempYList = []
            tempXList = []
            for j in range(9):
                tempYList.append(getY(mainArray[j][i]))
                tempXList.append(getX(mainArray[j][i]))
            # Input array and get the equation, append to the row list
            ColumnList.append(numpy.polyfit(array(tempXList), array(tempYList), 1))

# Calling to get coefficients for line location


    def rows(x, y):
        makeArray()
        fillRow()
        fillColumn()
        for i in range(len(RowList)):
            a = RowList[i][0]
            b = RowList[i][1]
            y_eq = a * x + b
            if (y <= y_eq):
                row = 9 - i
                return row



    def columns(x, y):
        makeArray()
        fillRow()
        fillColumn()
        for i in range(len(ColumnList)):
            a = ColumnList[i][0]
            b = ColumnList[i][1]
            x_eq = (y-b)/a
            if (x <= x_eq):
                column = 9 -i
                return(column)




#If statement for calculating total shape length
    if (len(approx) > 2):
        startPointx = int(approx[0][0][0])
        startPointy = int(approx[0][0][1])
        endPointx = int(approx[-1][0][0])
        endPointy = int(approx[-1][0][1])
        distance = ((endPointx - startPointx) ** 2 + (endPointy - startPointy) ** 2) ** (1 / 2)

        squareLength = 50

        xSquare = int(x / squareLength) + 1
        ySquare = int(y / squareLength) + 1

        # if statement for setting shape parameters so square 
        # are ignored
        if distance < 35 and distance > 25:
        # where shapes are defined as well determing the location of shape
            if len(approx) == 4:
                shape = cv2.putText(img_75, 'Rook/' + str(x) + ", " + str(y), (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
                final_x = columns(x, y)
                list_of_pieces('Rook', str(convert_x_to_letter(final_x)) + str(rows(x, y)))

                #list_of_pieces('Rook',convert_x_to_letter(rows(xSquare, ySquare)),columns(xSquare, ySquare))
            elif len(approx) == 5:
                shape = cv2.putText(img_75, 'Bishop/' + str(x) + ", " + str(y), (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
                final_x = columns(x, y)
                list_of_pieces('Bishop', str(convert_x_to_letter(final_x)) + str(rows(x, y)))

            elif len(approx) == 6:
               shape = cv2.putText(img_75, 'Knight/' + str(x) + ", " + str(y), (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
               final_x = columns(x, y)
               list_of_pieces('Knight', str(convert_x_to_letter(final_x)) + str(rows(x, y)))

            elif len(approx) == 7:
                shape = cv2.putText(img_75, 'Pawn/' + str(xSquare) + ", " + str(ySquare), (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
                final_x = columns(x, y)
                list_of_pieces('Pawn', str(convert_x_to_letter(final_x)) + str(rows(x, y)))

            elif len(approx) == 8:
                shape = cv2.putText(img, 'Queen/' + str(xSquare) + ", " + str(ySquare), (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
                final_x = columns(x, y)
                list_of_pieces('Queen', str(convert_x_to_letter(final_x)) + str(rows(x, y)))

            elif len(approx) == 9:
                shape = cv2.putText(img_75, 'King/' + str(xSquare) + ", " + str(ySquare), (x, y),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
                final_x = columns(x, y)
                list_of_pieces('King', str(convert_x_to_letter(final_x)) + str(rows(x, y)))

            #ignore the following elif/else
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

#print( 'Image width is', img_75.shape[1])
#print( 'Image width is', img_75.shape[0])


# displaying the image after drawing contours and labeling shapes
img_75 = cv2.resize(img_75, (1000,1000))
cv2.imshow('shapes', img_75)

cv2.waitKey(0)
cv2.destroyAllWindows()
