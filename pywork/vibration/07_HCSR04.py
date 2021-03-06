import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 6    #PINTRIG
ECHO = 5    #PPINECHO

print 'Distance Measurement in Progress'

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print "Waiting for Sensor to Settle"
time.sleep(3)

try:
    while(1):
        GPIO.output(TRIG, True)
        time.sleep(0.0001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0:
            pulse_start = time.time()

        while GPIO.input(ECHO)==1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start


        distance = pulse_duration * 17150
        distance = round(distance, 2)

       #print "Distance:", distance, " cm"
        print "Pulse:", pulse_duration*10000
        time.sleep(2)


finally:
    GPIO.cleanup()