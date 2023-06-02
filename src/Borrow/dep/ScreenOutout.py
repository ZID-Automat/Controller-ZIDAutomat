import machine
import time
from Libi.mp_i2c_lcd1602 import LCD1602

class ScreenOutput:

    def __init__(self, Address = 0x27, SCL = 21, SDA = 22):
        self.i2c = machine.I2C(0, scl=machine.Pin(SCL), sda=machine.Pin(SDA))
        self.lcd = LCD1602(self.i2c, Address)


    def print(self, text:str, line:int):
        if(line == 0):
            self.lcd.clear()
        self.lcd.puts(text, 0, line)
        
