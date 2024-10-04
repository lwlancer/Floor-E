import RPi.GPIO as io
from time import sleep

#Left Drive Output Bus Setup
io.setup(8, io.OUT)            #Left Drive PWM
io.setup(10, io.OUT)           #Left Drive E1
io.setup(12, io.OUT)           #Left Drive E2

#Right Drive Output Bus Setup
io.setup(22, io.OUT)           #Right Drive PWM
io.setup(24, io.OUT)           #Right Drive E1
io.setup(26, io.OUT)           #Right Drive E2

#Servo PWM Setup
io.setup(16, io.out)

