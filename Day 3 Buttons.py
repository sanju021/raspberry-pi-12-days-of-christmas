#import
from machine import Pin
import time

#set up button name and pin number
#pin in put and pull down
button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

#set up LED anme and GPIO pin numbers
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

while True:
    time.sleep(0.2)
    
    if button1.value() == 1:
        print("button 1 pressed")
        red.toggle()




#########################################################
#########Two button make green flash on and off##########
#
#    if button1.value() == 1 or button2.value() == 1:
#        print("button 1 or 2 are pressed")
#        green.value(1)
#        time.sleep(2)
#        green.value(0)
    
   
   
#########################################################
##########Each button corresponds to a colour############
#   
#    if button1.value() == 1:
#        print("Button 1 is pressed")
#        green.value(1)
#        
#    elif button2.value() == 1:
#        print("Button 2 is pressed")
#        amber.value(1)
#    
#    elif button3.value() == 1:
#        print("Button 3 is pressed")
#        red.value(1)
#    else:
#        red.value(0)
#       green.value(0)
#        amber.value(0)
