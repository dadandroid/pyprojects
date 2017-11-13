import serial


ser = "searching"
search = True

while (search):

    for i in range(0, 20):
        try:
            sub = '/dev/ttyACM' + str(i)
            ser = serial.Serial(sub, 9600)
        except:
            print "no"

        finally:
            print ser
            search = False


while True:

    #val comes from other raspi
    val = str(input("position 1 to 6 , speed 7 to 9"))
    ser.write(val) #write to arduino serial port
