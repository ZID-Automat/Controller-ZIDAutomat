from Borrow.dep.Eject import Eject
from Borrow.dep.LoadBorrowData import LoadBorrowData

from time import sleep

from Borrow.dep.QRCodeReader import QRCodeReader
from API.Requests import Requestsi

# Class that Manages everything related to Borrowing of Items
class BorrowM:
    _qRCodeReader:QRCodeReader
    _eject:Eject
    _lData:LoadBorrowData

    def __init__(self, event,request:Requestsi, PinConfiguration, screen):
        self._qRCodeReader = QRCodeReader(18)
        self._eject = Eject()
        self._lData = LoadBorrowData(request)
        self.output = screen
        self._event = event

    def run(self):
        self.output.print("www.ZIDAutoat.at",0)
        self.output.print("Scan QRCode",1)

        qrCode:str = self._qRCodeReader.read()
        self.output.print("QR Code",0)
        self.output.print("Scanned",1)


        valid,itemId, message, message2 = self._lData.ValidateQrCode(qrCode)

        if valid:
            self.output.print("QRCode",0)
            self.output.print("is Valid",1)
            sleep(0.2)
            itemLocation = self._lData.ItemLocation(itemId)
            #self._event.onScannedQrCode(qrCode,valid,itemLocation)

            self.output.print("Invalidateing",0)
            self.output.print("QrCode",1)
            self._lData.InvalidateQrCode(qrCode)	
            self.output.print("Start Eject",0)
            self.output.print("",1)
            self._eject.eject(itemLocation)
            sleep(5)

           # self._event.onEjectedItem(itemId,qrCode,itemLocation)

            self.output.print("Item Ejected",0)
            self.output.print("",1)
            sleep(0.4)
        else:
            self.output.print("QRCode not valid",0)
            sleep(1)
            self.output.print(message,0)
            self.output.print(message2,1)
            sleep(2)


           # self._event.onNotValidQrCode(qrCode)




    
