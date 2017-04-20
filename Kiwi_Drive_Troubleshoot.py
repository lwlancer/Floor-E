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

print("Mode set to BOARD")
print("Motor 1 Input 1 Initialized")
print("Motor 1 Input 2 Initialized")
print("Motor 1 Enable 1 Initialized")
print("Motor 2 Input 1 Initialized")
print("Motor 2 Input 2 Initialized")
print("Motor 2 Enable 1 Initialized")
print("Motor 3 Input 1 Initialized")
print("Motor 3 Input 2 Initialized")
print("Motor 3 Enable 1 Initialized")


print("PWM1 Initialized")
print("PWM2 Initialized")
print("PWM3 Initialized")
print("PWM1 Started at 0")
print("PWM2 Started at 0")
print("PWM3 Started at 0")

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
	w1 = - v_x
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
def go(time)
	get_angle()
	calculate_xy_vectors(theta)
	calculate_w_vectors(vx, vy)
	for i in range(0, time):
		if w1_ccw is True:
			print("Motor 1 Input 1: False")
			print("Motor 1 Input 2: True")
			print("Motor 1 Enable 1:True")
			Print("PWM1 set to %s" % w1)
		elif w1_ccw is False:
			print("Motor 1 Input 1: True)
			print("Motor 1 Input 2: False")
			print("Motor 1 Enable 1:True")
			Print("PWM1 set to %s" % w1)
		if w2_ccw is True:
			print("Motor 2 Input 1: False")
			print("Motor 2 Input 2: True")
			print("Motor 2 Enable 1:True")
			Print("PWM2 set to %s" % w2)
		elif w2_ccw is False:
			print("Motor 2 Input 1: True")
			print("Motor 2 Input 2: False")
			print("Motor 2 Enable 1:True")
			Print("PWM2 set to %s" % w2)
		if w3_ccw is True:
			print("Motor 3 Input 1: False")
			print("Motor 3 Input 2: True")
			print("Motor 3 Enable 1:True")
			Print("PWM3 set to %s" % w3))
		elif w3_ccw is False:
			print("Motor 3 Input 1: True")
			print("Motor 3 Input 2: False")
			print("Motor 3 Enable 1:True")
			Print("PWM3 set to %s" % w3)
		sleep(1)
    
	print("PWM1 Stopped")
	print("PWM2 Stopped")
	print("PWM3 Stopped")
	print("Motor 1 Enable 1: False")
	print("Motor 2 Enable 1: False")
	print("Motor 3 Enable 1: False")
	print("GPIO Cleanup")
