#! /usr/bin/python
from Adafruit_MotorHAT import Adafruit_MotorHAT #, Adafruit_DCMotor
from gpiozero import Button
import time
from datetime import datetime
import atexit

button1 = Button(27)
button2 = Button(22)
button3 = Button(23)
button4 = Button(24)
buttonDelay = 0.2

b1State = 0
pumpTime = 3 * 1000
mh = Adafruit_MotorHAT(addr=0X60)

def runPump(id,duration=3):
	global pumpList
	mid = int((id+1)/2) #set motorID
	pumpList[id] = getTime()
	motor = mh.getMotor(mid)
	motor.setSpeed(255)
	print("running pump: ",id)
	if id %2:
		motor.run(Adafruit_MotorHAT.FORWARD);
	else:
		motor.run(Adafruit_MotorHAT.BACKWARD);
	time.sleep(buttonDelay)

def stopPumps():
	global pumpList
	for p in pumpList:
		if(pumpList[p]):
			if((getTime() - pumpList[p]) > pumpTime):
				print("stopping pump:",p)
				pumpList[p] = 0
				mh.getMotor(int((p+1)/2)).run(Adafruit_MotorHAT.RELEASE);


def getTime():
	return int(round(time.time() * 1000))

pumpList = {1:0,2:0,3:0,4:0}

while True:
	if button1.is_pressed:
		runPump(1)
	elif button2.is_pressed:
		runPump(2)
	elif button3.is_pressed:
		runPump(3)
	elif button4.is_pressed:
		runPump(4)
	stopPumps()
