
# class reponsible for ejecting an Item
from time import sleep_ms,sleep_us
from machine import Pin, ADC
from time import sleep

from machine import Pin, PWM

ClockPin1 = 32
ClockPin2 = 33

Pin1 = 13#F
Pin2 = 12#A und G
Pin3 = 14#B und H
Pin4 = 27#C 
Pin5 = 26#D
Pin6 = 25#E



class Eject:
    def __init__(self) -> None:
        pass

    def eject(self,Location:str)-> int:
        self.PressCode(Location)
        return True

    def PressCode(self,str:str):

        Button = {
            "A":(Pin2,ClockPin1),
            "B":(Pin3,ClockPin1),
            "C":(Pin4,ClockPin1),
            "D":(Pin5,ClockPin1),
            "E":(Pin6,ClockPin1),
            "F":(Pin1,ClockPin2),
            "G":(Pin2,ClockPin2),
            "H":(Pin3,ClockPin2),
        }
        for i in str:
            self.HGFDings(Button[i][0],Button[i][1])

    def AusgabePin(self,pin, clock, Laenge:int): 
        print("Waiting for Clock to not be zero")
        while(clock.read() <= self.low):
            print("clock readas" + str(clock.read()))
            sleep_us(1)
        print("clock read" + str(clock.read()))
        
        print("Waiting for Clock to not be one")
        while(clock.read() >= self.high):
            print("clock readas" + str(clock.read()))

            sleep_us(1)
        print("clock read" + str(clock.read()))
        
        print("Waiting for Clock to not be zero")
        while(clock.read() < self.act):
            print("clock readas" + str(clock.read()))

            sleep_us(1)
        print("clock read" + str(clock.read()))
        
        print("Clock is one, sending signal")

        sleep_ms(Laenge)
        pin.off()
        sleep_ms(10)
        pin.on()
        sleep_ms(1000)

        print("PinSignal was send")

    def HGFDings(self, pin,clock, sl = 0, edge = 0.1, length = 0.1):
        out = Pin(pin, Pin.OUT)
        clockRead = ADC(Pin(clock))
        while True:
            ClockVal = (3.3/4095)* clockRead.read()

            if ClockVal > edge:
                out.on()
            else:
                out.off()
                sleep(length)
                Pin(pin, Pin.IN)
                return

            sleep_ms(sl)


#Eject(1,1,1).test(0,0.1,0.1)



