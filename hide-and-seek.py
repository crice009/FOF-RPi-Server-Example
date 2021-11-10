#hide-and-seek.py
#requires LED soldered on to GPIO 23 & GND

from gpiozero import LED
from time import sleep
from tqdm import tqdm #for loading bar as timer

led = LED(23) #the LED is soldered in to place here...
countdown = 120 #seconds of countdown
blink_pause = 0.1 #delay for the blink

print "There is a small Raspberry Pi hidden in the space."
print "You have", countdown, "seconds to find the tiny computer."
print "It is blinking BLUE. Start looking..."

for t in tqdm(range(int(countdown)), desc="Seconds Used"): #makes the loading bar
    for x in range(int(1/(blink_pause * 2))):
        led.on()
        sleep(blink_pause)
        led.off()
        sleep(blink_pause)

print "Sorry, try again... OR You found it!"
print "======>> Now, hide the RPi in a new location."
print "Don't be too sneaky, and make sure there is enough power."