#on RaspberryPi need to run with "Sudo python mcp3008lib.py"

from gpiozero import MCP3008
import time
import datetime

#ts = time.time()

i-0
while i<10 :
  rPot1 = MCP3008(0)
  rPot2 = MCP3008(1)

  ct =dattime.datetime,now()   # Current Time

  print ct
  print "  Left : ", rPot1.value , "  #  Right : ", rPot2.value
  time.sleep(1)  # Sleep for 1 second
  i=i+1
