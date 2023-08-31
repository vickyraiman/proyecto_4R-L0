from machine import Pin, time_pulse_us
from time import sleep_us, sleep


# Initialize trigger and echo pins
trigger = Pin(21, Pin.OUT)
echo = Pin(20, Pin.IN)


def measure_distance():
    # Ensure trigger is low initially
    trigger.low()
    sleep_us(2)


    # Send a 10 microsecond pulse to the trigger pin
    trigger.high()
    sleep_us(10)
    trigger.low()


    # Measure the duration of the echo pulse (in microseconds)
    pulse_duration = time_pulse_us(echo, Pin.high)


    # Calculate the distance (in centimeters) using the speed of sound (343 m/s)
    distance = pulse_duration * 0.0343 / 2
    return distance


def main():
    while True:
        # Measure the distance and print the value in centimeters
        distance = measure_distance()
        print("Distance: {:.2f} cm".format(distance))
       
        # Wait for 1 second before taking the next measurement
        sleep(1)


if __name__ == "__main__":
    main()




