import serial
ser = serial.Serial('/dev/ttyACM0', 9600)


while True:
    val = str(input("position 0 to 6: "))
    ser.write(val)
    msg = ser.read(ser.inWaiting())
    print msg
