import RPi.GPIO as IO
import time

ledR = 16
ledG = 20

led1 = 5
led2 = 6
led3 = 13
led4 = 26


l = [led1, led2, led3,led4]


IO.setwarnings(False)
IO.setmode(IO.BCM)

t= 2

try:
    while True:

        for led in l:
            IO.setup(led, IO.OUT)
            IO.output(led, 1)

        IO.setup(ledR, IO.OUT)
        IO.output(ledR, 1)
        time.sleep(t)
        IO.output(ledR, 0)

        for led in l:
            IO.output(led, 0)

        IO.setup(ledG, IO.OUT)
        IO.output(ledG, 1)
        time.sleep(t)
        IO.output(ledG, 0)

finally:
    IO.cleanup()
