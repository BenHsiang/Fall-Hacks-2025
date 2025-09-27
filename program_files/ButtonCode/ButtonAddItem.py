import ClassCart
#a general code for what happens when you submit aka you press ok after choosing how much you want
def ButtonPressAddItems(ItemName, amount,Cartt):
    Cartt.addDishToCart(ItemName, amount)
    #then a popup on the screen saying order added
