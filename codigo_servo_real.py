import RPi.GPIO as GPIO
import time

pin = 19

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

servo = GPIO.PWM(pin, 50)
servo.start(7.5)

try:
    while True:
        servo.ChangeDutyCycle(5)
        time.sleep(1)
        
        servo.ChangeDutyCycle(10)
        time.sleep(1)
        
except KeyboardInterrupt:
    servo.stop()
    GPIO.cleanup()
    print("Todo limpio")