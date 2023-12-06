import json

from Models import Customer, Dish
from Models.Dish import *


class Order:
    ID = 0
    total_price = 0
    order = []

    def __init__(self, customer: Customer):
        self.customer = customer
        Order.ID += 1
        self.ID = Order.ID
        customer.orders.append(self)

    def add_to_order(self, dish: Dish):
        self.order.append(dish)
        self.total_price += dish.price

    def remove_from_order(self, dish: Dish):
        self.order.remove(dish)
        self.total_price -= dish.price

    def show_order(self):
        print(f"Order Id: {self.ID}")
        print(f"Customer: {self.customer.firstname} {self.customer.lastname}")
        print("Order:")
        for dish in self.order:
            print(f"({dish.category.value}) - {dish.name} - {dish.price}€ ")
        print(f"Total price: {self.total_price}€")
        print("------------------\n")

    def to_json(self):
        return {
            'id': self.ID,
            'dishes': [dish.to_json() for dish in self.order],
            'total price': self.total_price,
        }

    @classmethod
    def from_json(cls, order_data):
        order = []
        for dish_data in order_data['dishes']:
            print("dish data", dish_data)
            order.append(Dish.from_json(dish_data))
        return order
