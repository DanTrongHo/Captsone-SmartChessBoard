##### This is the main autorun script

### Imports
import cv2
import numpy as np
from matplotlib import pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import math
import itertools
from numpy import array as Ar
import numpy as np
### Imports for bluetooth stuff
import dbus
from promisio import promisify
from advertisement import Advertisement
from service import Application, Service, Characteristic, Descriptor



## Pathfinding function imported from Graysons Pathfinding(with lag).py
###This function takes in center coordinates from the start/end squares and determines the best path for the magnet to move ###
## Written with the idea that the x/y origin is in the bottom left corner (magnet home) and input coordinates are center of squares###
## Double check motors forward/backwards direction in lab ##
def pathfinding(start_x, start_y, end_x, end_y, lag): ## DAN: Function takes in int start square x/y coords, int end square x/y coords, and bool lag (true, false)
	
	#initializations
	direction_start_x = "NONE" #Used to help tell the direction to step (FORWARD or BACKWARD)
	direction_start_y = "NONE" #Used to help tell the direction to step 

	direction_end_x = "NONE" #Used to help tell the direction to step 
	direction_end_y = "NONE" #Used to help tell the direction to step 

	direction_main_x = "NONE" #Used to help tell the direction to step (FORWARD or BACKWARD)
	direction_main_y = "NONE" #Used to help tell the direction to step (FORWARD or BACKWARD)

	motor_start_x = 0 #number of steps motors need to move in x direction to get out of square
	motor_start_y = 0 #number of steps motors need to move in y direction to get out of square

	motor_end_x = 0 #number of steps motors need to move in x direction to get into square
	motor_end_y = 0 #number of steps motors need to move in y direction to get into square

	motor_main_x = 0 #number of steps motors need to move in x direction
	motor_main_y = 0 #number of steps motors need to move in y direction

	total_x = abs(end_x - start_x) #total number of x steps that need to be traveled
	total_y = abs(end_y - start_y) #total number of y steps that need to be traveled

	lag_steps = 70 #number of extra steps needed to account for the lag of the piece when being dragged
	half_step = 200 #number of steps needed to enter/exit center of square from seam line

	#these if-else statements are for piece movement

	if start_x == end_x and start_y < end_y: #only y direction travel required, up (scenario 5)
		motor_start_x = half_step #number of steps to get out of square (LEFT)
		direction_start_x = "FORWARD"
		motor_start_y = 0 #no movement (NONE)
		direction_start_y = "NONE"

		motor_end_x = half_step #number of steps to get into square (RIGHT)
		direction_end_x = "BACKWARD"
		motor_end_y = 0 #no movement (NONE)
		direction_end_y = "NONE"

		motor_main_y = total_y - (motor_start_y + motor_end_y) #step count for main path in y direction (UP)
		direction_main_y = "FORWARD"


		if lag == "true"
			motor_end_x += lag_steps # total number of steps to get into square (RIGHT)

	elif start_x == end_x and start_y > end_y: #only y direction travel required, down (scenario 6)
		motor_start_x = half_step #number of steps to get out of square (RIGHT)
		direction_start_x = "BACKWARD"
		motor_start_y = 0 #no movement (NONE)
		direction_start_y = "NONE"

		motor_end_x = half_step #number of steps to get into square (LEFT)
		direction_end_x = "FORWARD"
		motor_end_y = 0 #no movement (NONE)
		direction_end_y = "NONE"

		motor_main_y = total_y - (motor_start_y + motor_end_y) #step count for main path in y direction (DOWN)
		direction_main_y = "BACKWARD"

		if lag == "true"
			motor_end_x += lag_steps # total number of steps to get into square (RIGHT)

	elif start_x > end_x and start_y == end_y: #only x direction travel required, Left (scenario 7)
		motor_start_x = 0 #no movement (NONE)
		direction_start_x = "NONE"
		motor_start_y = half_step #number of steps to get out of square (UP)
		direction_start_y = "FORWARD"

		motor_end_x = 0 #no movement (NONE)
		direction_end_x = "NONE"
		motor_end_y = half_step #number of steps to get into square (DOWN)
		direction_end_y = "BACKWARD"

		motor_main_x = total_x - (motor_start_x + motor_end_x) #step count for main path in x direction (LEFT)
		direction_main_x = "FORWARD"

		if lag == "true"
			motor_end_y += lag_steps # total number of steps to get into square

	elif start_x > end_x and start_y == end_y: #only x direction travel required, Right (scenario 8)
		motor_start_x = 0 #no movement (NONE)
		direction_start_x = "NONE"
		motor_start_y = half_step #number of steps to get out of square (DOWN)
		direction_start_y = "BACKWARD"

		motor_end_x = 0 #no movement (NONE)
		direction_end_x = "NONE"
		motor_end_y = half_step #number of steps to get into square (UP)
		direction_end_y = "FORWARD"

		motor_main_x = total_x - (motor_start_x + motor_end_x) #step count for main path in x direction (RIGHT)
		direction_main_x = "BACKWARD"

		if lag == "true"
			motor_end_y += lag_steps # total number of steps to get into square

	elif start_x > end_x and start_y < end_y: #move piece left and up (scenario 1)
		motor_start_x = 0 #no movement (NONE)
		direction_start_x = "NONE"
		motor_start_y = half_step #number of steps to get out of square (UP)
		direction_start_y = "FORWARD"

		motor_end_x = half_step #number of steps to get into square (LEFT)
		direction_end_x = "FORWARD"
		motor_end_y = 0 #no movement (NONE)
		direction_end_y = "NONE"

		motor_main_x = total_x - (motor_start_x + motor_end_x) #step count for main path in x direction (LEFT)
		direction_main_x = "FORWARD"
		motor_main_y = total_y - (motor_start_y + motor_end_y) #step count for main path in y direction (UP)
		direction_main_y = "FORWARD"

		if lag == "true"
			motor_end_x += lag_steps # total number of steps to get into square

	elif start_x < end_x and start_y > end_y: #move piece right and down (scenario 2)
		motor_start_x = 0 #no movement (NONE)
		direction_start_x = "NONE"
		motor_start_y = half_step #number of steps to get out of square (DOWN)
		direction_start_y = "BACKWARD"

		motor_end_x = half_step #number of steps to get into square (RIGHT)
		direction_end_x = "BACKWARD"
		motor_end_y = 0 #no movement (NONE)
		direction_end_y = "NONE"

		motor_main_x = total_x - (motor_start_x + motor_end_x) #step count for main path in x direction (RIGHT)
		direction_main_x = "BACKWARD"
		motor_main_y = total_y - (motor_start_y + motor_end_y) #step count for main path in y direction (DOWN)
		direction_main_y = "BACKWARD"

		if lag == "true"
			motor_end_x += lag_steps # total number of steps to get into square

	elif start_x > end_x and start_y > end_y: #move piece left and down (scenario 3)
		motor_start_x = 0 #no movement (NONE)
		direction_start_x = "NONE"
		motor_start_y = half_step #number of steps to get out of square (DOWN)
		direction_start_y = "BACKWARD"

		motor_end_x = half_step #number of steps to get into square (LEFT)
		direction_end_x = "FORWARD"
		motor_end_y = 0 #no movement (NONE)
		direction_end_y = "NONE"

		motor_main_x = total_x - (motor_start_x + motor_end_x) #step count for main path in x direction (LEFT)
		direction_main_x = "FORWARD"
		motor_main_y = total_y - (motor_start_y + motor_end_y) #step count for main path in y direction (DOWN)
		direction_main_y = "BACKWARD"

		if lag == "true"
			motor_end_x += lag_steps # total number of steps to get into square

	elif start_x < end_x and start_y < end_y: #move piece right and up (scenario 4)
		motor_start_x = 0 #no movement (NONE)
		direction_start_x = "NONE"
		motor_start_y = half_step #number of steps to get out of square (UP)
		direction_start_y = "FORWARD"

		motor_end_x = half_step #number of steps to get into square (RIGHT)
		direction_end_x = "BACKWARD"
		motor_end_y = 0 #no movement (NONE)
		direction_end_y = "NONE"

		motor_main_x = total_x - (motor_start_x + motor_end_x) #step count for main path in x direction (RIGHT)
		direction_main_x = "BACKWARD"
		motor_main_y = total_y - (motor_start_y + motor_end_y) #step count for main path in y direction (UP)
		direction_main_y = "FORWARD"

		if lag == "true"
			motor_end_x += lag_steps # total number of steps to get into square

	return motor_start_x, motor_start_y, direction_start_x, direction_start_y, motor_main_x, motor_main_y, direction_main_x, direction_main_y, motor_end_x, motor_end_y, direction_end_x, direction_end_y

