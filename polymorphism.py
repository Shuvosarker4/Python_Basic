# poly ---> many(multiple)
# morph ---> shape
class Animal:
    def __init__(self,name):
        self.name = name
    def makeSound(self):
        print('Animal making sounds')
    
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)
    def makeSound(self):
        print('meewo mewo')

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def makeSound(self):
        print('ghew ghew')

jerry = Dog('Jerri')
jerry.makeSound()
print(issubclass(Cat,Animal))
print(isinstance(jerry,Dog))