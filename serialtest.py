import serial

port = serial.Serial('/dev/ttyUSB0', baudrate = 115200, timeout = 3.0)

a = b"hello world"
print a

port.write("Say something:")
while True:
	rcv = port.read(10)
	print "I got " + str(len(rcv)) + " characters " + rcv 
	port.write("You sent:"   + rcv)
