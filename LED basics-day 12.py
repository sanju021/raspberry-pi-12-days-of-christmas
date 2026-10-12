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
import time
from machine import Pin
from neopixel import NeoPixel

# Define the strip pin number (28) and number of LEDs (15)
strip = NeoPixel(Pin(28), 15)

# Fill the strip with turquoise
strip.fill((255,0,0))

# Send the data to the strip
strip.write()