
# Just another abstraction for the API
from typing import Tuple
from API.Requests import Requests


class LoadBorrowData:
    _api: Requests

    def __init__(self,api:Requests) -> None:
        self._api = api

    #Returns if there is an valid QRCode
    def ValidateQrCode(self,qrCode:str)-> Tuple[bool,int]:
        re = self._api.RequestPost("CBorrow/ValidateQrCode",{"QRCode":qrCode})
        return (re['valid'],re['itemId'])

    #Loads all the relevant Item Data (ItemDetailed)
    def LoadItemData(self,id):
        re = self._api.RequestGet("CBorrow/LoadItemData",{"item":id})
        return re
    
    #Invalidates a Qr Code, so that it can't be used twice
    def InvalidateQrCode(self,qrCode, itemdetId):
        re = self._api.RequestPut("CBorrow/InvalidateQrCode",{"QRCode":qrCode,"itemdetId":itemdetId})
        return re

