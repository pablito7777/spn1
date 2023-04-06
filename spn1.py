import serial
import time
from time import gmtime 
#installate pyserial importante || pip3 install pyserial
ser = serial.Serial(
port='/dev/ttyUSB0',   #change with righ port 
baudrate = 9600,
parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE,#_ONE_POINT_FIVE,
bytesize=serial.EIGHTBITS,
timeout=1
)

def z1(ser):
    f='Z'
    line=[]
    c=0
    while c<4:
        f=str(f).encode()
        ser.write(f)
        x = ser.readline()
        line.append(x)
        c=c+1
    s=line[3]
    s=str(s)
    z=s.find("r")
    e=s.find("r?")
    z=z+1
    e=e-1
    print(s[z:e])

def z(ser):
    p=False
    f='Z'
    line=[]
    c=0
    while c<4:
        f=str(f).encode()
        ser.write(f)
        x = ser.readline()
        line.append(x)
        c=c+1
    s=line[3]
    s=str(s)
    z=s.find("r")
    e=s.find("r?")
    z=z+1
    e=e-1   
    st=(s[z:e])
    if '20' in st:
        p=True
    else:
        print(st)
        print('problems... resolving')
        p=False
        f='Z'
        line=[]
        c=0
        while c<4:
            f=str(f).encode()
            ser.write(f)
            x = ser.readline()#.decode()
            line.append(x)
            c=c+1
        s=line[3]
        s=str(s)
        z=s.find("r")
        e=s.find("r?")
        z=z+1
        e=e-1   
        st=(s[z:e])
        if '20' in st:
            p=True      
    if p==True:
        print(st)

def f(ser):
    f='F'
    line=[]
    c=0
    while c<4:
        f=str(f).encode()
        ser.write(f)
        x = ser.readline()#.decode()
        line.append(x)
        c=c+1
    s=line[2]
    s=str(s)
    z=s.find("F")
    e=s.find("r?")
    z=z+1
    e=e-1
    n=(s[z:e]).split(",")
    print('Reports Global:',n[0])
    print('Diffuse:',n[1])
    print('Sunstate:',n[2])
    print('ground reference:',n[3])
    print('Thermophile calibrated readings (s1):',n[4])
    print('Thermophile calibrated readings (s2):',n[5])
    print('Thermophile calibrated readings (s3):',n[6])
    print('Thermophile calibrated readings (s4):',n[7])
    print('Thermophile calibrated readings (s5):',n[8])
    print('Thermophile calibrated readings (s6):',n[9])
    print('Thermophile calibrated readings (s7):',n[10])
    print('Case Temp C°:',n[11])
    print('CPU Temp C°:',n[12])
    
def s(ser):
    f='S'
    line=[]
    c=0
    while c<4:
        f=str(f).encode()
        ser.write(f)
        x = ser.readline()#.decode()
        line.append(x)
        c=c+1
    s=line[2]
    s=str(s)
    #print(s)
    z=s.find("S")
    e=s.find("r?")
    z=z+1
    e=e-1
    f=(s[z:e])
    if '0' or '1' in f:
        f=f.split(",")
        print('Total readings:',f[0])
        print('Diffuse readings:',f[1])
        print('Sunshine presence:',f[2])
    else:
        c=0
        while c<4:
            f=str(f).encode()
            ser.write(f)
            x = ser.readline()#.decode()
            line.append(x)
            c=c+1
        s=line[2]
        s=str(s)
        z=s.find("S")
        e=s.find("r?")
        z=z+1
        e=e-1
        f=(s[z:e])
        if '0' or '1' in f:
            f=f.split(",")
            print('Total readings:',f[0])
            print('Diffuse readings:',f[1])
            print('Sunshine presence :',f[2])
def testmode(ser):
    f='T'
    line=[]
    c=0
    while c<1:
        f=str(f).encode()
        ser.write(f)
        time.sleep(.05)
        x = ser.readline()
        s=str(x)
        s=(s[2:6])
        #line.append(x)
        print(s)
        tt=s
        c=c+1
    return tt
def testmode2(ser):
    f='T'
    t='TEST'
    line=[]
    s='x'
    c=0
    p= False
    while p== False :
        f=str(f).encode()
        ser.write(f)
        time.sleep(.05)
        x = ser.readline()
        print(x)
        s=str(x)
        s=(s[2:5])
        print(s)
        s=str(s)
        c=c+1
        if t == s:
            p=True
            print(x)
        else:
            while c<1:
                f=str(f).encode()
                ser.write(f)
                time.sleep(.05)
                x = ser.readline()
                print(x)
                s=str(x[2:5])
                c=c+1
        time.sleep(.1)
