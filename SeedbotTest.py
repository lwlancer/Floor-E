def setup(group):
	import RPi.GPIO as io 
	from time import sleep
	io.setmode(io.BOARD)
	if group == 1:
		i1 = 3
		i2 = 5
		e1 = 7
	elif group == 2:
		i1 = 11
		i2 = 13
		e1 = 15
	elif group == 3:
		i1 = 19
		i2 = 21
		e1 = 23
	elif group == 4:
		i1 = 29
		i2 = 31
		e1 = 33
	elif group == 5:
		i1 = 8
		i2 = 10
		e1 = 12
	elif group == 6:
		i1 = 22
		i2 = 24
		e1 = 26
	elif group == 7:
		i1 = 36
		i2 = 38
		e1 = 40
	elif group == 8:
		i1 = 35
		i2 = 37
		e1 = 32
	forward = 1 
	reverse = 2
	pwm=io.PWM(e1, 50)
	pwm.start(0)
def runDC(pingroup, duty, direction, duration):
	setup(pingroup)
	if direction == 1:
		io.output(i1, True)
		9io.output(i2, False)
	elif direction == 2:
		io.output(i1, False)
		io.output(i2, True)
	else:
		print("Unrecognized Input Detected")
	pwm.ChangeDutyCycle(duty)
	io.output(e1, True)
	sleep(duration)
	io.output(e1, False)
	pwm.stop
	io.cleanup()
