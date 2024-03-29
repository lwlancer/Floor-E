import RPi.GPIO as io
from time import sleep

def gpio_setup_DC_motor(pin1, pin2, pin3): #Function expects inputs as pin #s, i.e. '01', '02', etc. 
    is_success = False
    try:
        io.setmode(GPIO.BOARD)
        io.setup(pin1, io.OUT)
        io.setup(pin2, io.OUT)
        io.setup(pin3, io.OUT)
        global pwm 
        pwm= io.PWM(pin3, 100)
        pwm.start(0)
        is_success = True
    except Exception:
        is_success = False
    return is_success

def motor_speed_set(pin1, pin2, pin3, direction, duty): #This function expects the pin names the same way the function above does, the direction as 0 or 1, and duty as a integer % between 0 and 100
    #This function presumes that gpio_Setup_DC_motor has been run first
    if direction:
        io.output(pin1, True)
        io.output(pin2, False)
        pwm.ChangeDutyCycle(duty)
        io.output(pin3, True)
    else:
        io.output(pin1, False)
        io.output(pin2, True)
        pwm.ChangeDutyCycle(duty)
        io.output(pin3, True)

def gpio_cleanup():
    pwm.stop()
    io.cleanup()

def test1():
    try:
        gpio_setup_DC_motor(23,24,25)
        gpio_setup_DC_motor(16,20,21)
        motor_speed_set(23,24,25,0,20)
        motor_speed_set(16,20,21,1,20)
        sleep(5)
        motor_speed_set(23,24,25,0,0)
        motor_speed_set(16,20,21,1,0)
        gpio_cleanup()
        print("test1 success")
    except Exception:
        print("Failure to run test1")

runtest1 = test1()

def test2():
    try:
        gpio_setup_DC_motor(23,24,25)
        gpio_setup_DC_motor(16,20,21)
        motor_speed_set(23,24,25,0,50)
        motor_speed_set(16,20,21,1,50)
        sleep(5)
        motor_speed_set(23,24,25,0,0)
        motor_speed_set(16,20,21,1,0)
        gpio_cleanup()
        print("test2 success")
    except Exception:
        print("Failure to run test2")

runtest2 = test2()

def test3():
    try:
        gpio_setup_DC_motor(23,24,25)
        gpio_setup_DC_motor(16,20,21)
        motor_speed_set(23,24,25,0,75)
        motor_speed_set(16,20,21,1,75)
        sleep(5)
        motor_speed_set(23,24,25,0,0)
        motor_speed_set(16,20,21,1,0)
        gpio_cleanup()
        print("test3 success")
    except Exception:
        print("Failure to run test3")

runtest3 = test3()

def test4():
    try:
        gpio_setup_DC_motor(23,24,25)
        gpio_setup_DC_motor(16,20,21)
        motor_speed_set(23,24,25,0,100)
        motor_speed_set(16,20,21,1,100)
        sleep(5)
        motor_speed_set(23,24,25,0,0)
        motor_speed_set(16,20,21,1,0)
        gpio_cleanup()
        print("test4 success")
    except Exception:
        print("Failure to run test4")

runtest4 = test4()