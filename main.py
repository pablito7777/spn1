import serial 
import spn1
import time
#installate pyserial importante || pip3 install pyserial
ser = serial.Serial(
port='/dev/ttyUSB0',   #change with righ port importat a lotssss
baudrate = 9600,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,#_ONE_POINT_FIVE,
bytesize=serial.EIGHTBITS,
timeout=1
)
ch='g'
print('THE POSSIBILE CHOISES ARE: ')
print('S: Total & Diffuse reading , 0 or 1 for sunshine presence')
print('F: Reports Global,Diffuse,Sunstate,Ground Geference,7xThermophile,Case Temp,CPU Temp')
print('T: Enable TESTMODE')
print('Z: Displays date and date')
print('Y: Set the local date ' )
print('H: Set the local hours')
print('D: To calculate DNI')
print('EXIT: to exit')
print('ALL COMMAND NEED TO BE SEND IN CAPITAL LETTERS')
print('NOW IF YOU WANT I CAN SET TIME,DATE,LATITUDE,LONGITUDE & TIME ZONE')
sc='P'
sc=input(' YES on NO to set values: ')
if(ser.isOpen()==False):
    ser.open()
if sc=='YES' or 'yes':
    spn1.testmode(ser)
    time.sleep(.3)
    spn1.setData(ser)
    spn1.setHour(ser)
    spn1.cord(ser)
    print('if dete or time is NOT correct please input again H to correct time o D to correct date')
while True:
    ch='g'
    ch=input('Enter your choice: ',)
    if ch == 'S' or 's':
        spn1.s(ser)
    elif ch == 'F' or 'f':
        spn1.f(ser)
    elif ch == 'T' or 't':
        spn1.testmode(ser)
    elif ch == 'Z' or 'z':
        spn1.z(ser)
    elif ch == 'Y' or 'y':
        spn1.setData(ser)
    elif ch == 'H' or 'h':
        spn1.setHour(ser)
    elif ch == 'D'or 'd':
        spn1.d3(ser)
    elif ch =='C' or 'c ' :
        spn1.cord(ser)
    elif ch == 'EXIT':
        break