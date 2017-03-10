print("DC Group 1, pins 3;5;7; Ready:")
print("DC Group 2, pins 11;13;15; Ready:")
print("DC Group 3, pins 19;21;23; Ready:")
print("DC Group 4, pins 29;31;33; Ready:")
print("DC Group 5, pins 8;10;12; Ready:")
print("DC Group 6, pins 22;24;26; Ready:")
print("DC Group 7, pins 36;38;40; Ready:")
print("DC Group 8, pins 35:37;32; Ready:")

print("Servo ready for use on pins 3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 18, 19, 21, 22, 23, 24, 26, 29, 31, 32, 33, 35, 36, 37, 38, and 40")

print("Stepper Group 1, pins 3;5;7;8;10; Ready:")
print("Stepper Group 2, pins 11;12;13;15;16; Ready:")
print("Stepper Group 3, pins 18;19;21;22;23; Ready:")
print("Stepper Group 4, pins 24;26;29;31;32; Ready:")
print("Stepper Group 5, pins 33;35;36;37;38; Ready:")

def setup(group, mtype):
	global import RPi.GPIO as io 
	global from time import sleep
	global io.setmode(io.BOARD)
     	global forward = 1 
	global reverse = 2
	global DC = 1
	global Servo = 2
      	global Stepper = 3
	if mtype == 1:
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
      		else:
      			print("Error at DC pin setup")
      	elif mtype == 2:
      		global e1 = group
	elif mtype == 3:
		if group == 1:
			global a1 = 3
			global a2 = 5
			global b1 = 7
			global b2 = 8
			global e1 = 10
		elif group == 2:
			global a1 = 11
			global a2 = 12
			global b1 = 13
			global b2 = 15
			global e1 = 16
		elif group == 3:
			global a1 = 18
			global a2 = 19
			global b1 = 21
			global b2 = 22
			global e1 = 23
		elif group == 4:
			global a1 = 24
			global a2 = 26
			global b1 = 29
			global b2 = 31
			global e1 = 32
		elif group == 5:
			global a1 = 33
			global a2 = 35
			global b1 = 36
			global b2 = 37
			global e1 = 38
		else:
			print("Error at Stepper pin setup")
	else:
		print("Error at motor type selection")
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
	freq = angle / 18 + 2
	io.output(e1, True)
	pwm.ChangeDutyCycle(freq)
	sleep(1)
	io.output(e1, False)
	pwm.stop()
	io.cleanup()
def run(motortype, pingroup, duration, angle, duty, direction, delay, steps)
	if motortype == 1:
		runDC(pingroup, duty, direction, duration)
	elif motortype == 2:
		runServo(pingroup, angle)
	elif motortype == 3:
      		runStepper(pingroup, delay, steps)
	else:
		print("Unrecognized Input Detected")
