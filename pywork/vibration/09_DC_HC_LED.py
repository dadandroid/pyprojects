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

def remap(OldValue, OldMax, OldMin,NewMax, NewMin):
    return (((OldValue - OldMin) * (NewMax - NewMin)) / (OldMax - OldMin)) + NewMin

#HC-SR04 PINS
TRIG = 6    #PINTRIG
ECHO = 5    #PPINECHO
#MOTOR PINS
Motor1A = 26
Motor1B = 19
Motor1E = 13

#LED PIN
LEDpin = 21

#LED SETUP
GPIO.setup(LEDpin, GPIO.OUT)
ledPWM = GPIO.PWM(LEDpin, 100)
ledPWM.start(0)

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

motorPWM = GPIO.PWM(Motor1A, 500)
motorPWM.start(0)


#CALIBRATION VARIABLES
maxDist = 60
sensorMaxVal = 0
counter = 0
maxLED = 100
maxMotor = 100
#GPIO.setwarnings(False)

try:

    while(1):

        sensorRead = readSensor(ECHO, TRIG)
        print "Distance:", sensorRead, " cm"

        #CALIBRATION

        if sensorRead > sensorMaxVal and (sensorMaxVal - sensorRead) < 50 and sensorRead < maxDist:
            sensorMaxVal = sensorRead
        print sensorMaxVal

        #remmap values

        remappedLED = remap(sensorRead, sensorMaxVal , 0, maxLED, 0)
        remappedMotor = int(remap(sensorRead, sensorMaxVal, 0, maxMotor, 0))

        # LED ACTUATION
        if remappedLED <= maxLED:
            ledPWM.ChangeDutyCycle(remappedLED)


        #MOTOR ACTUATION
        """
        GPIO.output(Motor1B, GPIO.HIGH)
        GPIO.output(Motor1E, GPIO.HIGH)
        motorPWM.ChangeDutyCycle(remappedMotor)
        """


        counter += 1
        time.sleep(.2)

finally:
    ledPWM.stop()
    motorPWM.stop()
    GPIO.cleanup()

