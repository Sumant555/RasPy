#on RaspberryPi need to run with "Sudo python mcp3008lib.py"

from gpiozero import MCP3008
import time
import datetime
from gpiozero import LED

#ts = time.time()
trl = 0   #Initiate Transition Right to Left Flag
led = LED(11) # Pin 11 on RaspberryPi selected [GPIO-0]

# To Read sensor value from ADC MCP3008
def readSensor(pinN):
  sensoRead = MCP3008(pinN)

# Output on display
def DispalyOut(lVal, rVal):
  print ct
  print ("  Left : ", rVal.value , "  #  Right : ", lVal.value)
  if tChange = True:
    print ("Changeover observed at " + ct)

#Toggle LED
def tgLED(n):
  if led[n].on() == True
    led[n].off()
  else
    led[n].on()
  
i=0
while i<10 :
  rPot1 = MCP3008(0)
  rPot2 = MCP3008(1)

  tempCheck()
  
  ct =dattime.datetime,now()   # Current Time

  DisplayOut(rPot1, rPot2)
  
  time.sleep(1)  # Sleep for 1 second
  i += 1

#To detect the change over of temperature
def tempCheck():
  if trl == 0:
    if rPot1 > rPot2
      tChange = True
      trl = 1
      DisplayOut()
    else
      tChange = False
    elf trl == 1
      if rPot2 > rPot1
        tchange = True
        trl = 0
        DisplayOut()
      else
        tChange = False
