#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from grove.gpio import GPIO
from grove.factory import Factory
from grove.button import Button
from grove.grove_ryb_led_button import GroveLedButton


__all__ = ["GroveRelay"]

#------
# Global Variables
#------
button = GroveLedButton(5)
lcd = Factory.getDisplay("JHD1802")
relayPin = 12
totalTime = 5

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

relay = GroveRelay(relayPin)
Grove = GroveRelay


def on_event(index, event, tm):
    #print("event index:{} ".format(index))
    #print("event:{}".format(event))
    #print("pressed:{}".format(event['presesed']))
    if event & Button.EV_SINGLE_CLICK:
        button.led.blink(True)
        Countdown(lcd,relay,totalTime)
        button.led.blink(False)
        InitializeDisplay(lcd,totalTime)
    elif event & Button.EV_LONG_PRESS:
        print('long press') 
        button.led.light(False)

button.on_event = on_event
    

def InitializeDisplay(lcd,totalTime):
    # LCD 16x2 Characters
    lcd.setCursor(0, 0)
    lcd.write("Tokie Blaster M2")
    lcd.setCursor(1, 0)
    lcd.write("Ready   ")
    mins, secs = divmod(totalTime, 60)
    lcd.setCursor(1, -5)
    lcd.write('{:02d}:{:02d}'.format(mins, secs))
    
def Countdown(lcd,relay,totalTime):
    currTime = totalTime
    relay.on()
    lcd.setCursor(1,0)
    lcd.write('Running')
    while currTime:
        try:
            mins, secs = divmod(currTime, 60) 
            timer = '{:02d}:{:02d}'.format(mins, secs)
            lcd.setCursor(1, -5)
            lcd.write(timer) 
            time.sleep(1) 
            currTime -= 1
        except KeyboardInterrupt:
            lcd.setCursor(1, 0)
            relay.off()
            lcd.write("ABORTED!")
            exit(1)
    lcd.setCursor(1,0)
    #mins, secs = divmod(totalTime, 60)
    #lcd.write('DONE {:02d}:{:02d}'.format(mins, secs))
    relay.off()
if __name__ == '__main__':
    #lcd = Factory.getDisplay("JHD1802")
    #relayPin = 12
    #relay = GroveRelay(relayPin)
    #totalTime = 5
    #relayState=0
    InitializeDisplay(lcd,totalTime)
    waiting = True
    while waiting:
        try:
            time.sleep(0.5)
        except KeyboardInterrupt:
            lcd.setCursor(1, 0)
            relay.off()
            lcd.write("ABORTED!")
            exit(1)

    #ledButton = GroveLedButton(5)

    lcd.setCursor(1,0)
    lcd.write('Done   ')
    #main()


