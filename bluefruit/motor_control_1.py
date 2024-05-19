import time
import pwmio
import digitalio
import board
from adafruit_circuitplayground import cp
 
print("Code started")
 
# Set DC motors
pwm_left = pwmio.PWMOut(board.A2, frequency=1000)
 
# Motor control pins (in1, in2 for both motors)
in1 = digitalio.DigitalInOut(board.A3)
in2 = digitalio.DigitalInOut(board.A4)
 
# Button pin
button_pin = digitalio.DigitalInOut(board.A1)
button_pin.switch_to_input(pull=digitalio.Pull.DOWN)
 
pwm_left.duty_cycle = 0
 
# Set motor control pins as outputs
in1.direction = digitalio.Direction.OUTPUT
in2.direction = digitalio.Direction.OUTPUT
 
# LED setup and functions
cp.pixels.brightness = 0.1
cp.pixels.fill((0, 0, 0))
cp.pixels.show()
 
def set_led_color(color):
    cp.pixels.fill(color)
    cp.pixels.show()
 
def set_motor_speed(speed):
    pwm_left.duty_cycle = int(speed * 65535)
 
def set_motor_direction(direction):
    in1.value = direction
    in2.value = not direction
 
print("Starting up....")
set_led_color((0, 255, 0))  # Green
set_motor_speed(0.5)
set_motor_direction(True)
time.sleep(1)
set_motor_speed(0)
print(" Startup complete and ready.")
 
while True:
    if cp.button_b:
        print("Button B pressed")
 
        # Ramp up speed over 5 seconds
        print("Ramping up speed...")
        set_led_color((0, 255, 0))  # Green
        for speed in range(0, 101, 2):
            set_motor_speed(speed / 100)
            time.sleep(0.05)
 
        # Run at full speed
        print("Running at full speed...")
        set_motor_speed(1.0)
 
        # Display colors for 60 seconds
        start_time = time.monotonic()
        while time.monotonic() - start_time < 60:
            for color in [(0, 255, 0), (255, 0, 0), (0, 0, 255), (128, 0, 128), (0, 255, 255)]:
                set_led_color(color)
                time.sleep(1)
 
        # Ramp down speed over 5 seconds
        print("Ramping down speed...")
        set_led_color((255, 165, 0))  # Orange
        for speed in range(100, -1, -2):
            set_motor_speed(speed / 100)
            time.sleep(0.05)
 
        set_motor_speed(0)  # Stop the motor
        set_led_color((255, 0, 0))  # Red
        print("Motor stopped after ramping down")