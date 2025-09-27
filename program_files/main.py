# main.py
#
# Fall Hacks 2025 Project
# 
# Benley Hsiang
# Aeris Chan
# Brandon Fong
# Duc anh Nguyen

import test
import ClassCart
import ClassDish
import testi 
def main():
    #create dishes
    MyCart=ClassCart.Cart(1111111,"Bob")
    CheeseBurg=ClassDish.Dish(5.99,0,"CHEESEBURGER","Res 1")
    DBB=ClassDish.Dish(7.99,0,"DOUBLE BACON BURGER","Res 1")
    FriesL=ClassDish.Dish(2.49,0,"FRIES(LARGE)","Res 1")
    GCW=ClassDish.Dish(6.49,0,"GRILLED CHICKEN WRAP","Res 2")
    CS=ClassDish.Dish(4.99,0,"CAESAR SALAD","Res 2")
    Pizza=ClassDish.Dish(8.99,0,"PEPPERONI PIZZA","res 3")
    GK=ClassDish.Dish(3.49,0,"GARLIC KNOTS","Res 3")
    VB=ClassDish.Dish(9.49,0,"VEGAN BOWL","Res 4")
    GS=ClassDish.Dish(4.29,0,"GREEN SMOOTHIE","Res 4")


    test.test()
    testi.testi()
    

    
if __name__ == "__main__":
    main()