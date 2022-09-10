import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)

p = GPIO.PWM(22, 1000)
p.start(0)

try:
    while True:
        p.ChangeDutyCycle(int(input()))


finally:
    GPIO.output(22, 0)
    GPIO.cleanup()