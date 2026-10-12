# Imports
from machine import Pin
import time

# Set up tilt sensor pin
tilt = Pin(26, Pin.IN, Pin.PULL_DOWN)

# Set up a counter variable at zero
tiltcount = 0

# Create a state variable at zero
state = 0

while True: # Run forever
    
    time.sleep(0.1) # Short delay
        
    if state == 0 and tilt.value() == 1: # If state is 0 and our pin is HIGH
                    
         tiltcount = tiltcount + 1 # Add +1 to tiltcount
                  
         state = 1 # Change state to 1
            
         print("tilts =",tiltcount) # Print our new tiltcount
            
    if state == 1 and tilt.value() == 0: # If state is 1 and our pin is LOW
                            
        state = 0 # Change the state to 0



################################################################################################
##################################### TILT ALARM ###############################################
# Imports
#from machine import Pin, PWM
#import time
#
# Set up tilt sensor pin
#tilt = Pin(26, Pin.IN, Pin.PULL_DOWN)
#
# Set up the Buzzer pin as PWM
#buzzer = PWM(Pin(13)) # Set the buzzer to PWM mode
#
# Set PWM frequency to 1000
#buzzer.freq(1000)
#
#while True: # Run forever
#    
#    time.sleep(0.01) # Short delay
#    
#    if tilt.value() == 1: # If sensor is HIGH
#        
#        print("***TILT DETECTED***") # Print a string
#        
#        buzzer.duty_u16(10000) # Set duty (volume up)
#        
#        time.sleep(0.2) # Short delay
#        
#        buzzer.duty_u16(0) # Duty to zero (volume off)

