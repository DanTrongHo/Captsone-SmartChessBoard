import time 
import board 
from adafruit_motorkit import MotorKit 
from adafruit_motor import stepper

from gpiozero import LED
from time import sleep
red = LED(17)



kit= MotorKit(i2c=board.I2C())

#while True:

#forward path

for i in range(700):
	kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
	
#time.sleep(1.5)

for i in range(300):
	kit.stepper2.onestep(style=stepper.DOUBLE)


time.sleep(5)


for i in range(700):
	kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)

#time.sleep(1.5)

for i in range(700):
	kit.stepper2.onestep(style=stepper.DOUBLE)

time.sleep(5)


for i in range(1400):
	kit.stepper1.onestep(style=stepper.DOUBLE)
	
for i in range(1000):
	kit.stepper2.onestep(direction=stepper.BACKWARD,style=stepper.DOUBLE)


    

#Y-Axis (Stepper 2) 2075 Up = Forward Back= Backwards
#X-Axis (Stepper 1) 2175 Right = Backwards Left = Forward

