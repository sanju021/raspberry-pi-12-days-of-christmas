# Imports
from machine import ADC, Pin, PWM
import time

# Set up the potentiometer on ADC pin 27
potentiometer = ADC(Pin(27))

#set up LED with Pulse Width Modulation
led = PWM(Pin(18))

#set PWM frequency
led.freq(1000)

#create variable for reading
reading = 0

# Set up the LED pins
#red = Pin(18, Pin.OUT)
#amber = Pin(19, Pin.OUT)
#green = Pin(20, Pin.OUT)


while True: # Run forever
    
    reading = potentiometer.read_u16() # Read the potentiometer value and set this as our reading variable value
    
    print(reading) # Print the reading
    
    # Set the LED PWM duty cycle to the potentiometer reading value
    # The duty cycle tells the LED for how long it should be on each time
    led.duty_u16(reading)
    
    time.sleep(0.0001) # A really short delay
    
    
    
    
################################################################################
    
#    time.sleep(0.1) # short delay
#    
#    if reading <= 20000: # If reading is less than or equal to 20000
#         
#        red.value(1) # Red ON
#        amber.value(0)
#        green.value(0)
#        
#    elif 20000 < reading < 40000: # If reading is between 20000 and 40000
#    #
#        red.value(0) 
#        amber.value(1) # Amber ON
#        green.value(0)
#        
#    elif reading >= 40000: # If reading is greater than or equal to 40000
#            
#        red.value(0) 
#        amber.value(0)
#        green.value(1) # Green ON
