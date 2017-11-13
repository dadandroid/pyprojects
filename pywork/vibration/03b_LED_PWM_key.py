import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

LEDpin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDpin, GPIO.OUT)

p = GPIO.PWM(LEDpin, 200)  # GPIO19 as PWM output, with 100Hz frequency
p.start(0)


intensity = 100

#GPIO.setwarnings(False)
try:
    while intensity != 0:
        intensity = input("How much intensity? (20-100)")
        p.ChangeDutyCycle(intensity)



finally:
    p.stop()
    GPIO.cleanup()