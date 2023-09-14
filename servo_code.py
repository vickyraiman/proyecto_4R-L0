import machine
import sys

p = machine.Pin(4)
pwm = machine.PWM(machine.Pin(15))

# sys.path.append('C:\Python310\Lib\site-packages')