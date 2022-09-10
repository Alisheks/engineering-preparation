import RPi.GPIO as GPIO
import time

dac=[26, 19, 13, 6, 5, 11, 9, 10]
c=[0]*len(dac)
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def dacbin(x):
    return [int(b) for b in bin(x)[2:].zfill(len(dac))]

try:
    while True:
        num = str(input("Enter a num in range(0,255): "))
        if num.isdigit():
            num = int(num)
            if num < 0:
                print("num<0, try again ")
            elif num > 255:
                print("num>255, try again ")
            else:
                c = dacbin(num)
                GPIO.output(dac, c)
                print ("{:.3f}".format(3.3*(0.5*c[0]+0.25*c[1]+0.125*c[2])))
        else:
            if num == "q":
                break
            else:
                print ("Enter a positive integer! ")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup
    print("GPIO cleanup completed ")