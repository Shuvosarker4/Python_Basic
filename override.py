class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print('I eat Poalw') # actual eat method

class Cricketer(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def eat(self):
        print('Vegetable') # we over ride eat method

sakib = Cricketer('sakiiib',38)
sakib.eat()