from Models import Customer, Dish
from Models.Dish import *


class Order:
    ID = 0
    total_price = 0

    def __init__(self, customer: Customer, order_id=None, order=None):
        if order is None:
            self.order = []
        else:
            self.order = order

        if order_id is None:
            Order.ID += 1
            self.ID = Order.ID
        else:
            self.ID = order_id

        self.customer = customer
        customer.orders.append(self)

    def add_to_order(self, dish: Dish):
        self.order.append(dish)
        self.total_price += dish.price

    def remove_from_order(self, dish: Dish):
        self.order.remove(dish)
        self.total_price -= dish.price

    def show_order(self):
        print(f"Order Id: {self.ID}")
        #print(f"Customer: {self.customer.firstname} {self.customer.lastname}")
        print("Order:")
        for dish in self.order:
            print(f"({dish.category.value}) - {dish.name} - {dish.price}€ ")
        print(f"Total price: {self.total_price}€")
        print("------------------\n")

    def to_dict(self):
        return {
            'ID': self.ID,
            'dishes': [dish.to_dict() for dish in self.order],
            'total price': self.total_price,
        }

    @classmethod
    def from_dict(cls, json_data, customer):
        if json_data['ID'] >= Order.ID:
            Order.ID = json_data['ID']
        return cls(
            customer,
            json_data['ID'],
            [Dish.from_dict(order_data) for order_data in json_data['dishes']]
        )
