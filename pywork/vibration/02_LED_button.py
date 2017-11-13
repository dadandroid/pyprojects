import RPi.GPIO as IO         #we are calling header file which helps us to use GPIOs of PI
import time                           # we are calling for time to provide delays in program



IO.setwarnings(False)          #do not show any warnings
IO.setmode(IO.BCM)         #we are programming the GPIO by BCM pin numbers. (PIN39 as GPIO19)
IO.setup(21,IO.OUT)         # initialize GPIO19 as an output.
IO.setup(20,IO.IN)               #initialize GPIO26 as input
while 1:                                       #execute loop forever
    if(IO.input(20) == False):       #if GPIO26 goes low execute the below statements
        IO.output(21,True)           # turn the LED on (making the voltage level HIGH)
        time.sleep(0.15)                 #sleep for 100m second
        IO.output(21,False)            # turn the LED off (making GPIO19 low)
        #time.sleep(1)                      #sleep for 100m second