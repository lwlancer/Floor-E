import RPi.GPIO as io
from time import sleep
import keyboard

#Left Drive Output Bus Setup
io.setup(8, io.OUT)            #Left Drive PWM
pwm_left=io.PWM(8, 50)
pwm_left.start(0)
io.setup(10, io.OUT)           #Left Drive E1
io.setup(12, io.OUT)           #Left Drive E2

#Right Drive Output Bus Setup
io.setup(22, io.OUT)           #Right Drive PWM
pwm_right=io.PWM(22, 50)
pwm_right.start(0)
io.setup(24, io.OUT)           #Right Drive E1
io.setup(26, io.OUT)           #Right Drive E2

#Servo PWM Setup
io.setup(16, io.out)
pwm_servo=io.PWM(16, 50)
pwm_servo.start(16)

def set_speed_left(direction, speed):          #Direction should be input as 0 for reverse and 1 for forward, and speed as an integer between 0-100
    if direction == 0:
        io.output(10, True)
        io.output(12, False)
    elif direction == 1:
        io.output(10, False)
        io.output(12, True)
    pwm_left.ChangeDutyCycle(speed)
    io.output(8, True)

def set_speed_right(direction, speed):          #Direction should be input as 0 for reverse and 1 for forward, and speed as an integer between 0-100
    if direction == 0:
        io.output(24, True)
        io.output(26, False)
    elif direction == 1:
        io.output(24, False)
        io.output(26, True)
    pwm_right.ChangeDutyCycle(speed)
    io.output(22, True)

def set_head_angle(angle):                      #TBD what angles are accetpable
    freq = angle / 18 + 2
    io.output(16, True)
    pwm_servo.ChangeDutyCycle(freq)
    io.output(16, False)

#Main Control Structure
def forward_full():
    set_speed_left(1,100)
    set_speed_right(1,100)
def reverse_full():
    set_speed_left(0,100)
    set_speed_right(0,100)
def turn_left():
    set_speed_left(0,25)
    set_speed_right(1,25)
def turn_right():
    set_speed_left(1,25)
    set_speed_right(0,25)

# Define keyboard bindings
keyboard.add_hotkey('w', forward_full)  # 'w' key for forward full speed
keyboard.add_hotkey('s', reverse_full)  # 's' key for reverse full speed
keyboard.add_hotkey('a', turn_left)     # 'a' key for turn left
keyboard.add_hotkey('d', turn_right)    # 'd' key for turn right

#Run the robot
keyboard.wait('esc')  # Wait for the 'esc' key to exit

#Stop and Cleanup
pwm_left.stop()
pwm_right.stop()
io.cleanup()