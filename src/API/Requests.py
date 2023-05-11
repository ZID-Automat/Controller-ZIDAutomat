import json 
import ujson
import urequests
import gc;

class Requestsi:
    jwt:str = ""
    baseUrl:str

    verifySSL = False

    def __init__(self,baseUrl):
        self.baseUrl = baseUrl

    def RequestGet(self,EndPoint):
        header=self.getHeader()
        url = self.baseUrl+EndPoint
        return urequests.get(url,headers=header).json()
    
    def RequestPost(self,EndPoint , params =  {}, ReturnsJson = True):
        header=self.getHeader()
        url = self.baseUrl+EndPoint
        resp =  urequests.post(url,headers=header,json =params)
        if ReturnsJson:
           return resp.json()
    
    def RequestPatch(self,EndPoint , params =  {}):
        header=self.getHeader()
        payload = json.dumps(params)
        url = self.baseUrl+EndPoint
        response = urequests.request("PATCH", url, headers=header, data=payload)
        return response

    def getHeader(self):
        gc.collect()
        return  {'Authorization': 'Bearer '+self.jwt,  'Content-type':'application/json', 'Accept':'application/json'}

    def Authenticate(self,password:str):
        print("Authenticating")
        urli = self.baseUrl+"Authentification/AutomatLogin"
        bo =  ujson.dumps({"controllerPassword":password})
        self.jwt = urequests.post(url= urli,headers = {'content-type': 'application/json'} ,data = bo).text
        print("sucessful Authenticated, jwt loaded")

   