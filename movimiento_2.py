# from machine import Pin
# from time import sleep
# 
# IN1 = Pin(0, Pin.OUT)
# IN2 = Pin(1, Pin.OUT)
# IN3 = Pin(2, Pin.OUT)
# IN4 = Pin(3, Pin.OUT)
# 
# def adelante():
#     In1.high()
#     In2.low()
#     In3.high()
#     In4.low()
#     
# def freno():
#     In1.low()
#     In2.high()
#     In3.low()
#     In4.high()
#     
# while True:
#     adelante()
#     print("Adelante")
#     time.Sleep(2)
#     
#     freno()
#     print("Freno")
#     time.Sleep(2)

import time
from machine import Pin

In1=Pin(14,Pin.OUT) 
In2=Pin(15,Pin.OUT)  
#vEN_A=Pin(8,Pin.OUT)

In3=Pin(16,Pin.OUT)  
In4=Pin(17,Pin.OUT)  
# EN_B=Pin(2,Pin.OUT)

#EN_A.high()
#EN_B.high()

def adelante():
    In1.high()
    In2.low()
    In3.high()
    In4.low()
    
def atras():
    In1.low()
    In2.high()
    In3.low()
    In4.high()

def giro_der():
    In1.low()
    In2.low()
    In3.low()
    In4.high()
    
def giro_izq():
    In1.low()
    In2.high()
    In3.low()
    In4.low()

def freno():
    In1.low()
    In2.low()
    In3.low()
    In4.low()
    
while True:
    adelante()
    print("Adelante")
    time.sleep(2)
    
    freno()
    print("Freno")
    time.sleep(2)
    
    atras()
    print("Atrás")   
    time.sleep(2)
    
    freno()
    print("Freno")
    time.sleep(2)