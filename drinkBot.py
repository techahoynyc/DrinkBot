#! /usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT #, Adafruit_DCMotor
from gpiozero import Button
import time

button1 = Button(27)
button2 = Button(22)
button3 = Button(23)
button4 = Button(24)
buttonDelay = 0.2 #debounce

pumpTime = 3 * 1000 #amount of time pump automatically runs
pumpTimers = {1:0,2:0,3:0,4:0} #pumpTimers
mh = Adafruit_MotorHAT(addr=0X60)

def runPump(id):
	global pumpTimers
	mid = int((id+1)/2) #set motorID
	motor = mh.getMotor(mid)
	motor.setSpeed(255)
	print("Running pump: ",id)
	if id %2:
		motor.run(Adafruit_MotorHAT.FORWARD);
	else:
		motor.run(Adafruit_MotorHAT.BACKWARD);
	pumpTimers[id] = getTime()
	time.sleep(buttonDelay)

def checkPumpTimers():
	global pumpTimers
	for p in pumpTimers:
		if(pumpTimers[p]):
			if((getTime() - pumpTimers[p]) > pumpTime):
				stopPump(p)
				pumpTimers[p] = 0

def stopPump(id):
	print("Stopping pump: ")
	mh.getMotor(int((id+1)/2)).run(Adafruit_MotorHAT.RELEASE);

def getTime():
	return int(round(time.time() * 1000))

print("Beginning drinkBot.py")
print("Auto-pump timer set to ",pumpTime," second(s)")
while True:
	if button1.is_pressed:
		runPump(1)
	elif button2.is_pressed:
		runPump(2)
	elif button3.is_pressed:
		runPump(3)
	elif button4.is_pressed:
		runPump(4)
	checkPumpTimers()
