import json

from io import TextIOWrapper
import os
from typing import Dict, Tuple
from API.Requests import Requests

from Event import Event

from Borrow.Borrow import Borrow
from DataCollect.DataCollect import DataCollect

IsAutomat = False
if IsAutomat :
    import network, time



class Main():
    wlanInformation :Tuple[str,str]
    
    backendUrl:str
    backendPassword:str

    _requests:Requests
    _borrowManager:Borrow
    _dataCollect:DataCollect

    def __init__(self) -> None:
        self.loadConfiguration()
        if IsAutomat:
            self.setupWlan(self.wlanInformation)

    def start(self):
        self._requests = Requests(self.backendUrl)

        self._dataCollect = DataCollect()
        self._borrowManager = Borrow(self,self._requests)
        
        self.authenticate()

        self._borrowManager.run()

    def onScannedQrCode(self,data):
        self._dataCollect.LogScannedQrCode(data)

    def onFailedItemEjection(self,data):
        self._dataCollect.LogFailedItemEjection(data)

    def onNotValidQrCode(self,QrCode):
         self._dataCollect.LogInvaldScannedQrCode(QrCode)

    def onEjectedItem(self,data):
        self._dataCollect.LogEjecetedItem(data)

    def loadConfiguration(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))

        f:TextIOWrapper = open(dir_path+'/Configuration.json','r')
        data:dict[str,str]= json.load(f)

        wInform:Dict[str,str] = data['wlan']
        self.wlanInformation = (wInform['ssid'],wInform['password'])

        bInfrom:Dict[str,str] = data['backend']
        self.backendUrl = bInfrom['url']
        self.backendPassword = bInfrom['password']

    def setupWlan(self,wInfo:Tuple[str,str]):
        ssid,key = wInfo
        #Damit kommen wir inder Schule aber nicht weit, da die Anmeldung da über die Accounts funktioniert.
        wlan = Network.WLAN(Network.STA_IF)
        wlan.active(True)
        if not wlan.isconnected():
            print('connect wlan')
            wlan.connect(ssid, key)
            while not wlan.isconnected():
                pass
        print('wlan connected')

    def authenticate(self):
        self._requests.Authenticate(self.backendPassword)

if __name__ == "__main__":
    Main().start()
