class Cricketer:
    def __init__(self,name,age,country):
        self.name = name
        self.age = age
        self.country = country
    def __add__(self,other):
        print(self.age + other.age)

    def details(self):
        print(f"{self.name} is a {self.country} cricketer and his age is {self.age}")

sakib = Cricketer('sakib',38,'BD')
sakib.details()

mushi = Cricketer('Mushi',36,'BD')
mushi.__add__(sakib)
