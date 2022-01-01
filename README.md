# FOF-RPi-Server-Example
The few simple files that help make the 'Foundations of Fabrication' project/lesson a fun experience!


## hide-and-seek.py
The 'hide and seek' file will blink an LED so users can go physically find the server in the room. (It is, perhaps, the nerdiest hide and seek.)

Requires 
* tqdm package: https://pypi.org/project/tqdm/
* LED soldered on to GPIO 23 & GND

## oled-stats.py
The PIOLED display can show a few lines of messages on the Raspberry Pi.
It will require a few dependancies, and an edit to /etc/rc.local for auto-start
Instructions: https://learn.adafruit.com/adafruit-pioled-128x32-mini-oled-for-raspberry-pi/usage

## was-here.txt
This file is a simple register for all those who have "visited" the Raspberry Pi by logging in via SSH.