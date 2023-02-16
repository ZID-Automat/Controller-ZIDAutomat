from machine import UART,Pin,ADC
# class reponsible for scanning the QR Code
class QRCodeReader:

    

    def __init__(self) -> None:
        
        self.uart = UART(1, 9600)
        self.uart.init(9600, bits=8, parity=None, tx=Pin.P1, stop=1)
        

    def read(self)->str:
        return "9a1299ed-70d9-4a07-af47-d5206e6557ab"

    def readTest(self)-> str:
        while True:
            qrCode = self.uart.read()
            print(qrCode)