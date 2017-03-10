def setup(group):
	global import RPi.GPIO as io 
	global from time import sleep
	global io.setmode(io.BOARD)
	if group == 1:
		global i1 = 3
		global i2 = 5
		global e1 = 7
	elif group == 2:
		global i1 = 11
		global i2 = 13
		global e1 = 15
	elif group == 3:
		global i1 = 19
		global i2 = 21
		global e1 = 23
	elif group == 4:
		global i1 = 29
		global i2 = 31
		global e1 = 33
	elif group == 5:
		global i1 = 8
		global i2 = 10
		global e1 = 12
	elif group == 6:
		global i1 = 22
		global i2 = 24
		global e1 = 26
	elif group == 7:
		global i1 = 36
		global i2 = 38
		global e1 = 40
	elif group == 8:
		global i1 = 35
		global i2 = 37
		global e1 = 32
	global forward = 1 
	global reverse = 2
	global DC = 1
	global Servo = 2
	global pwm=io.PWM(e1, 50)
	global pwm.start(0)
def runDC(pingroup, duty, direction, duration):
	setup(pingroup)
	if direction == 1:
		io.output(i1, True)
		io.output(i2, False)
	elif direction == 2:
		io.output(i1, False)
		io.output(i2, True)
	else:
		print("Unrecognized Input Detected")
	pwm.ChangeDutyCycle(duty)
	io.output(e1, True)
	sleep(duration)
	io.output(e1, False)
	pwm.stop()
	io.cleanup()
def runServo(pingroup, angle):
	setup(pingroup)
	freq = angle * .05520268341422 + 2.029955093436
	io.output(e1, True)
	pwm.ChangeDutyCycle(freq)
	sleep(1)
	io.output(e1, False)
	pwm.stop()
	io.cleanup()
def run(DCorSERVO, pingroup, duration, angle, duty, direction)
	if DCorSERVO == 1:
		runDC(pingroup, duty, direction, duration)
	elif DCorSERVO == 2:
		runServo(pingroup, angle)
	else:
		print("Unrecognized Input Detected")
def run2(pingroup1, angle1, pingroup2, angle2)
	runServo(pingroup1, angle1)
	runServo(pingroup2, angle2)
def run3(pingroup1, angle1, pingroup2, angle2, pingroup3, angle3)
	runServo(pingroup1, angle1)
	runServo(pingroup2, angle2)
	runServo(pingroup3, angle3)
