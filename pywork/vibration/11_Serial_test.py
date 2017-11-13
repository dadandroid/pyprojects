import serial
ser = serial.Serial('/dev/ttyACM0', 9600)


while True:
    val = str(input("number of blinks"))
    ser.write(val)
    msg = ser.read(ser.inWaiting())
    print msg
