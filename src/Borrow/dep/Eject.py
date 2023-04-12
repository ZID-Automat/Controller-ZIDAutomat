
# class reponsible for ejecting an Item
from time import sleep_ms,sleep_us
from machine import Pin, ADC
from time import sleep

from machine import Pin, PWM

ClockPin = 34
Pin1 = 13
Pin2 = 12
Pin3 = 14
Pin4 = 27
Pin5 = 26
class Eject:
    def __init__(self, low, high, act) -> None:
        self.clock = ADC(Pin(ClockPin))
        self.clock.atten(ADC.ATTN_11DB)
        self.Pins = [
            Pin(Pin1,Pin.OUT),
            Pin(Pin2,Pin.OUT),
            Pin(Pin3,Pin.OUT),
            Pin(Pin4,Pin.OUT),
            Pin(Pin5,Pin.OUT) 
        ]
        self.low = low
        self.high = high
        self.act = act

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
            "F":(4,20),
            "G":(0,30),
            "H":(1,30),
            "I":(2,30),
            "J":(3,30)
        }
        for i in str:
            self.AusgabePin(self.Pins[0],self.clock,Button[i][1])

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

    def test(self, sl, edge, length):
        out = Pin(5, Pin.OUT)
        clockRead = ADC(Pin(32))

        ClockOut = PWM(Pin(4), 5000)


        while True:
            val = (3.3/4095)* self.clock.read()
            ClockVal = (3.3/4095)* clockRead.read()

            if ClockVal > edge:
                out.on()
            else:
                out.off()
                sleep(length)
                Pin(5, Pin.IN)
                return

            ClockOut.duty(int((1023/3.3)*ClockVal))

            sleep_ms(sl)


#Eject(1,1,1).test(0,0.1,0.1)



