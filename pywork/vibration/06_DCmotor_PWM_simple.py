import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#enable in pin13
Motor1A = 26
Motor1B = 19
Motor1E = 13

GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)

my_pwm = GPIO.PWM(Motor1A, 500)
my_pwm.start(0)


fast = 100

try:
    while fast != 0:
        GPIO.output(Motor1B, GPIO.HIGH)
        GPIO.output(Motor1E, GPIO.HIGH)
        fast = input("How fast? (20-100)")
        my_pwm.ChangeDutyCycle(fast)



finally:
    my_pwm.stop()
    GPIO.cleanup()

