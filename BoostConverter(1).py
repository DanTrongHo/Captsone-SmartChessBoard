from gpiozero import LED
from time import sleep
red = LED(17)

while True:
	red.on()
	sleep(3)
	red.off()
	sleep(3)
