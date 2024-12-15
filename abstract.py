from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def eat(self):
        print('Animal need food')

class Monkey(Animal):
    def __init__(self,name):
        self.name = name
        super().__init__()
    
    def eat(self):
        print('I eat banana')

# layka = Animal()
# layka.eat()

naika = Monkey('Lucky')
naika.eat()