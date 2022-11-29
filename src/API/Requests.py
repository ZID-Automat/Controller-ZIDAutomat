from enum import Enum
import json 
import requests
import json 
class Requests:
    jwt:str
    baseUrl:str

    verifySSL = False

    def __init__(self,baseUrl):
        self.baseUrl = baseUrl

    def RequestGet(self,EndPoint, params =  {}):
        header=self.getHeader()
        url = self.baseUrl+EndPoint
        return requests.get(url,headers=header,params=params, verify=self.verifySSL).json()
    
    def RequestPost(self,EndPoint , params =  {}):
        header=self.getHeader()
        url = self.baseUrl+EndPoint
        return requests.post(url,headers=header,json =params, verify=self.verifySSL).json()
    
    def RequestPut(self,EndPoint , params =  {}):
        header={
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiQ29udHJvbGxlciIsIm5iZiI6MTY2OTcyNzc2OCwiZXhwIjoxNjY5NzYzNzY4LCJpYXQiOjE2Njk3Mjc3Njh9.DK3UyQ6U3eI6qaFr3_3xS1Xnyjp439oxGHCxyygoqAo',
        'Content-Type': 'application/json'
        }
        payload = json.dumps(params)
        url = self.baseUrl+EndPoint
        response = requests.request("PUT", url, headers=header, data=payload,verify=self.verifySSL)
        return response

    def getHeader(self):
        return  {'Authorization': 'Bearer '+self.jwt,  'Content-type':'application/json', 'Accept':'application/json'}

    def Authenticate(self,password:str):
        url = self.baseUrl+"Authentification/AutomatLogin"
        self.jwt = requests.post(url, json ={"ControllerPassword":password},verify=self.verifySSL).text
