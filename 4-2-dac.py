import RPi.GPIO as GPIO
import time

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.cleanup
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)


def dacbin(x):
    return [int(b) for b in bin(x)[2:].zfill(len(dac))]


p = GPIO.PWM(24, 0.5)

try:
    t = int(input("Press T: "))
    t = (t / 256)

    while True:
        i = 0
        for i in range(255):
            GPIO.output(dac, dacbin(i))
            time.sleep(t)

        for i in range(255, 0, -1):
            GPIO.output(dac, dacbin(i))
            time.sleep(t)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup