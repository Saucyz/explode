import serial
import time

#Holds the serial loop to send and recieve
#the states of the DE2 module and bomb
class serialCom:
	def __init__(self):
		self.port = serial.Serial('/dev/ttyUSB0', baudrate = 115200, timeout = 0.01)
		a = b"Serial port connected and running"
		print a

	def serialWrite(self, state):
		self.port.write(state)

	def serialRead(self):
		rcv = self.port.read(1)
		#time.sleep(0.01)
		#print "I got " + str(len(rcv)) + " characters " + rcv 
		return rcv

