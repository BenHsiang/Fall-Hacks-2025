#testing class functions
import ClassCart
import ClassDish


def testi():
   print("hello")
   Dish1=ClassDish.Dish(10.99,0,"Tofu","Tofuta")
   Dish2=ClassDish.Dish(5.99,0,"Hamburger","McDonalds")
   MYCart=ClassCart.Cart(1043,"Bob")
   MYCart.addDishToCart(Dish1,10)
   MYCart.addDishToCart(Dish2,10)
   MYCart.PrintOrder()
   print(MYCart.sum)
   MYCart.Remove_Item(Dish1,5)


    

