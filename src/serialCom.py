import serial
import time

port = serial.Serial('/dev/ttyUSB0', baudrate = 115200, timeout = 3.0)

a = b"Serial port connected and running"
print a

#Holds the serial loop to send and recieve
#the states of the DE2 module and bomb
def serialCom(self):
	def serialWrite(self, string state):
		port.write(state)

	def serialRead(self):
		rcv = port.read(1)
		print "I got " + str(len(rcv)) + " characters " + rcv 
		return rcv
		time.sleep(0.5)

