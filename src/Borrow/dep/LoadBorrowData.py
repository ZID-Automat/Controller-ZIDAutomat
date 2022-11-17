# Just another abstraction for the API
class LoadBorrowData:

    #Returns if there is an valid QRCode
    def ValidateQrCode(self,qrCode:str)-> bool:
        return False;

    #Loads all the relevant Item Data
    def LoadItemData(self,qrCode):
        pass
    
    #Invalidates a Qr Code, so that it can't be used twice
    def InvalidateQrCode(self,Itemid):
        return False;
