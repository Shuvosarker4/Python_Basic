class Shopping:
    cart = []
    def __init__(self,name,location):
        self.name = name
        self.location = location
    @staticmethod
    def multiple(a,b):
        print (a * b)
    @staticmethod
    def watch(item):
        print(f"{item} ta dekhi")

bashundara = Shopping('bashundare','Dhaka')
bashundara.multiple(10,20)
bashundara.watch('shoes')