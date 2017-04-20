import RPi.GPIO as io
from time import sleep
from math import *

m1i1 = 
m1i2 = 
m1e1 = 
m2i1 = 
m2i2 =
m2e1 = 
m3i1 = 
m3i2 = 
m3e1 = 

sqrt3o2 = 1.0 * sqrt(3) / 2

io.setmode(io.BOARD)
io.setup(m1i1, io.OUT)
io.setup(m1i2, io.OUT)
io.setup(m1e1, io.OUT)
io.setup(m2i1, io.OUT)
io.setup(m2i2, io.OUT)
io.setup(m2e1, io.OUT)
io.setup(m3i1, io.OUT)
io.setup(m3i2, io.OUT)
io.setup(m3e1, io.OUT)

pwm1 = io.PWM(m1e1, 50)
pwm2 = io.PWM(m2e1, 50)
pwm3 = io.PWM(m3e1, 50)
pwm1.start(0)
pwm2.start(0)
pwm3.start(0)

def get_angle():
	ang = input("Specify Direction of Movement (Degrees): ")
	global theta
	theta = radians(ang)
def calculate_xy_vectors(angl):
	global vx
	global vy
	vx = cos(angl)
	vy = sin(angl)

def calculate_w_vectors(v_x, v_y):
	global w1
	global w2
	global w3
	w1 = - vx
	w2 = 0.5 * v_x - sqrt3o2 * v_y
	w3 = 0.5 * v_x + sqrt3o2 * v_y
	if w1 < 0:
		w1_ccw = True
	elif w1 >= 0:
		w1_ccw = False
	if w2 < 0:
		w2_ccw = True
	elif w2 >= 0:
		w2_ccw = False
	if w3 < 0:
		w3_ccw = True
	elif w3 >= 0:
		w3_ccw = False
def go(degree, time)
	get_angle()
	calculate_xy_vectors(theta)
	calculate_w_vectors(vx, vy)
	for i in range(0, time):
		if w1_ccw is True:
			io.output(m1i1, False)
			io.output(m1i2, True)
			io.output(m1e1, True)
			pwm1.ChangeDutyCycle(w1)
		elif w1_ccw is False:
			io.output(m1i1, True)
			io.output(m1i2, False)
			io.output(m1e1, True)
			pwm1.ChangeDutyCycle(w1)
		if w2_ccw is True:
			io.output(m2i1, False)
			io.output(m2i2, True)
			io.output(m2e1, True)
			pwm2.ChangeDutyCycle(w2)
		elif w2_ccw is False:
			io.output(m2i1, True)
			io.output(m2i2, False)
			io.output(m2e1, True)
			pwm2.ChangeDutyCycle(w2)
		if w3_ccw is True:
			io.output(m3i1, False)
			io.output(m3i2, True)
			io.output(m3e1, True)
			pwm3.ChangeDutyCycle(w3)
		elif w3_ccw is False:
			io.output(m3i1, True)
			io.output(m3i2, False)
			io.output(m3e1, True)
			pwm3.ChangeDutyCycle(w3)
		sleep(1)
	pwm1.stop()
	pwm2.stop()
	pwm3.stop()
	io.output(m1e1, False)
	io.output(m2e1, False)
	io.output(m3e1, False)
	io.cleanup()
	
