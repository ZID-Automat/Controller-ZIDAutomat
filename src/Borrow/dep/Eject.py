
# class reponsible for ejecting an Item
from machine import Pin
from time import sleep_ms,sleep_us

ClockPin = 18
Pin1 = 13
Pin2 = 12
Pin3 = 14
Pin4 = 27
Pin5 = 26
Pin6 = 25
class Eject:
    def __init__(self) -> None:
        self.clock = Pin(ClockPin,Pin.IN)
        self.Pins = [
            Pin(Pin1,Pin.OUT),
            Pin(Pin2,Pin.OUT),
            Pin(Pin3,Pin.OUT),
            Pin(Pin4,Pin.OUT),
            Pin(Pin5,Pin.OUT),
            Pin(Pin6,Pin.OUT) 
        ]
     

    def eject(self,Location:str)-> int:
        self.PressCode(Location)
        return True

    def PressCode(self,str:str):
        Button = {
            "A":(1,20),
            "B":(2,20),
            "C":(3,20),
            "D":(4,20),
            "E":(5,20),
            "F":(0,20),
            "G":(1,30),
            "H":(2,30),
            "I":(3,30),
            "J":(0,30)
        }
        for i in str:
            self.PinSignfal2(Button[i][0],Button[i][1])

    def PinSignfal2(self,Pin:int, Laenge:int):
        print("Waiting for Clock to not be zero")
        if(self.clock.value() == 0):
            sleep_ms(30)
        print("Waiting for Clock to not be one")
        while(self.clock.value() == 1):
            sleep_us(1)
        print("Clock is zero, sending signal")
        sleep_ms(Laenge)
        self.Pins[Pin].on()
        sleep_ms(100)
        self.Pins[Pin].off()
        print("PinSignal was send")
        sleep_ms(1000)



  