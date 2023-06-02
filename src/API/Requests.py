import json 
import ujson
import urequests
import gc;
import utime
import ubinascii
class Requestsi:
    jwt:str = ""
    baseUrl:str
    password = ""
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
        if(self.jwt == "" or self.check_jwt_expiration(self.jwt)):
            self.Authenticate(self.password)
        gc.collect()
        return  {'Authorization': 'Bearer '+self.jwt,  'Content-type':'application/json', 'Accept':'application/json'}

    def Authenticate(self,password:str):    
        print("Authenticating")
        urli = self.baseUrl+"Authentification/AutomatLogin"
        bo =  ujson.dumps({"controllerPassword":password})
        self.jwt = urequests.post(url= urli,headers = {'content-type': 'application/json'} ,data = bo).text
        print("sucessful Authenticated, jwt loaded")

    def check_jwt_expiration(self,token):
        # Das JWT dekodieren und den Payload erhalten
        header, payload, signature = token.split('.')
        decoded_payload = ujson.loads(ubinascii.a2b_base64(payload + '==='))

        # Ablaufzeit (exp) im Payload überprüfen
        expiration_time = decoded_payload.get('exp', 0)

        # Aktuelle Zeit in Unix-Zeitstempel umwandeln
        current_time = utime.time()

        # Überprüfen, ob das JWT in den nächsten 30 Minuten abläuft
        if expiration_time > current_time and expiration_time <= current_time + 1800:
            return True
        else:
            return False


   