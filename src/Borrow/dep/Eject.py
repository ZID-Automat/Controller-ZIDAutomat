from ast import Num
from xmlrpc.client import boolean

# class reponsible for ejecting an Item
class Eject:
    def __init__(self) -> None:
        pass

#hier sollte wahrscheinlich statt der ItemId, eine Position oder so sein.
    def eject(self,ItemId:int)-> boolean:
        return True