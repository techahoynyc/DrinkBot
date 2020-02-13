#! /usr/bin/python/
'''
This code clears all the tubes from liquid. Be sure to remove tubes from bottles
before running this command
'''
from Adafruit_MotorHAT import Adafruit_MotorHAT
from gpiozero import Button
from time import sleep
import os

path = "python3 /home/pi/DrinkBot/pump.py "

os.system(path + "1 7")
os.system(path + "2 7")
os.system(path + "3 7")
os.system(path + "4 7")
