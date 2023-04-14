
# class reponsible for ejecting an Item
from time import sleep_ms,sleep_us
from machine import Pin, ADC
from time import sleep

from machine import Pin, PWM

#ClockPin1 = 32
#ClockPin2 = 33

#Pin1 = 13#F
#Pin2 = 12#A und G
#Pin3 = 14#B und H
#Pin4 = 27#C 
#Pin5 = 26#D
#Pin6 = 25#E



class Eject:
    def __init__(self, Pins, ClockPins) -> None:
        self.Pin1 = Pins[0]
        self.Pin2 = Pins[1]
        self.Pin3 = Pins[2]
        self.Pin4 = Pins[3]
        self.Pin5 = Pins[4]
        self.Pin6 = Pins[5]
        self.ClockPin1 = ClockPins[0]
        self.ClockPin2 = ClockPins[1]
        pass

    def eject(self,Location:str)-> int:
        for i in Location:
            self.PressCode(i)
        return True

    def PressCode(self,stri:str):
        Button = {
            "A":(self.Pin2,self.ClockPin1),
            "B":(self.Pin3,self.ClockPin1),
            "C":(self.Pin4,self.ClockPin1),
            "D":(self.Pin5,self.ClockPin1),
            "E":(self.Pin6,self.ClockPin1),
            "F":(self.Pin1,self.ClockPin2),
            "G":(self.Pin2,self.ClockPin2),
            "H":(self.Pin3,self.ClockPin2),
        }
        self.HGFDings(Button[stri][0],Button[stri][1])

    def HGFDings(self, pin,clock, sl = 0, edge = 0.1, length = 0.1):
        out = Pin(pin, Pin.OUT)
        clockRead = ADC(Pin(clock))
        while True:
            ClockVal = (3.3/4095)*clockRead.read()

            if ClockVal > edge:
                out.on()
            else:
                out.off()
                sleep(length)
                Pin(pin, Pin.IN)
                return

            sleep_ms(sl)





