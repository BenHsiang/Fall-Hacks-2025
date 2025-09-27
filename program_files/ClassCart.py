import math
import json
class Cart:
    UserId=0
    Name="Bob"
    ItemsOrdered= list() # list to hold the dishes 
    sum=0 #not total cost but the sum like the subtotal. I will change var name after
    FailedMathA=0
    TotalCost=0
    AdditonalFees=0 #tracks the amount incurred by messing up math questions
    Tax=0 

    ## add the Additonal stuff aka the tax and the wrong math anwsers
   ##webiste is handling add and

    def __init__(self,UserId,name):
        self.Name=name
        self.UserId=UserId
    def CalculateSum(self):
        self.sum=0
        for x in self.ItemsOrdered:
            self.sum+=(x.price *x.ordered)
    
    def addDishToCart(self,Dish,amount):
        length=len(self.ItemsOrdered)
        added=False
        if(length>0):
            for x in self.ItemsOrdered:
                if((x.Name== Dish.Name) & (x.price == Dish.price) & (x.ordered== Dish.ordered)):
                    x.addItem(amount)
                    added=True
                    break
            if(added==False):
                Dish.add_item(amount)
                self.ItemsOrdered.append(Dish)   
        else:
            Dish.add_item(amount)
            self.ItemsOrdered.append(Dish)   
        self.CalcTotalCost() #testing is required for this cause im not sure if it will run a class function  
    def Remove_Item(self,Dish,amount):
        for x in self.ItemsOrdered :
            if((x.Name== Dish.Name) & (x.price == Dish.price) & (x.ordered== Dish.ordered)):
                x.remove_item(amount)
                if(x.ordered<=0):
                    self.ItemsOrdered.remove(x)
                self.CalcTotalCost()
                break
    def PrintOrder(self):
        for x in self.ItemsOrdered:
            print(x.Name + " x "+(str)(x.ordered) +"   "+ (str)(x.ordered*x.price)) # hopefully it can pint new lines
        print("Sub Total:    $",self.sum)
        print("Additonal Fees:    $",self.AdditonalFees)
        print("Tax:    $",self.Tax)
        print("Total:    #",self.TotalCost)

    def CalcAdd(self):
        self.AdditonalFees= self.FailedMathA*self.sum*0.01 #may change value later 
    
    def CalcTax(self):
        self.CalcAdd()
        self.CalculateSum()
        self.Tax=(self.AdditonalFees +self.sum)*0.05 #figure out how to round to 2 dec
        
    
    def CalcTotalCost(self):
        self.CalculateSum()
        self.CalcAdd()
        self.CalcTax()
        self.TotalCost=self.sum +self.AdditonalFees +self.Tax
    def Set_Item_List(self,jsonString): #confuseion but we move forward?
        self.ItemsOrdered=json.loads(jsonString)
        
     
    
           



     

            
        
    