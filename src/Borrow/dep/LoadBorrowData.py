
# Just another abstraction for the API
from typing import Tuple
from API.Requests import Requests
from API.dep.ItemDetailed import ItemDetailed

class LoadBorrowData:
    _api: Requests

    def __init__(self,api:Requests) -> None:
        self._api = api

    #Returns if there is an valid QRCode
    def ValidateQrCode(self,qrCode:str)-> Tuple[bool,int]:
        re = self._api.RequestPost("CBorrow/ValidateQrCode",{"QRCode":qrCode})
        return (re['valid'],re['itemId'])

    #Loads all the relevant Item Data (ItemDetailed)
    def LoadItemData(self,id)->ItemDetailed:
        return ItemDetailed(self._api.RequestGet("CBorrow/LoadItemData",{"item":id}))
    
    #Invalidates a Qr Code, so that it can't be used twice
    def InvalidateQrCode(self,qrCode, itemdetId)->None:
       self._api.RequestPut("CBorrow/InvalidateQrCode",{"qrCode":qrCode,"itemInstanceId":itemdetId})

