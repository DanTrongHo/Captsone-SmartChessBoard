from getkey import getkey, keys

import time 
import board 
from adafruit_motorkit import MotorKit 
from adafruit_motor import stepper

kit= MotorKit(i2c=board.I2C())
x=0
y=0

key = getkey()
poop=True

while poop:
  if key == keys.DOWN:
    kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)  # Handle the UP key
    y=y-1
    print("(",x,",",y,")")
    
    
  elif key == keys.UP:
    y=y+1
    kit.stepper1.onestep(style=stepper.DOUBLE)  # Handle the DOWN key
    print("(",x,",",y,")")
   
  elif key == keys.RIGHT:
    x=x+1
    kit.stepper2.onestep(direction=stepper.BACKWARD,style=stepper.DOUBLE)  # Handle the LEFT KEY
    print("(",x,",",y,")")
    
  elif key == keys.LEFT:
    x=x-1
    kit.stepper2.onestep(style=stepper.DOUBLE)   # Handle RIGHT KEY
    print("(",x,",",y,")")
    
  key = getkey()
  
print("done")
"""
  else:
  # Handle other text characters
    buffer += key
    print(buffer)
"""

"""
From origin to first graveyard = (95,200)
Next over= (495,200)
Center to center of square = 400 Steps
