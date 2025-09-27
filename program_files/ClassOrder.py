# ClassOrder.py
#
# Object containing details of an order, used for tracking multiple orders.

class Order:
    restaurant = ""
    price = 0.0
    
    def __init__(self, restaurant_name, price):
        self.restaurant = restaurant_name
        self.price = price

    def get_restaurant(self):
        return self.restaurant

    def get_price(self):
        return self.price