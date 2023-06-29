class Item:
    def __init__(self, name: str, price: float, quantity=0):
        
        # We can create further restraints on the value created by instance by using the assert function
        assert price >= 0, f"Your number {price} is not greater than 0"
        assert quantity >= 0, f"Your number {quantity} is not greater than 0"


        self.name = name
        self.price = price
        self.quantity = quantity
    
    
    def calcTotalPrice(self):
        return self.price * self.quantity

item1 = Item("Phone", 100, -5)

item2 = Item("Laptop", 1000, 3)


print(item1.calcTotalPrice())
