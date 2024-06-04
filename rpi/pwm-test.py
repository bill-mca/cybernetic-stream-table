import RPi.GPIO as IO          
import time                            

IO.setwarnings(False)          

IO.setmode (IO.BCM)

# initialize GPIO18 as an output.
IO.setup(18,IO.OUT)           

#GPIO18 as PWM output, with 100Hz frequency
p = IO.PWM(18,100) 

#generate PWM signal with 0% duty cycle
p.start(0)

while 1:
    for x in range (90):
        p.ChangeDutyCycle(x) 
        time.sleep(0.1)
    time.sleep(5)
    for x in range (90):

        p.ChangeDutyCycle(90-x) 
        print(90-x)
        time.sleep(0.5) 
    time.sleep(1)
