import time
from machine import Pin, time_pulse_us

In1=Pin(3,Pin.OUT) 
In2=Pin(2,Pin.OUT)  
EN_A=Pin(4,Pin.OUT)

In3=Pin(1,Pin.OUT)  
In4=Pin(0,Pin.OUT)  
EN_B=Pin(5,Pin.OUT)

trigger = Pin(21, Pin.OUT)
echo = Pin(20, Pin.IN)

EN_A.high()
EN_B.high()

def measure_distance():
    trigger.low()
    sleep_us(2)

    trigger.high()
    sleep_us(10)
    trigger.low()

    pulse_duration = time_pulse_us(echo, Pin.high)

    distance = pulse_duration * 0.0343 / 2
    return distance

def main():
    while True:
        distance = measure_distance()
        print("Distance: {:.2f} cm".format(distance))
       
        sleep(1)

if __name__ == "__main__":
    main()

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
