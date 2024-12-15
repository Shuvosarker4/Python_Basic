class Gadget:
    def __init__(self,name,brand,price):
        self.name = name
        self.brand = brand
        self.price = price

class Phone(Gadget):
    def __init__(self,camera,name,brand,price):
        self.camera = camera
        super().__init__(name,brand,price)

class HeadPhone(Gadget):
    def __init__(self,name,brand,price,manufactured):
        self.manufactured = manufactured
        super().__init__(name,brand,price)

class WaterBottle(Gadget):
    def __init__(self,name,brand,price,weight):
        self.weight = weight
        super().__init__(name,brand,price) # inheritance
        
    def view_details(self):
        print(f"water bottle price is {self.price} and its {self.weight} ml")


bottle = WaterBottle('Mum','Akij',20,250)

bottle.view_details()


