#! /usr/bin/python/
from Adafruit_MotorHAT import Adafruit_MotorHAT
from gpiozero import Button
from time import sleep
import os

button1 = Button(27)
button2 = Button(22)
button3 = Button(23)
button4 = Button(24)
path = "python3 /home/pi/DrinkBot/pump.py "
while True:
	if button1.is_pressed:
		os.system(path + "1 180")
		print("Pressed")
	elif button2.is_pressed:
		os.system(path + "2 180")
		print("Pressed")
	elif button3.is_pressed:
		os.system(path + "3 180")
		print("Pressed")
	elif button4.is_pressed:
		os.system(path + "4 180")
		print("Pressed")
	else:
		print("Released")

	sleep(.1)
