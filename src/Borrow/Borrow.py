from Borrow.dep.Eject import Eject
from Borrow.dep.LoadBorrowData import LoadBorrowData

from Borrow.dep.QRCodeReader import QRCodeReader

from API.Requests import Requests
# Class that Manages everything related to Borrowing of Items
class BorrowM:
    _qRCodeReader:QRCodeReader
    _eject:Eject
    _lData:LoadBorrowData

    def __init__(self, event,request:Requests ):
        self._qRCodeReader = QRCodeReader()
        self._eject = Eject()
        self._lData = LoadBorrowData(request)

        self._event = event

    def run(self):
        #loop forever aber noch nicht, weil dings
        for i in range(0,1):
            qrCode:str = self._qRCodeReader.read()
            print("QR Code was read" + qrCode)

            valid,itemId = self._lData.ValidateQrCode(qrCode)

            if valid:
                print ("QRCode is Valid")
                itemLocation = self._lData.ItemLocation(itemId)
                print(itemLocation)
                self._event.onScannedQrCode(qrCode,valid,itemLocation)
                print("Item Data was loaded")

                print("start Ejecting Item")
                          
                if self._eject.eject(itemLocation)      :
                    self._event.onEjectedItem(itemId,qrCode,itemLocation)
                    print("Item was ejected")
                    self._lData.InvalidateQrCode(qrCode)	
                    print("QR Code was invalidated")
                else:
                    print ("handle failed Ejection")
                    self._event.onFailedItemEjection(itemId,qrCode,itemLocation)

            else:
                print ("handle not Valid QR Code")
                self._event.onNotValidQrCode(qrCode)




    
