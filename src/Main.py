from io import TextIOWrapper
import os
from DataCollect.DataCollect import DataCollect
import json
from API.Requests import Requests
import Borrow.Borrow as Borrow
# class reponsible for ejecting an Item
from machine import Pin
from time import sleep_ms,sleep_us

class Main():
    wlanInformation = None
    
    backendUrl:str
    backendPassword:str

    def __init__(self) -> None:
        self.loadConfiguration()
        self.setupWlan(self.wlanInformation)

    def start(self):
        print("start Main")
        self._requests = Requests(self.backendUrl)
        print("init Request Manager")
        self._borrowManager = Borrow.BorrowM(self,self._requests)
        print("init Borrow Manager")

        self._dataCollect = DataCollect()
        print("init Data Collect Manager")

      #  self.authenticate()

        print("run Borrow Service")
        self._borrowManager.run()


    def onScannedQrCode(self,itemId,qrCode,itemlocation):
        self._dataCollect.LogScannedQrCode(itemlocation)

    def onFailedItemEjection(self,itemId,qrCode,itemlocation):
        self._dataCollect.LogFailedItemEjection(itemlocation)

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
        print("Configuration loaded")

    def setupWlan(self,wInfo):
        ssid,key = wInfo
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        if not wlan.isconnected():
            print('connect wlan')
            wlan.connect(ssid, key)
            while not wlan.isconnected():
                time.sleep(1)
        print('wlan connected: ' + str(wlan.isconnected()))

    def authenticate(self):
        self._requests.Authenticate(self.backendPassword)

def AusgabePin(pin:int, clock:int, Laenge:int): 

    pin = Pin(pin, Pin.OUT)
    clock = Pin(clock, Pin.IN)
    pin.on()

    print("Waiting for Clock to not be zero")
    while(clock.value() == 0):
        sleep_us(5)
    print("Waiting for Clock to not be one")
    while(clock.value() != 0):
        sleep_us(5)

    sleep_ms(10)
    print("Clock is one, sending signal")


    sleep_ms(Laenge)
    pin.off()
    sleep_ms(10)
    pin.on()
    sleep_ms(1000)

    print("PinSignal was send")
