
# class reponsible for ejecting an Item
from machine import Pin
from time import sleep_ms,sleep_us

ClockPin = 12
Pin1 = 2
Pin2 = 3
Pin3 = 6
Pin4 = 7
Pin5 = 8
Pin6 = 9
class Eject:
    def __init__(self) -> None:
        print("init Eject")
        self.Pins = []
        pins = [Pin1,Pin2,Pin3,Pin4,Pin5,Pin6]
        for i in pins:
            self.Pins.append(Pin(i,Pin.OUT))

        self.clock = Pin(ClockPin,Pin.IN)
        print("Eject init done")

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
            self.PinSignal(Button[i][0],Button[i][1])

    #Diese Funktion wurde imprinzip aus dem Original ZID Automat Code übernommen(nur halt in python übersetzt und optimiert)
    #NICHT GETESTET!!!
    def PinSignal(self,Pin:int,Laenge:int):
        PinOb = self.Pins[Pin]

        if self.clock.value() == 0:
            sleep_ms(30)
        while (self.clock.value() == 1):
            sleep_us(5) 
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