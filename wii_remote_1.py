#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|-|S|p|y|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# wii_remote_1.py
# Connect a Nintendo Wii Remote via Bluetooth
# and  read the button states in Python.
#
# Project URL :
# http://www.raspberrypi-spy.co.uk/?p=1101
#
# Author : Matt Hawkins
# Date   : 30/01/2013

# -----------------------
# Import required Python libraries
# -----------------------
import cwiid
import time
#import RPi.GPIO as io

#Neutral flat table acc = [135, 136, 161]
#on left side = [104, 136, 135] on right [162 .. ..





button_delay = 0.05 #was 0.1

print ('Press 1 + 2 on your Wii Remote now ...')
time.sleep(1)

# Connect to the Wii Remote. If it times out
# then quit.
try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print( "Error opening wiimote connection")
  quit()

print ('Wii Remote connected...\n')
print ('Press some buttons!\n')
print ('Press PLUS and MINUS together to disconnect and quit.\n')

#set Wiimote to report button presses and accelerometer state 
wii.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC 
 
#turn on led to show connected 
wii.led = 1
 
while True:
	
  buttons = wii.state['buttons']
  time.sleep(0.05)

  # If Plus and Minus buttons pressed
  # together then rumble and quit.
  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):  
    print ('\nClosing connection ...')
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    exit(wii)  

  #wii.rumble = (wii.state['acc'][0] < 134)
  if (buttons & cwiid.BTN_A):
    print (wii.state['acc'])
  #prev = wii.state['acc'][0] 
  ind = 50
  left = 0
  right = 0
  neutral = 0
  if (wii.state['acc'][0] < 100 or wii.state['acc'][0] > 160):
    #print('Entered while')
    while (ind > 0):
      while(ind > 20):
        if(wii.state['acc'][0] < 100):
          right += 1
          #prev = 'RIGHT'
        #elif(wii.state['acc'][0] >160):
          #left += 1
        else:
          left += 1#neutral +=1
        ind-=1
      #print('right = '+str(right))
      #print('left = '+str(left))
      if(right > (left + 2)):
        while (neutral < 1000):
          j = wii.state['acc'][0]
          if( j > 100 and j < 160):
            neutral +=1
      elif(left > (right+2)): 
        while (neutral < 1000):
          j = wii.state['acc'][0]
          if( j > 100 and j < 160):
            neutral +=1
      ind -= 1
      #time.sleep(0.01)
  if(right > left):  
    print("Swing Right!")
  elif(left > right):
    print("Swing Left!")

  time.sleep(0.2)
  if wii.state['buttons'] & cwiid.BTN_A:
      wii.led = (wii.state['led'] + 1 % 16)
  
  # Check if other buttons are pressed by
  # doing a bitwise AND of the buttons number
  # and the predefined constant for that button.
  if (buttons & cwiid.BTN_LEFT):
    print ('Left pressed')
    time.sleep(button_delay)         
    #io.output(2, True)

  if(buttons & cwiid.BTN_RIGHT):
    print ('Right pressed')
    time.sleep(button_delay)          
    #io.output(3, True)

  if (buttons & cwiid.BTN_UP):
    print ('Up pressed')        
    time.sleep(button_delay)          
    #io.output(4, True)
    
  if (buttons & cwiid.BTN_DOWN):
    print ('Down pressed')      
    time.sleep(button_delay)  
    #io.output(17, True)
    
  if (buttons & cwiid.BTN_1):
    print ('Button 1 pressed')
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_2):
    print ('Button 2 pressed')
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_A):
   # print ('Button A pressed')
    #time.sleep(button_delay)          
    pass
      #io.output(i, False)    

  if (buttons & cwiid.BTN_B):
    print ('Button B pressed')
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_HOME):
    print ('Home Button pressed')
    time.sleep(button_delay)           
    
  if (buttons & cwiid.BTN_MINUS):
    print ('Minus Button pressed')
    time.sleep(button_delay)   
    
  if (buttons & cwiid.BTN_PLUS):
    print( 'Plus Button pressed')
    time.sleep(button_delay)


	
