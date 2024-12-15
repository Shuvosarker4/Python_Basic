# encapsulation means hide details
# access modifier like public, protected, private

class Bank:
    def __init__(self,name,branch,deposit):
        self.name = name # public
        self._branch = branch # protected
        self.__balance = deposit # private

    def get_balance(self):
        return self.__balance # get the balance
    
    def deposit(self,amount):
        self.__balance = amount + self.__balance # deposit the balance

Bkash = Bank('Shuvo','Narayanganj',2000)
Bkash.deposit(3000)
print(Bkash.get_balance())