import serial
from datetime import datetime


ser = serial.Serial('/dev/ttyUSB0',115200)  # open serial port
print(ser.name)         # check which port was really used
value='VNWRG,5,9600*60'
#ser.write("$VNASY,1*XX\r\n".encode()) 

ser.write("$VNWRG,06,0*6C\r\n".encode()) 
ser.write("$VNWRG,75,3,16,08,01*XX\r\n".encode()) 
#ser.write("$VNWRG,05,115200*58\r\n".encode())


ser.close()
