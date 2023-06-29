class Item:
    def __init__(self, name: str, price: float, quantity=0): # you declare types for your arguments to ensure correct objects goes into the variable,  
  
        self.name = name
        self.price = price
        self.quantity = quantity
    
    
    def calcTotalPrice(self):
        return self.price * self.quantity

item1 = Item("Phone", 100, 5)

item2 = Item("Laptop", 1000, 3)


print(item1.calcTotalPrice())