## DAN: motor_start_x and motor_start_y (both ints) are the step counts needed for the motors to exit the starting square, followed by their respective stepper motor command directions (both string) (FORWARD/BACKWARD)
## motor_main_x and motor_main_y (both ints) are the step counts needed for the long distance seam traveling, followed by their respective stepper motor command directions (both string) (FORWARD/BACKWARD)
## motor_end_x and motor_end_y (both ints) are the step counts needed to get from the seam into the end square (with lag adjustment), followed by their respective stepper motor command directions (both string) (FORWARD/BACKWARD)
## Need to somehow have motor go back 70 steps after magent turns off and piece is released when lag is adjusted for so that the magnet is back to the center of thr square if that makes sense ##


## Function imported from Mo's Chess Script.py
def update_internal_board():
	emptylist=[]
	x=0

	"""
	Pawn =1 
	Rook = 2
	Knight =3
	Bishop = 4
	Queen= 5
	King =6
	"""


	start=np.array([
        [2,3,4,5,6,4,3,2],
        [1,1,1,1,1,1,1,1],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0],
         [1,1,1,1,1,1,1,1],
         [2,3,4,5,6,4,3,2]]
        )  #Initial Chess board

	BigDict = {     #Dictionary to convert Bluetooth Data into piece movement steps
        'a' : 200,
        'b' : 400,
        'c' : 600,
        'd' : 800,
        'e' : 900,
        'f' : 1100,
        'g' : 1300,
        
        '1' : 200,
        '2' : 400,
        '3' : 600,
        '4' : 800,
        '5' : 1000,
        '6' : 1200,
        '7' : 1400,
        '8' : 1600,
        
	}


	ArrayDict = {     #Dictonary to update array
        'a' : 0,
        'b' : 1,
        'c' : 2,
        'd' : 3,
        'e' : 4,
        'f' : 5,
        'g' : 6,
        'h' : 7,
        
        '1' : 0,
        '2' : 1,
        '3' : 2,
        '4' : 3,
        '5' : 4,
        '6' : 5,
        '7' : 6,
        '8' : 7,
        
	}

	DanString=(input("Input Dan String")) #will always be a 5 letter string in the form of e4-e5

	GrabX= BigDict[DanString[0]]
	GrabY= BigDict[DanString[1]]

	#Movement script for motors to go to Grab X , Grab Y then turn on Electromagnet


	print("Grabbing (",GrabX,",",GrabY,")")


	DropX= BigDict[DanString[3]]
	DropY= BigDict[DanString[4]]

	#Movement script for motors to go to DropX , DropY then turn off Electromagnet


	#Electromagnet go home 


	print(ArrayDict[DanString[0]])
	print(ArrayDict[DanString[1]])
	POI=start[ArrayDict[DanString[1]]][ArrayDict[DanString[0]]]
	print("piece moved is the", POI)

	#print(POI)
	start[ArrayDict[DanString[1]]][ArrayDict[DanString[0]]]=0
	start[ArrayDict[DanString[4]]][ArrayDict[DanString[3]]]=POI

	print(start)



	#print(start)
	#print(start[0][0])
	#print(BigDict["a"])

	""" ///
	Legal Piece movement Check
	//"""



	"""
	Pawn =1 
	Rook = 2
	Knight =3
	Bishop = 4
	Queen= 5
	King =6
	"""
	#start[ArrayDict['a']][ArrayDict['1']] = x 


	"""
	def cfu_func(a,b,x):
		for aRow in range(Rows):
			EachRow=[]
			for aCol in range (Cols):
					EachRow.append(0)
			emptylist.append(EachRow)
			final_array=Ar(emptylist)
		return(final_array)
	print(cfu_func(Cols,Rows,x))


	"""
	return


