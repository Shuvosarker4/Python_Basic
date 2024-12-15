class Shopping:
    def __init__(self,name):
        self.name = name
        self.cart = []

    def add_to_cart(self,itemName,quantity,price):
        self.itemName = itemName
        self.quantity = quantity
        self.price = price
        product ={'itemName':itemName,'quantity':quantity,'price':price}
        self.cart.append(product)

    def checkout(self,amount):
        total = 0
        for item in self.cart:
            total = total + (item['quantity']) * (item['price'])
            print(f"Total Price:{total} tk")
        if (amount < total):
            print(f"please provide {total - amount} tk more")
        else:
            print(f"You give {amount} tk and Your extra tk is {amount - total}")

jamuna = Shopping('Shuvo')
jamuna.add_to_cart('Watch',2,500)

jamuna.checkout(1020)

boshun = Shopping('Shipu')
boshun.add_to_cart('Shoes',2,1000)

boshun.checkout(3000)