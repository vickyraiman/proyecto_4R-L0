import time
from machine import Pin

# In1=Pin(6,Pin.OUT) 
# In2=Pin(7,Pin.OUT)  
# EN_A=Pin(8,Pin.OUT)
# 
# In3=Pin(4,Pin.OUT)  
# In4=Pin(3,Pin.OUT)  
# EN_B=Pin(2,Pin.OUT)

# ORIGINAL

In1=Pin(3,Pin.OUT) 
In2=Pin(2,Pin.OUT)  
EN_A=Pin(4,Pin.OUT)

In3=Pin(1,Pin.OUT)  
In4=Pin(0,Pin.OUT)  
EN_B=Pin(5,Pin.OUT)

EN_A.high()
EN_B.high()

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
    time.sleep(1)
    
    atras()
    print("Atrás")   
    time.sleep(2)
    
    freno()
    print("Freno")
    time.sleep(1)
    
    giro_izq()
    print("Izquierda")
    time.sleep(2)
    
    giro_der()
    print("Derecha")
    time.sleep(2)