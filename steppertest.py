import RPi.GPIO as io
from time import sleep
io.setmode(io.BOARD)
io.setwarnings(False)

e1 = 37
a1 = 35
a2 = 33
b1 = 31
b2 = 29

io.setup(e1, io.OUT)
io.setup(a1, io.OUT)
io.setup(a2, io.OUT)
io.setup(b1, io.OUT)
io.setup(b2, io.OUT)

io.output(e1, True)

def setStep(i1, i2, i3, i4):
    io.output(a1, i1)
    io.output(a2, i2)
    io.output(b1, i3)
    io.output(b2, i4)

def clockstep(delay, steps):
    for i in range(0, steps):
        setStep(True, False, True, False)
        sleep(delay)
        setStep(False, True, True, False)
        sleep(delay)
        setStep(False, True, False, True)
        sleep(delay)
        setStep(True, False, False, True)
        sleep(delay)

def counterstep(delay, steps):
    for i in range(0, steps):
        setStep(True, False, False, True)
        sleep(delay)
        setStep(False, True, False, True)
        sleep(delay)
        setStep(False, True, True, False)
        sleep(delay)
        setStep(True, False, True, False)
        sleep(delay)

while True:
    delay = raw_input("Delay (in milliseconds):")
    steps = raw_input("Steps Forward:")
    clockstep(int(delay) / 1000.0, int(steps))
    steps = raw_input("Steps Backward:")
    counterstep(int(delay) / 1000.0, int(steps))
