from machine import Pin
from utime import sleep
green=Pin(0,Pin.OUT)
red=Pin(1,Pin.OUT)
amber=Pin(2,Pin.OUT)
while True:
    green.on()
    sleep(3)
    green.off()
    amber.on()
    sleep(3)
    amber.off()
    red.on()
    sleep(3)
    amber.on()
    sleep(3)
    red.off()
    amber.off()
        
        
    
    