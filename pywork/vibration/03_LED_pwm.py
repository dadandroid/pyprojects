import RPi.GPIO as GPIO  # calling header file which helps us use GPIOs of PI

import time  # calling time to provide delays in program

LEDpin = 21

GPIO.setwarnings(False)  # do not show any warnings

GPIO.setmode(GPIO.BCM)  # we are programming the GPIO by BCM pin numbers. (PIN35 as GPIO19)

GPIO.setup(LEDpin, GPIO.OUT)  # initialize GPIO19 as an output.

p = GPIO.PWM(LEDpin, 100)  # GPIO19 as PWM output, with 100Hz frequency
p.start(0)  # generate PWM signal with 0% duty cycle

maxV = 100

try:
    while 1:  # execute loop forever

        for x in range(maxV):  # execute loop for 50 times, x being incremented from 0 to 49.
            p.ChangeDutyCycle(x)  # change duty cycle for varying the brightness of LED.
            time.sleep(0.5)  # sleep for 100m second

        for x in range(maxV):  # execute loop for 50 times, x being incremented from 0 to 49.
            p.ChangeDutyCycle(maxV - x)  # change duty cycle for changing the brightness of LED.
            time.sleep(0.5)  # sleep for 100m second

finally:
    GPIO.cleanup()