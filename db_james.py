#! /usr/bin/python
# drinkBot.py
from Adafruit_MotorHAT import Adafruit_MotorHAT #, Adafruit_DCMotor
from gpiozero import Button
import time


import Adafruit_CharLCD as LCD


# Raspberry Pi pin configuration:
lcd_rs        = 25  # Note this might need to be changed to 21 for older revision Pi's.
lcd_en        = 5
lcd_d4        = 6
lcd_d5        = 12
lcd_d6        = 13
lcd_d7        = 16
lcd_backlight = 4

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows    = 2

#Initialize the LCD using the pins above.
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)
#welcome message
msg = "   Welcome to \n   DrinkBot"
lcd.clear()
lcd.message(msg)

def changeMSG(newMsg):
	msg = newMsg
	lcd.clear()
	lcd.message(msg)

button1 = Button(27)
button2 = Button(22)
button3 = Button(23)
button4 = Button(24)
stopButton = Button(20)

buttonDelay = 0.2 #debounce

pumpTime = 10 * 1000 #amount of time pump automatically runs
pumpTimers = {1:0,2:0,3:0,4:0} #pump timers
mh = Adafruit_MotorHAT(addr=0X60)

def runPump(id):
	global pumpTimers
	if (pumpTimers[id]):
		stopPump(id)
		pumpTimers[id] = 0
	else:
		mid = int((id+1)/2) #set motorID
		motor = mh.getMotor(mid)
		motor.setSpeed(255)
		print("Running pump:",id)
		if id %2:
			motor.run(Adafruit_MotorHAT.FORWARD);
		else:
			motor.run(Adafruit_MotorHAT.BACKWARD);
		pumpTimers[id] = getTime()
		time.sleep(buttonDelay)

# check if running pumps are exceeding pumpTime
def checkPumpTimers():
	global pumpTimers
	for p in pumpTimers:
		if(pumpTimers[p]):
			if((getTime() - pumpTimers[p]) > pumpTime):
				stopPump(p)
				pumpTimers[p] = 0

def stopPump(id):
	print("Stopping pump:",id)
	mh.getMotor(int((id+1)/2)).run(Adafruit_MotorHAT.RELEASE)
	changeMSG("   Welcome to \n   DrinkBot ")

def getTime():
	return int(round(time.time() * 1000))

print("Beginning drinkBot.py")
print("Auto-pump timer set to",pumpTime,"miliseconds.")
while True:
	if button1.is_pressed:
		runPump(1)
		changeMSG("  Dispensing\n Coke")
	elif button2.is_pressed:
		runPump(2)
		changeMSG("  Dispensing\n Sprite")
	elif button3.is_pressed:
		changeMSG("  Dispensing\n Punch")
		runPump(3)
	elif button4.is_pressed:
		changeMSG("  Dispensing\n Water")
		runPump(4)
	elif stopButton.is_pressed:
		stopPump(1)
		stopPump(2)
		stopPump(3)
		stopPump(4)
		print("Stopping")
	checkPumpTimers()
