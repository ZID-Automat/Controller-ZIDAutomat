
# class reponsible for ejecting an Item
from machine import Pin
from time import sleep_ms,sleep_us

ClockPin = 18
Pin1 = 13
Pin2 = 12
Pin3 = 14
Pin4 = 27
Pin5 = 26
class Eject:
    def __init__(self) -> None:
        self.clock = Pin(ClockPin,Pin.IN)
        self.Pins = [
            Pin(Pin1,Pin.OUT),
            Pin(Pin2,Pin.OUT),
            Pin(Pin3,Pin.OUT),
            Pin(Pin4,Pin.OUT),
            Pin(Pin5,Pin.OUT),
        ]
        for p in self.Pins:
            p.on()
     

    def eject(self,Location:str)-> int:
        self.PressCode(Location)
        return True

    def PressCode(self,str:str):
        Button = {
            "A":(0,20),
            "B":(1,20),
            "D":(2,20),
            "E":(3,20),
            "F":(4,30),
            "G":(0,30),
            "H":(1,30),
            "I":(2,30),
            "J":(3,30)
        }
        for i in str:
            self.PinSignfal2(Button[i][0],self.clock,Button[i][1])

    def AusgabePin(self,pin, clock, Laenge:int): 
        print("Waiting for Clock to not be zero")
        while(clock.value() == 0):
            sleep_us(5)
        print("Waiting for Clock to not be one")
        while(clock.value() != 0):
            sleep_us(5)

        sleep_ms(10)
        print("Clock is one, sending signal")


        sleep_ms(Laenge)
        pin.off()
        sleep_ms(10)
        pin.on()
        sleep_ms(1000)

        print("PinSignal was send")





  