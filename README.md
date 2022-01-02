# FOF-RPi-Server-Example
The few simple files that help make the 'Foundations of Fabrication' project/lesson a fun experience!\

You can play hide-and-seek with the Raspberry Pi, provided that it is connected correctly and in the space.\ 
Just type in: [change the IP address to whatever the instructor tells you]\
```r
ssh pi@192.168.1.220
```
You may be prompted to 'add this to your known hosts' and, provided that you did this right, that is fine to allow - type: 'yes'\
\
Then you will need to enter the password for the user 'pi' on the Raspberry Pi computer. Your instructor should have told you this.\
Finally, type the following command, and then start searching the space:\
```r
python hide-and-seek.py
```
\

## hide-and-seek.py
The 'hide and seek' file will blink an LED so users can go physically find the server in the room. (It is, perhaps, the nerdiest hide and seek.)\

Requires 
* tqdm package: https://pypi.org/project/tqdm/
* LED soldered on to GPIO 23 & GND

## stats.py
The PIOLED display can show a few lines of messages on the Raspberry Pi.\
It will require a few dependancies, and an edit to /etc/rc.local for auto-start.\
Instructions: https://learn.adafruit.com/adafruit-pioled-128x32-mini-oled-for-raspberry-pi/usage

## washere.txt
This file is a simple register for all those who have "visited" the Raspberry Pi by logging in via SSH.