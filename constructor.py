class Phone:
    manufactured = 'china'
    def __init__(self,model,name,price,color):
        self.model = model
        self.name = name
        self.price = price
        self.color = color

my_phone = Phone('S series','samsung',12000,'blue')
# print(my_phone.manufactured)
# print(my_phone.model)

# print(my_phone.color)