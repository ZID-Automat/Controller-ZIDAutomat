from enum import Enum
import json 
import requests
import json 

class EndPoints(Enum):
    Test:"test"

AuthEndpoint = "Auth"


class Requests:
    jwt:str
    baseUrl:str

    def __init__(self,baseUrl):
        self.baseUrl = baseUrl
        pass

    def Request(self,EndPoint):
        if(self.jwt == None):
            print ("Cant send Request to"+ EndPoint+" ,not Authenticated")
        else:
            url = self.baseUrl+EndPoint
            headers = {'Authentification': 'Bearer: '+self.jwt}
            return json.loads(requests.get(url,headers=headers))

    def Authenticate(self,password:str):
        url = self.baseUrl+AuthEndpoint
        self.jwt = requests.get(url)
