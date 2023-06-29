class Item:
    def __init__(self):
        print("I am created!")
        
    def calcTotalPrice(self, x, y):
        return x * y

item1 = Item()

item1Name = "Phone"
item1Price = 100
item1Quantity = 5

print(item1.calcTotalPrice(item1Price, item1Quantity))

item1 = Item()

item1Name = "Phone"
item1Price = 100
item1Quantity = 5