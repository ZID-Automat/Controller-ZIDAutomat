from ast import Num
from xmlrpc.client import boolean

# class reponsible for ejecting an Item
class Eject:
    def __init__(self) -> None:
        pass

# Gibt ein Item aus. Die ItemId sagt, welches Item ausgegeben werden soll. Returned die ItemInstance id des ausgegebenen Items 
# wenn das Ausgeben nicht funktioniert hat, wird eine negative Zahl zurückgegeben
    def eject(self,ItemId:int)-> int:
        return 0