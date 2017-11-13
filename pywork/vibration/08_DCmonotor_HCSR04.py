import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

def readSensor(ECHO, TRIG):
    GPIO.output(TRIG, True)
    time.sleep(0.0001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150
    distance = round(distance, 2)

    return distance



#HC-SR04 PINS
TRIG = 6    #PINTRIG
ECHO = 5    #PPINECHO
#MOTOR PINS
Motor1A = 26
Motor1B = 19
Motor1E = 13


#HC-SR04 SETUP
print 'Distance Measurement in Progress'

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print "Waiting for Sensor to Settle"
time.sleep(3)

#MOTOR SETUP

GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)

GPIO.output(Motor1E, GPIO.LOW)

my_pwm = GPIO.PWM(Motor1A, 500)
my_pwm.start(0)

maxVal = 0
counter = 0

#GPIO.setwarnings(False)

try:

    while(1):

        read = readSensor(ECHO, TRIG)
        print "Distance:", read, " cm"

        #CALIBRATION

        if read > maxVal and (maxVal - read) <50:
            maxVal = read


        OldRange = (maxVal - 0)
        DesiredRange = (100 - 0)
        newRead = (((read - 0) * DesiredRange) / OldRange)

        newRead = int(newRead)
        print newRead


        GPIO.output(Motor1B, GPIO.HIGH)
        GPIO.output(Motor1E, GPIO.HIGH)
        my_pwm.ChangeDutyCycle(newRead)


        counter += 1

        time.sleep(2)

finally:
    my_pwm.stop()
    GPIO.cleanup()

