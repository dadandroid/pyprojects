import RPi.GPIO as IO
import time

IO.setwarnings(False)
IO.setmode(IO.BCM)


led1 = 5
led2 = 6
led3 = 13
led4 = 19

l = [led1, led2, led3,led4]

for led in l:
    IO.setup(led, IO.OUT)


t= 2

try:
    while True:

        for led in l:
            IO.output(led, 1)
        time.sleep(t)
        for led in l:
            IO.output(led, 0)
        time.sleep(t)

finally:
    IO.cleanup()
