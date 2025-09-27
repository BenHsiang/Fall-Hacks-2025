import ClassCart
def ButtonRemoveItem(ItemName,amount,Cartt):
    if(amount<=ItemName.ordered):
        Cartt.Remove_Item(ItemName,amount)
        #popup saying item removed
    else:
        print("Hell no")
        #popup saying failed to remove item as amount removing is too big.

