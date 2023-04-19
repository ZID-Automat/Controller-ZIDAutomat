from machine import UART

# class reponsible for scanning the QR Code
class QRCodeReader:

    def __init__(self, pin):
        self.pin = pin

    def read(self)->str:
        #initates an Serial Connection over the Second Serial Bus
        uart1 = UART(2, baudrate=9600, rx=self.pin)
        uart1.init(9600, bits=8, parity=None, stop=1)
        while True:
            textB = uart1.read()
            if textB is not None:
                print("read: "+textB.decode('UTF-8'))
                return textB.decode('UTF-8')[:-2]
