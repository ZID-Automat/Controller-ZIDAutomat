
# Just another abstraction for the API
from API.Requests import Requests
from API.dep.ItemDetailed import ItemDetailed

# class resposible or leading the data from the API
class LoadBorrowData:
    _api: Requests

    def __init__(self,api:Requests) -> None:
        self._api = api

    #Returns if there is an valid QRCode Bool int Tuple
    def ValidateQrCode(self,qrCode:str):
        re = self._api.RequestPost("CBorrow/ValidateQrCode",{"QRCode":qrCode})
        return (re['valid'],re['itemId'])

    #Loads all the relevant Item Data (ItemDetailed)
    def LoadItemData(self,id)->ItemDetailed:
        return ItemDetailed(self._api.RequestGet("CBorrow/LoadItemData/"+str(id)))
    
    #Invalidates a Qr Code, so that it can't be used twice
    def InvalidateQrCode(self,qrCode)->None:
       self._api.RequestPatch("CBorrow/InvalidateQrCode",{"qrCode":qrCode})

    #Returns the Location of an Item
    def ItemLocation(self,itemId)->str:
        return self._api.RequestGet("CBorrow/ItemLocation/"+str(itemId))['location']

