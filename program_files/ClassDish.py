import math
class Dish:
    #might have alot of errors thus far 
    price = 0.0  
    ordered =0
    Name="Im a dish"
    Resturant="IDk man"

    def __init__(self, price,ordered, Name,Resturant):
        self.price=price
        self.ordered=ordered
        self.Name=Name
        self.Resturant=Resturant
    
    def add_item(self, amount):
        self.ordered+= amount
        #then it will run the cart one in which it adds the item to a list if not already on it
    
    def remove_item(self, amount):
        if(self.ordered>=amount):
            self.ordered-= amount