## Function imported from Swades ShapeID_pic_resize_CoordList.py
def ShapeID():
	# For reading/slecting image
	img = cv2.imread('locationTest2.jpg')

	img_75 = cv2.resize(img, None, fx = 0.6, fy = 0.6)
	#img_75 = cv2.resize(img, (1220,1220))
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

		coordinate_list = []
		def list_of_pieces(str, x_coord, y_coord):
			L = []
			L.append(str)
			L.append(x_coord)
			L.append(y_coord)
			print(L) #!!!!!This is the output variable to got to app/pi and it is a List variable!!!!!!




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
					list_of_pieces('Rook',xSquare,ySquare)
				elif len(approx) == 5:
					shape = cv2.putText(img_75, 'Bishop/' + str(xSquare) + ", " + str(ySquare), (x, y),
								cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
					list_of_pieces('Bishop', xSquare, ySquare)
				elif len(approx) == 6:
				   shape = cv2.putText(img_75, 'Knight/' + str(xSquare) + ", " + str(ySquare), (x, y),
								cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
				   list_of_pieces('Knight', xSquare, ySquare)
				elif len(approx) == 7:
					shape = cv2.putText(img_75, 'Pawn/' + str(xSquare) + ", " + str(ySquare), (x, y),
								cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
					list_of_pieces('Knight', xSquare, ySquare)
				elif len(approx) == 8:
					shape = cv2.putText(img_75, 'Queen/' + str(xSquare) + ", " + str(ySquare), (x, y),
								cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
					list_of_pieces('Queen', xSquare, ySquare)
				elif len(approx) == 9:
					shape = cv2.putText(img_75, 'King/' + str(xSquare) + ", " + str(ySquare), (x, y),
								cv2.FONT_HERSHEY_SIMPLEX, 0.6, (124, 252, 0), 2)
					list_of_pieces('King', xSquare, ySquare)
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
	cv2.imshow('shapes', img_75)

	cv2.waitKey(0)
	cv2.destroyAllWindows()
