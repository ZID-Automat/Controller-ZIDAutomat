from io import TextIOWrapper
import json
import network
# class reponsible for ejecting an Item
from machine import Pin
from time import sleep
from Borrow.dep.ScreenOutout import ScreenOutput
import neopixel
class Main123():
    wlanInformation = None
    
    backendUrl:str
    backendPassword:str

    def __init__(self) -> None:

        self.screen = ScreenOutput()
        self.screen.print("Automat Start",0)
        sleep(1)
        self.screen.print("Load Config",0)
        self.loadConfiguration()
        sleep(0.3)
        self.screen.print("Connect Wlan",0)
        self.setupWlan(self.wlanInformation)

    def Eject(self,str):
        self._borrowManager._eject.eject(str)

    def start(self):
        self.screen.print("Setup LED",0)

        self.setupLED(self.ledpin,(self.rot,self.gruen,self.blau),self.lednum)
        self.screen.print("Start MAIN",0)

        from API.Requests import Requestsi
        import Borrow.Borrow as Borrow
        from DataCollect.DataCollect import DataCollect


        
        self.screen.print("initDep",0)

        self._requests = Requestsi(self.backendUrl)
        print("init Request Manager")
        self._borrowManager = Borrow.BorrowM(self,self._requests, (self.pins, self.clockPins, self.QrCodePin),self.screen)
        print("init Borrow Manager")
        self._dataCollect = DataCollect(self._requests)
        print("init Data Collect Manager")


        self.screen.print("authenticate",0)

        self.authenticate()

        self.screen.print("start Borrow",0)
        self.screen.print("Service",1)

        
        while True:
            try:
                self._borrowManager.run()
            except Exception as e:
                print("error")


    def onScannedQrCode(self,itemId,qrCode,itemlocation):
        self._dataCollect.LogScannedQrCode(itemlocation)

    def onNotValidQrCode(self,QrCode):
         self._dataCollect.LogInvaldScannedQrCode(QrCode)

    def onEjectedItem(self,itemId,qrCode,itemlocation):
        self._dataCollect.LogEjecetedItem(itemlocation)

    def loadConfiguration(self):
        f:TextIOWrapper = open('Configuration.json','r')
        data= json.load(f)

        wInform = data['wlan']
        self.wlanInformation = (wInform['ssid'],wInform['password'])

        bInfrom = data['backend']
        self.backendUrl = bInfrom['url']
        self.backendPassword = bInfrom['password']

        

        PinConf = data["PinConfiguration"]
        self.pins = PinConf["ButtonPins"]
        self.clockPins = PinConf["ClockPins"]
        self.QrCodePin = PinConf["QRCodePin"]

        ledConf = data["LED"]
        self.rot = ledConf["cR"]
        self.gruen = ledConf["cG"]
        self.blau = ledConf["cB"]
        self.ledpin = ledConf["pin"]
        self.lednum = ledConf["n"]
        

        print("Configuration loaded")

    def setupWlan(self,wInfo):
        ssid,key = wInfo
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        if not wlan.isconnected():
            print('connect wlan')
            wlan.connect(ssid, key)
            while not wlan.isconnected():
                sleep(1)
        print('wlan connected: ' + str(wlan.isconnected()))

    def setupLED(self,color, pinnum, lednum):
        self.np = neopixel.NeoPixel(Pin(pinnum), lednum)
        for i in range(self.lednum):
            self.np[i] = color
        self.np.write()

    def authenticate(self):

        self._requests.password = self.backendPassword
        self._requests.Authenticate(self.backendPassword)
