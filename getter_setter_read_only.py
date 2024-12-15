class User:
    def __init__(self,name,age,money):
        self._name = name
        self._age = age
        self.__money = money
    # its read only because its have no setter
    @property 
    def get_age(self):
        return self._age
    
    # getter
    @property
    def get_salary(self):
        return self.__money
    
    # setter
    @get_salary.setter # you can assign value of the new salary
    def set_money(self,amount):
        self.__money += amount

shuvo = User('shuvo',22,5000)
shuvo.set_money = 2000
shuvo.__money = 20 # This will create a new attribute instead of modifying __money
print(shuvo.get_salary) # --> 7000
print(shuvo.__money) # --> 20
# convert call a func to use dot notation for access because we use @property