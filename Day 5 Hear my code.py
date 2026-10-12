# Imports used for all the projects
from machine import Pin, PWM, ADC
import time

#set uo buzzer pin as PWM
buzzer = PWM(Pin(13))

#Create library of tone variables for jingle bells
C = 523
D = 587
E = 659
G = 784

#create volume variable
volume = 10000

#Create a frunction with arguments
def playtone(note, vol, delay1, delay2):
    buzzer.duty_u16(vol)
    buzzer.freq(note)
    time.sleep(delay1)
    buzzer.duty_u16(0)
    time.sleep(delay2)
    
# Play the tune
playtone(E,volume,0.1,0.2)
playtone(E,volume,0.1,0.2)
playtone(E,volume,0.1,0.5) #Longer second delay

playtone(E,volume,0.1,0.2)
playtone(E,volume,0.1,0.2)
playtone(E,volume,0.1,0.5) #Longer second delay

playtone(E,volume,0.1,0.2)
playtone(G,volume,0.1,0.2)
playtone(C,volume,0.1,0.2)
playtone(D,volume,0.1,0.2)
playtone(E,volume,0.1,0.2)

# Duty to 0 to turn the buzzer off
buzzer.duty_u16(0)


#######################################################
#play the tune

# "Jin..."
#buzzer.duty_u16(volume) # Volume up
#buzzer.freq(E) # Set frequency to the E note
#time.sleep(0.1) # Delay
#buzzer.duty_u16(0) # Volume off
#time.sleep(0.2) # Delay

# "...gle"
#buzzer.duty_u16(volume)
#buzzer.freq(E)
#time.sleep(0.1)
#buzzer.duty_u16(0)
#time.sleep(0.2)

# "Bells"
#buzzer.duty_u16(volume)
#buzzer.freq(E)
#time.sleep(0.1)
#buzzer.duty_u16(0)
#time.sleep(0.5) # longer delay

# "Jin..."
#buzzer.duty_u16(volume) # Volume up
#buzzer.freq(E) # Set frequency to the E note
#time.sleep(0.1) # Delay
#buzzer.duty_u16(0) # Volume off
#time.sleep(0.2) # Delay

# "...gle"
#buzzer.duty_u16(volume)
#buzzer.freq(E)
#time.sleep(0.1)
#buzzer.duty_u16(0)
#time.sleep(0.2)

# "Bells"
#buzzer.duty_u16(volume)
#buzzer.freq(E)
#time.sleep(0.1)
#buzzer.duty_u16(0)
#time.sleep(0.5) # longer delay

# "Jin..."
#buzzer.duty_u16(volume) # Volume up
#buzzer.freq(E) # Set frequency to the E note
#time.sleep(0.1) # Delay
#buzzer.duty_u16(0) # Volume off
#time.sleep(0.2) # Delay

# "...gle"
#buzzer.duty_u16(volume)
#buzzer.freq(E)
#time.sleep(0.1)
#buzzer.duty_u16(0)
#time.sleep(0.2)

# "All"
#buzzer.duty_u16(volume)
#buzzer.freq(C)
#time.sleep(0.1)
#buzzer.duty_u16(0)
#time.sleep(0.2)

# "The"
#buzzer.duty_u16(volume)
#buzzer.freq(D)
#time.sleep(0.1)
#buzzer.duty_u16(0)
#time.sleep(0.2)

# "Way"
#buzzer.duty_u16(volume)
#buzzer.freq(E)
#time.sleep(0.1)
#buzzer.duty_u16(0)
#time.sleep(0.2)

# Duty to 0 to turn the buzzer off
#buzzer.duty_u16(0)







#######################################################
###############Changing volume of buzzer###############

# Set up the Buzzer pin as PWM
#potentiometer = ADC(Pin(27))
#buzzer = PWM(Pin(13)) # Set the buzzer to PWM mode
#
#reading = 0
#
#while True:
#    time.sleep(0.01)
#    reading=potentiometer.read_u16()
#    
#    buzzer.freq(500) # set buzzer freq to 500
#    buzzer.duty_u16(reading) # use reading variable as the duty
#    
#    print(reading)
    
 
#######################################################
############## Two toned buzzer #######################
# Set PWM duty
#buzzer.duty_u16(10000)
#
# Set PWM frequency to 1000 for one second
#buzzer.freq(1000)
#time.sleep(1)

# Set PWM frequency to 500 for one second
#buzzer.freq(500)
#time.sleep(1)

# Buzzer off
#buzzer.duty_u16(0)


