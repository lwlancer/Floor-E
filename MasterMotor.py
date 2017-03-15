import RPi.GPIO as io
from time import sleep
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
    io.setmode(io.BOARD)
    io.setwarnings(False)
    global forward
    forward = 1
    global reverse
    reverse = 2
    global DC
    DC = 1
    global Servo
    Servo = 2
    global Stepper
    Stepper = 3
    global i1
    global i2
    global e1
    global a1
    global a2
    global b1
    global b2
    if mtype == 1:
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
        else:
                print("Error at DC pin setup")
        io.setup(i1, io.OUT)
        io.setup(i2, io.OUT)
        io.setup(e1, io.OUT)
        global pwm
        pwm=io.PWM(e1, 50)
        pwm.start(0)
    elif mtype == 2:
            e1 = group
            io.setup(e1, io.OUT)
            global pwm
            pwm=io.PWM(e1, 50)
            pwm.start(0)
    elif mtype == 3:
        if group == 1:
            a1 = 3
            a2 = 5
            b1 = 7
            b2 = 8
            e1 = 10
        elif group == 2:
            a1 = 11
            a2 = 12
            b1 = 13
            b2 = 15
            e1 = 16
        elif group == 3:
            a1 = 18
            a2 = 19
            b1 = 21
            b2 = 22
            e1 = 23
        elif group == 4:
            a1 = 24
            a2 = 26
            b1 = 29
            b2 = 31
            e1 = 32
        elif group == 5:
            a1 = 33
            a2 = 35
            b1 = 36
            b2 = 37
            e1 = 38
        else:
            print("Error at Stepper pin setup")
        io.setup(a1, io.OUT)
        io.setup(a2, io.OUT)
        io.setup(b1, io.OUT)
        io.setup(b2, io.OUT)
        io.setup(e1, io.OUT)
    else:
        print("Error at motor type selection")
def runDC(pingroup, duty, direction, duration):
    setup(pingroup, 1)
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
    setup(pingroup, 2)
    freq = angle / 18 + 2
    io.output(e1, True)
    pwm.ChangeDutyCycle(freq)
    sleep(.5)
    io.output(e1, False)
    pwm.stop()
    io.cleanup()
    
def setsteps(n1, n2, n3, n4, pingroup):
    setup(pingroup, 3)
    io.output(a1, n1)
    io.output(a2, n2)
    io.output(b1, n3)
    io.output(b2, n4)
    
def runStepper(pingroup, delay, steps):
    setup(pingroup, 3)
    if steps > 0:
        io.output(e1, True)
        for i in range(0, steps):
            setsteps(1,0,1,0, pingroup)
            sleep(delay)
            setsteps(0,1,1,0, pingroup)
            sleep(delay)
            setsteps(0,1,0,1, pingroup)
            sleep(delay)
            setsteps(1,0,0,1, pingroup)
            sleep(delay)
    elif steps < 0:
        steps = abs(steps)
        for i in range(0, steps):
            setsteps(1,0,0,1, pingroup)
            sleep(delay)
            setsteps(0,1,0,1, pingroup)
            sleep(delay)
            setsteps(0,1,1,0, pingroup)
            sleep(delay)
            setsteps(1,0,1,0, pingroup)
            sleep(delay)
    elif steps == 0:
        print("You dumb")
    else:
        print("Error at step analyzer:")
def run(motortype, pingroup, duration, angle, duty, direction, delay, steps):
    if motortype == 1:
        runDC(pingroup, duty, direction, duration)
    elif motortype == 2:
        runServo(pingroup, angle)
    elif motortype == 3:
            runStepper(pingroup, delay, steps)
    else:
        print("Unrecognized Input Detected")
