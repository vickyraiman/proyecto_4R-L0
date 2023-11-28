import time
from mpu6050 import mpu6050
import RPi.GPIO as GPIO

# pines del modelo de figma
SDA_PIN = 2
SCL_PIN = 3
MOTOR_PIN_1A = 17  
MOTOR_PIN_1B = 27  
MOTOR_PIN_2A = 19  
MOTOR_PIN_2B = 26 

sensor = mpu6050(address=0x68, bus=1, scl=SCL_PIN, sda=SDA_PIN)

GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_PIN_1A, GPIO.OUT)
GPIO.setup(MOTOR_PIN_1B, GPIO.OUT)
GPIO.setup(MOTOR_PIN_2A, GPIO.OUT)
GPIO.setup(MOTOR_PIN_2B, GPIO.OUT)

def controlar_motores():
    lectura = sensor.get_accel_data()
    eje_y = lectura['y']

  if eje_y > 0:
        GPIO.output(MOTOR_PIN_1A, GPIO.HIGH)
        GPIO.output(MOTOR_PIN_1B, GPIO.LOW)
    else:
        GPIO.output(MOTOR_PIN_1A, GPIO.LOW)
        GPIO.output(MOTOR_PIN_1B, GPIO.HIGH)

    if eje_y > 0:
        GPIO.output(MOTOR_PIN_2A, GPIO.HIGH)
        GPIO.output(MOTOR_PIN_2B, GPIO.LOW)
    else:
        GPIO.output(MOTOR_PIN_2A, GPIO.LOW)
        GPIO.output(MOTOR_PIN_2B, GPIO.HIGH)

try:
    while True:
        controlar_motores()
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
