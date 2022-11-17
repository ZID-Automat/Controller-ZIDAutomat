from ast import While
import threading
from Borrow.dep.Eject import Eject
from Borrow.dep.LoadBorrowData import LoadBorrowData

from Borrow.dep.QRCodeReader import QRCodeReader
from Event import Event

# Class that Manages everything related to Borrowing of Items
class Borrow (threading.Thread):
    _qRCodeReader:QRCodeReader
    _eject:Eject
    _lData:LoadBorrowData

    _event: Event

    def __init__(self, event):
        threading.Thread.__init__(self)
        self._qRCodeReader = QRCodeReader()
        self._eject = Eject()
        self._lData = LoadBorrowData()

        self._event =event

    def run(self):
        while True:
            qrCode:str = self._qRCodeReader.read()

            if self._lData.ValidateQrCode(qrCode):
                data = self._lData.LoadItemData(qrCode)

                # Ist nur provisorisch, da die LoadITemData Funktion noch nicht implementiert ist, weder am Backend noch im Controller
                self._event.onScannedQrCode(data)

                if self._eject.eject():
                    self._event.onEjectedItem(data)
                    self._lData.InvalidateQrCode(data.ItemId)
                else:
                    print ("handle failed Ejection")
                    self._event.onFailedItemEjection(data)

            else:
                print ("handle not Valid QR Code")
                self._event.onNotValidQrCode(qrCode)




    
