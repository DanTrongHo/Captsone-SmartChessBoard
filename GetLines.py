# Take a 9x9 array of coordinates and calculates a quadratic equation for each row/column
import numpy
import matplotlib.pyplot as plt
from numpy import array
import string

mainArray = []
RowList = []
ColumnList = []
def makeArray():
    f = open("CameraCoordinates.txt", 'r')
    i = 0
    tempArray = []
    for line in f:
        line = line.rstrip()
        if i < 9: # if not full column then just append to the temp array
            tempArray.append(line)
            i = i + 1
        else: # Column is full need to reset the i counter, append the temp array to the main array, and append the current readline to a new array
            i = 1
            mainArray.append(tempArray.copy())
            tempArray.clear()
            tempArray.append(line)
    f.close()

def getY(coord):
    commaPosition = coord.find(',')
    return int(coord[commaPosition+1:])

def getX(coord):
    commaPosition = coord.find(',')
    return int(coord[:commaPosition])

def fillRow(): # top down order
    for i in range(len(mainArray)):
        tempYList = []
        tempXList = []
        for j in range(9):
            tempYList.append(getY(mainArray[i][j]))
            tempXList.append(getX(mainArray[i][j]))
        # Input array and get the equation, append to the row list
        print(tempXList)
        RowList.append(numpy.polyfit(array(tempXList), array(tempYList), 1))



def fillColumn(): # left to right order
    for i in range(9):
        tempYList = []
        tempXList = []
        for j in range(9):
            tempYList.append(getY(mainArray[j][i]))
            tempXList.append(getX(mainArray[j][i]))
        # Input array and get the equation, append to the row list
        ColumnList.append(numpy.polyfit(array(tempXList), array(tempYList), 1))

def main():
    # Need to go through each row and make a quadratic equation from the lines using polyfit
    # polyfit requires an array of x coordinates, an array of y coordinates, and the degree of polynomial (2)
    makeArray()
    fillRow()
    fillColumn()
    print("Rows:")
    print(RowList)
    print("---------")
    print("Column:")
    print(ColumnList)

main()