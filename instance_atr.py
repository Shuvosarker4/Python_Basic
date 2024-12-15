class Shop:
    def __init__(self,buyer):
        self.buyer = buyer
        self.cart = [] # instance attribute

    def add_to_cart(self,item):
        self.cart.append(item)

shuvo = Shop('Shuvo')
shuvo.add_to_cart('Watch')
shuvo.add_to_cart('Shoes')
shuvo.add_to_cart('Phone')

print(shuvo.cart)

shipu = Shop('shipu')
shipu.add_to_cart('Headphone')
print(shipu.cart)
