import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


def frequentVal(lst):
    return max(set(lst), key=lst.count)


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


def sensorCalibration():
    print "Calibrating sensor max distance. Please point ultrasonic sensor to the furthest target and stand by..."
    valList = []
    for i in range(10):
        val = readSensor(ECHO, TRIG)
        valList.append(val)
        time.sleep(.5)
    mode = frequentVal(valList)
    print "Calibration Done. Max distance is ", mode
    return mode


def remap(OldValue, OldMax, OldMin, NewMax, NewMin):
    return (((OldValue - OldMin) * (NewMax - NewMin)) / (OldMax - OldMin)) + NewMin

GPIO.setwarnings(False)

# HC-SR04 PINS
TRIG = 24  # PINTRIG
ECHO = 25 # PPINECHO


# MOTOR PINS
Motor1A = 26
Motor1B = 19
Motor1E = 13

# LED PIN
LEDpin = 5

# LED SETUP
GPIO.setup(LEDpin, GPIO.OUT)
ledPWM = GPIO.PWM(LEDpin, 100)
ledPWM.start(0)

# HC-SR04 SETUP
print 'Initizalizing sensor...'
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
time.sleep(1)

# MOTOR SETUP

GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)

GPIO.output(Motor1E, GPIO.LOW)

motorPWM = GPIO.PWM(Motor1A, 500)
motorPWM.start(0)

# CALIBRATION VARIABLES
maxDist = 60
sensorMaxVal = 0
counter = 0
maxLED = 100
maxMotor = 100

lastVal = 0

try:

    # SENSOR CALIBRATION
    sensorMaxVal = sensorCalibration()

    while (1):

        sensorRead = readSensor(ECHO, TRIG)
        print "Distance:", sensorRead, " cm"


        """
        if sensorRead > sensorMaxVal and (sensorMaxVal - sensorRead) < 50 and sensorRead < maxDist:
            sensorMaxVal = sensorRead
        print sensorMaxVal
        """


        # remmap values
        remappedLED = int(remap(sensorRead, sensorMaxVal, 0, maxLED, 5))
        remappedMotor = int(remap(sensorRead, sensorMaxVal, 0, maxMotor, 0))

        # LED ACTUATION
        if remappedLED <= maxLED and abs((100-remappedLED) - lastVal) > 10:
            ledPWM.ChangeDutyCycle(100-remappedLED)
            lastVal = 100-remappedLED
        else:
            ledPWM.ChangeDutyCycle(lastVal)




        """
        # MOTOR ACTUATION
        if remappedMotor <= maxMotor:
            GPIO.output(Motor1B, GPIO.HIGH)
            GPIO.output(Motor1E, GPIO.HIGH)
            motorPWM.ChangeDutyCycle(remappedMotor)

        """

        counter +=1

        #more sleeping time = more precision
        time.sleep(.5)

finally:
    ledPWM.stop()
    motorPWM.stop()
    GPIO.cleanup()

