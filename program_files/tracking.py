# tracking.py
#
# Simulates the tracking of food order deliveries.

import queue
import timer
import ClassOrder
import random
import time

orders = queue.Queue(5) #Initializing queue of arbitrary size, can be changed later
counter = 1
random.seed(time.time())

# So far only works for one at a time because of the timer
def add_order(restaurant_name, total_cost):
    food_order = ClassOrder.Order(restaurant_name, total_cost)
    orders.put(food_order)
    global counter 

    print("\n")
    print("Order number {}:".format(counter))
    print("Restaurant: {}".format(food_order.get_restaurant()))
    print("Total: ${:.2f}".format(food_order.get_price()))
    timer.countdown(random.randint(1, 1))

    counter += 1

def remove_finished_order():
    queue.get()
