# Class that manages all the Data Collection(Historie...) stuff
class DataCollect:
    def __init__(self,requests) -> None:
        self._api = requests

    def LogScannedQrCode(self,QrCode):
        self._api.RequestPost("CLogging/LogEjectedItem",{"guid":QrCode},False)


    def LogInvaldScannedQrCode(self,QrCode):
        self._api.RequestPost("CLogging/LogInvaldScannedQrCode",{"guid":QrCode},False)


    def LogEjecetedItem(self,QrCode):
        self._api.RequestPost("CLogging/LogEjectedItem",{"guid":QrCode},False)

    def test(self):
        self.LogScannedQrCode("test")
        self.LogInvaldScannedQrCode("C10E100C-FF68-40BE-988E-92487BF9EB63")
        self.LogEjecetedItem("C10E100C-FF68-40BE-988E-92487BF9EB63")

