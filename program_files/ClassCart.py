class Cart:
    UserId=0
    Name="Bob"
    ItemsOrdered= list() # list to hold the dishes 
    sum=0

    def __init__(self,UserId,name):
        self.Name=name
        self.UserId=UserId
    def get_sum(self):
        return self.sum
    def getUserId(self):
        return self.UserId
    def getName(self):
        return self.Name
    def CalculateSum(self):
        self.sum=0
        for x in self.ItemsOrdered:
            self.sum+=(x.price *x.ordered)
    
    def addDishToCart(self,Dish,amount):
        length=len(self.ItemsOrdered)
        added=False
        if(length>0):
            for x in self.ItemsOrdered:
                if(x.Name== Dish.Name & x.price == Dish.price & x.ordered== Dish.ordered):
                    x.addItem(x,amount)
                    added=True
                    break
            if(added==False):
                Dish.addItem(Dish,amount)
                self.ItemsOrdered.append(Dish)   
        else:
            Dish.addItem(Dish,amount)
            self.ItemsOrdered.append(Dish)   
        CalculateSum(self) #testing is required for this cause im not sure if it will run a class function  
    def Remove_Item(self,Dish,amount):
        for x in self.ItemsOrdered :
            if(x.Name== Dish.Name & x.price == Dish.price & x.ordered== Dish.ordered):
                x.removeItem(x,amount)
                if(x.ordered<=0):
                    self.ItemsOrdered.remove(x)
                CalculateSum(self)
                break
     

            
        

    