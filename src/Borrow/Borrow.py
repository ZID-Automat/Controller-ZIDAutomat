from Borrow.dep.Eject import Eject
from Borrow.dep.LoadBorrowData import LoadBorrowData
from Borrow.dep.ScreenOutout import ScreenOutput


from Borrow.dep.QRCodeReader import QRCodeReader
from API.Requests import Requestsi

# Class that Manages everything related to Borrowing of Items
class BorrowM:
    _qRCodeReader:QRCodeReader
    _eject:Eject
    _lData:LoadBorrowData

    def __init__(self, event,request:Requestsi, PinConfiguration):
        self._qRCodeReader = QRCodeReader(22)
        self._eject = Eject()
        self._lData = LoadBorrowData(request)
        self.output = ScreenOutput()
        self._event = event

    def run(self):
        self.output.print("Go to www.ZIDAutomat.com to borrow an Item")
        self.output.print("Scan the QR Code here(purple thing)")

        qrCode:str = self._qRCodeReader.read()
        self.output.print("QR Code was scanned")

        valid,itemId = self._lData.ValidateQrCode(qrCode)

        if valid:
            self.output.print("QR is valid")
            itemLocation = self._lData.ItemLocation(itemId)
            self._event.onScannedQrCode(qrCode,valid,itemLocation)

            self.output.print("Now ejecting Item")
            self._lData.InvalidateQrCode(qrCode)	
            self._eject.eject(itemLocation)
            self.output.print("Invalidate QR Code")
            self._event.onEjectedItem(itemId,qrCode,itemLocation)
            self.output.print("Invalidating QR Code")
        else:
            self.output.print("QR Code is not valid try again or contact an admin")
            self._event.onNotValidQrCode(qrCode)




    
