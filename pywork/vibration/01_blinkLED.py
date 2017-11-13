import RPi.GPIO as IO
import time

LEDpin = 22
                             #calling for time to provide delays in program
IO.setmode(IO.BCM)       #programming the GPIO by BOARD pin numbers, GPIO21 is called as PIN40
IO.setup(LEDpin ,IO.OUT)          #initialize digital pin40 as an output.
IO.output(LEDpin , 1)                      #turn the LED on (making the voltage level HIGH)
time.sleep(1)                         #sleep for a second
IO.output(LEDpin , 0)                          # turn the LED off (making all the output pins LOW) (IO.cleanup)
time.sleep(1)                        #sleep for a second

#loop is executed second time
IO.setmode(IO.BOARD)
IO.setup(LEDpin ,IO.OUT)
IO.output(LEDpin ,1)
time.sleep(1)
IO.cleanup()
time.sleep(1)

#loop is executed third time
IO.setmode(IO.BOARD)
IO.setup(LEDpin ,IO.OUT)
IO.output(LEDpin ,1)
time.sleep(1)
IO.cleanup()
time.sleep(1)