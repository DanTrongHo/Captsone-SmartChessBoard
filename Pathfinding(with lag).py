### This function takes in center coordinates from the start/end squares and determines the best path for the magnet to move ###
### Written with the idea that the x/y origin is in the bottom left corner (magnet home) and input coordinates are center of squares###

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
