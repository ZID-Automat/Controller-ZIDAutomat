class ItemDetailed:
    def __init__(self,itemDet:dict) -> None:
        self.id = itemDet['id']
        self.name = itemDet['name']
        self.subName = itemDet['subName']
        self.description = itemDet['description']
        self.image = itemDet['image']
        self.available = itemDet['available']
        self.price = itemDet['price']
        self.categorie = itemDet['categorie']
    id:int 
    name:str 
    subName:str 
    description:str 
    image:str 
    available :int
    price :int
    categorie:str 