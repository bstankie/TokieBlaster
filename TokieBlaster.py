#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from grove.gpio import GPIO
from grove.factory import Factory

__all__ = ["GroveRelay"]

class GroveRelay(GPIO):
    '''
    Class for Grove - Relay

    Args:
        pin(int): number of digital pin the relay connected.
    '''
    def __init__(self, pin):
        super(GroveRelay, self).__init__(pin, GPIO.OUT)

    def on(self):
        '''
        enable/on the relay
        '''
        self.write(1)

    def off(self):
        '''
        disable/off the relay
        '''
        self.write(0)


Grove = GroveRelay
def InitializeDisplay(lcd,totalTime):
    # LCD 16x2 Characters
    lcd.setCursor(0, 0)
    lcd.write("Tokie Blaster")
    lcd.setCursor(1, -5)
    lcd.write("Ready")
    mins, secs = divmod(totalTime, 60)
    lcd.setCursor(1, 0)

    lcd.write('T:{:02d}:{:02d}'.format(mins, secs)) 

def Countdown(totalTime,lcd):
    currTime = totalTime
    while currTime: 
        mins, secs = divmod(currTime, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer, end="\r") 
        time.sleep(1) 
        currTime -= 1

def main():
    from grove.helper import SlotHelper
    pin = 12
    relay = GroveRelay(pin)

    while True:
        try:
            relay.on()
            time.sleep(1)
            relay.off()
            time.sleep(1)
        except KeyboardInterrupt:
            relay.off()
            print("exit")
            exit(1)            

if __name__ == '__main__':
    lcd = Factory.getDisplay("JHD1802")

    InitializeDisplay(lcd,30)
    main()


