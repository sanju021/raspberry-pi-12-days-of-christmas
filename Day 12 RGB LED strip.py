#####################################################################################
############################# Button Colour control #################################
# Imports
import time
from machine import Pin
from neopixel import NeoPixel

# Define our button pin
button = Pin(15, Pin.IN, Pin.PULL_DOWN)

# Define the strip pin number (28) and number of LEDs (15)
strip = NeoPixel(Pin(28), 15)

# Colour variables
red = 255,0,0
green = 0,255,0
blue= 0,0,255

# Define colour list
colours = [red, green, blue]

# Create index variable starting at 0
myindex = 0

# Variable with the number of items in our list (3)
# We -1 as the index starts at 0, and we want to use this for the colour list index number (0, 1 or 2)
# This is useful as it means we don't have to count the colours if we add more
indexlength = len(colours) -1

while True: # Run forever
    
    time.sleep(0.4) # Delay
    
    if button() == 1: # If button pressed
        
        # If the index variable is less than or equal to the lengh of the index
        if myindex < indexlength:
            
            # Add +1 to the index variable
            myindex = myindex + 1
        
        # If the index variable is over the index length
        else:
            
            # Set index variable back to 0 (the first item in our list)
            myindex = 0
            
        ## Now this code runs AFTER the if statements...
        
        # Fill the strip with the current list index colour
        strip.fill((colours[myindex]))
            
        # Write the data to the LED strip
        strip.write()



#####################################################################################
######################### Speed controlled Light Chaser #############################
#impots
import time
from machine import Pin, ADC
from neopixel import NeoPixel

# Define the strip pin number (28) and number of LEDs (15)
strip = NeoPixel(Pin(28), 15)

# Set up the potentiometer on ADC pin 26
potentiometer = ADC(Pin(26))

# Colour variables
red = 255,0,0
green = 0,255,0
blue= 0,0,255

# Define colour list
colours = [red, green, blue]

while True:
    for j in colours:
        for i in range(15):
                        # Set the next LED in the range to light with a colour
            strip[i] = (j)
            
            # Read the potentiometer
            # Divide the reading to make it more usable as a time delay
            mydelay = potentiometer.read_u16() / 50000
            
            # Delay - the speed of the chaser
            time.sleep(mydelay)
            
            # Send the data to the strip
            strip.write()
            


#####################################################################################
################################# Light Chaser ######################################
# Imports
#import time
#from machine import Pin
#from neopixel import NeoPixel

# Define the strip pin number (28) and number of LEDs (15)
#strip = NeoPixel(Pin(28), 15)

# Colour variables
#red = 255,0,0
#green = 0,255,0
#blue= 0,0,255

# Define colour list
#colours = [red, green, blue]

#while True: # Run forever

    # Iterate over the colours
#    for j in colours:
        
        # Then iterate over 15 leds
#        for i in range(15):
            
            # Set each LED in the range to red
#            strip[i] = (j)
            
            # Delay - the speed of the chaser
#            time.sleep(0.1)
            
            # Send the data to the strip
#            strip.write()


#####################################################################################
############################### Colour management ###################################
# Imports
#import time
#from machine import Pin
#from neopixel import NeoPixel

# Define the strip pin number (28) and number of LEDs (15)
#strip = NeoPixel(Pin(28), 15)

# Colour variables
#red = 255,0,0
#green = 0,255,0
#blue = 0,0,255
#yellow = 255,255,0
#pink = 255,20,147

# iterate over 15 leds
#for i in range(15):
    
    # Set each LED in the range to pink
#    strip[i] = (pink)

# Send the data to the strip
#strip.write()

#####################################################################################
################################### Single LED ######################################
# Imports
#import time
#from machine import Pin
#from neopixel import NeoPixel

# Define the strip pin number (28) and number of LEDs (15)
#strip = NeoPixel(Pin(28), 15)
        
# Select the first pixel (pixel 0)
# Set the RGB colour ()
#strip[7] = (3,43,97)

# Send the data to the strip
#strip.write()


#####################################################################################
############################ Multiple LED  - Basic ##################################
# Imports
#import time
#from machine import Pin
#from neopixel import NeoPixel

# Define the strip pin number (28) and number of LEDs (15)
#strip = NeoPixel(Pin(28), 15)
        
# Select the first pixel (pixel 0)
# Set the RGB colour (red)
#strip[0] = (255,0,0)
#strip[1] = (255,0,0)
#strip[2] = (255,0,0)
#strip[3] = (255,0,0)
#strip[4] = (255,0,0)

# Send the data to the strip
#strip.write()

#####################################################################################
############################ Multiple LED  - Better #################################
# Imports
#import time
#from machine import Pin
#from neopixel import NeoPixel

# Define the strip pin number (28) and number of LEDs (15)
#strip = NeoPixel(Pin(28), 15)

# iterate over 15 leds
#for i in range(15):
    
    # Set each LED in the range to yellow
#    strip[i] = (255,255,0)

# Send the data to the strip
#strip.write()

#####################################################################################
########################## Multiple LED  - Even better ##############################
# Imports
#import time
#from machine import Pin
#from neopixel import NeoPixel

# Define the strip pin number (28) and number of LEDs (15)
#strip = NeoPixel(Pin(28), 15)

# Fill the strip with turquoise
#strip.fill((255,0,0))

# Send the data to the strip
#strip.write()