def setData(ser):
    time.sleep(.5)
    named_tuple = time.localtime() # get struct_time
    f = time.strftime("Y%Y/%m/%d", named_tuple)
    print(f)
    c=0
    while c<1:
        f=str(f).encode()
        ser.write(f)
        time.sleep(.05)
        x = ser.readline()#.decode()
        c=c+1
    z(ser)
def setHour(ser):
    time.sleep(.5)
    named_tuple = time.gmtime() # get struct_time
    f = time.strftime("H%H:%M:%S", named_tuple)
    print(f)
    c=0
    while c<1:
        f=str(f).encode()
        ser.write(f)
        time.sleep(.05)
        x = ser.readline()#.decode()
        c=c+1
    z(ser)
def dni(ser):
    named_tuple = time.localtime() # get struct_time
    f = time.strftime("D%H:%M:%S %Y/%m/%d Calc DNI", named_tuple)
    print(f)
    c=0
    while c<2:
        f=str(f).encode()
        ser.write(f)
        time.sleep(.05)
        x = ser.readline()#.decode()
        print(x)
        c=c+1
def cord(ser):
    f='L45.1,009.68,-01:00'  #modifica con +02:00
    c=0
    while c<2:
        f=str(f).encode()
        ser.write(f)
        time.sleep(.05)
        x = ser.readline()#.decode()
        c=c+1
        print(x)
    
def d(ser):
    cord(ser)
    f='D'
    c=0
    line=[]
    while c<4:
        f=str(f).encode()
        ser.write(f)
        time.sleep(.7)
        x = ser.readline()#.decode()
        line.append(x)
        s=str(x)
        c=c+1
    s=line[3]
    s=str(s)
    z=s.find("T,")
    
    e=s.find("r?")
    z=z+1
    e=e-1
    f=(s[z:e])
    if '20'  in f:
        f=f.split(",")
        print('GMT:',f[1])
        print('Total readings :',f[2])
        print('Diffuse readings:',f[3])
        print('Sunshine presence :',f[4])
        print('DNI:',f[5])
def d1(ser):
    cord(ser)
    named_tuple = time.gmtime() # get struct_time
    f = time.strftime("A%Y:%m:%d %H/%M/%S Calc DNI", named_tuple)
    print(f)
    c=0
    line=[]
    while c<4:
        f=str(f).encode()
        ser.write(f)
        time.sleep(.7)
        x = ser.readline()#.decode()
        line.append(x)
        s=str(x)
        c=c+1
    s=line[3]
    s=str(s)
    z=s.find("T,")
    
    e=s.find("r?")
    z=z+1
    e=e-1
    f=(s[z:e])
    if '20'  in f:
        f=f.split(",")
        print('GMT:',f[1])
        print('Total readings :',f[2])
        print('Diffuse readings:',f[3])
        print('Sunshine presence :',f[4])
        print('DNI:',f[5])
def d2(ser):    
    testmode(ser)
    tt=testmode(ser)
    if tt=='TEST':
        time.sleep(.5)
        setData(ser)
        time.sleep(1)
        testmode(ser)
        setHour(ser)
        time.sleep(1)
        d(ser)
        time.sleep(.5)
    else:
        testmode(ser)
        tt=testmode(ser)
        if tt=='TEST':
            time.sleep(.5)
            setData(ser)
            time.sleep(1)
            testmode(ser)
            setHour(ser)
            time.sleep(1)
            d(ser)
            time.sleep(.5)
def testmodex(ser):
    testmode(ser)
    x=False
    y=0
    l='k'
    while x==False :
        testmode(ser)
        tt=testmode(ser)
        print('asdfa',tt)
        if tt == 'TEST':
            x=True
def d4(ser):
    testmodex(ser)
    setHour(ser)
    testmodex(ser)
    setData(ser)
    d()
def d3(ser):
    tt='xx'
    x=False
    y=0
    l='k'
    while x==False :
        testmode(ser)
        tt=testmode(ser)
        if tt == 'TEST':
            x=True
    x= False
    time.sleep(.5)
    setData(ser)
    y=0
    l=str(l).encode()
    ser.write(l)
    time.sleep(.3)
    while x==False :
        testmode(ser)
        tt=testmode(ser)
        if tt == 'TEST':
            x=True
    time.sleep(1)
    setHour(ser)
    time.sleep(.5)
    d(ser)
    
def static(ser):
    while True:
        #ser.close()
        d3(ser)
        time.sleep(20)
    
#static(ser)