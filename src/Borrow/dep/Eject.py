
# class reponsible for ejecting an Item
from machine import Pin
from time import sleep_ms,sleep_us

ClockPin = 33
Pin1 = 13
Pin2 = 10
Pin3 = 9
Pin4 = 13
Pin5 = 12
Pin6 = 14
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
     

# Gibt ein Item aus. Die ItemId sagt, welches Item ausgegeben werden soll. Returned die ItemInstance id des ausgegebenen Items 
# wenn das Ausgeben nicht funktioniert hat, wird eine negative Zahl zurückgegeben
    def eject(self,Location:str)-> int:
        self.PressCode(Location)
        return True

    def PressCode(self,str:str):
        Button = {
            "A":(0,20),
            "B":(1,20),
            "C":(2,20),
            "D":(3,20),
            "E":(4,20),
            "F":(5,20),
            "G":(0,30),
            "H":(1,30),
            "I":(2,30),
            "J":(3,30)
        }
        for i in str:
            self.PinSignfal2(Button[i][0],Button[i][1])

    #Diese Funktion wurde imprinzip aus dem Original ZID Automat Code übernommen(nur halt in python übersetzt und optimiert)
    #NICHT GETESTET!!!
    def PinSignal(self,Pin:int,Laenge:int):
        PinOb = self.Pins[Pin]
        print("PinOB")
        if self.clock.value() == 0:
            print("val")
            sleep_ms(30)
        abcdefg = self.clock.value() == 1
        while (abcdefg):
            print("val2")
            sleep_us(5) 
            abcdefg = self.clock.value() == 1
        sleep_ms(10)


        sleep_ms(Laenge)
        
        PinOb.on()

        sleep_ms(10)

        PinOb.off()

        for i in range(0,3):
            sleep_ms(60)
            PinOb.on()
            sleep_ms(10)
            PinOb.off()
        sleep_ms(200)      

    def PinSignfal2(self,Pin:int,Laenge:int):
        while(self.clock.value() == 0):
            sleep_us(5)
        while(self.clock.value() == 1):
            sleep_us(5)
        sleep_ms(10)
        sleep_ms(Laenge)
        self.Pins[Pin].value(1)
        sleep_ms(10)
        self.Pins[Pin].value(0)

        sleep_ms(1000)


