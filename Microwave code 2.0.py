from machine import Pin
import time
from time import sleep
from s2pico_oled import OLED
from machine import Pin, I2C

i2c = I2C(0, sda=Pin(8), scl=Pin(9))
oled = OLED(i2c, Pin(18))

timer = 0


b1 = Pin(7, Pin.IN, Pin.PULL_UP)
b2 = Pin(6, Pin.IN, Pin.PULL_UP)
b3 = Pin(5, Pin.IN, Pin.PULL_UP)
b30 = Pin(4, Pin.IN, Pin.PULL_UP)
door = Pin(35, Pin.IN, Pin.PULL_UP)
microwave = Pin(38, Pin.OUT)


def display_timer(Timer, timer):
    oled.fill(0)
    oled.text(Timer, 0, 0, 1)
    oled.text(str(timer), 0, 20, 1)
    oled.show()
    

while True: 
    if door.value() == 0:
        while True:
            if timer < 0:
                microwave.off()
                oled.fill(0)
                oled.text("Select cook time", 0, 0)
                oled.show()
                print("Select cook time")
                sleep(1)
            if b1.value() == 0:
                timer = 30
            elif b2.value() == 0:
                timer = 60
            elif b3.value() == 0:
                timer = 120
            elif b30.value() == 0:
                timer = timer + 30
            else:
                timer = timer - 1
                sleep(0.55)
            if timer > 0:
                display_timer("Timer:", timer)
                print(timer)
                sleep(0.55)
                microwave.on()
            if timer == 0:
                microwave.off()
                oled.fill(0)
                oled.text("Ready to eat", 0, 0, 1)
                oled.show()
                print("Ready to eat")
                sleep(4)
            if door.value() == 1:
                oled.fill(0)
                oled.text("Door is open", 0, 0, 1)
                oled.show()
                timer = 0
                print("Door is open")
                microwave.off()
                sleep(2)
                
                  
            
                
                