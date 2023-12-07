from Models import Customer, Dish
from Models.Dish import *


class Order:
    ID = 0

    def __init__(self, customer_id: int, order_id=None, order=None, status=False):
        if order is None:
            self.order = {"Starter": {}, "Main course": {}, "Dessert": {}}
        else:
            self.order = order

        if order_id is None:
            Order.ID += 1
            self.ID = Order.ID
        else:
            self.ID = order_id
        self.customer_id = customer_id
        self.status = status

    def add_to_order(self, dish: Dish, quantity=1):
        category = dish.category.value
        if dish in self.order[category]:
            self.order[category][dish] += quantity
        else:
            self.order[category][dish] = quantity

    def remove_from_order(self, dish: Dish):
        self.order.remove(dish)

    def get_order_by_customer_id(self, customer_id: int):
        if self.customer_id == customer_id:
            return self
        return None

    def get_price(self):
        total_price = 0
        for dish in self.order:
            total_price += dish.price
        return total_price

    def show_order(self, restaurant):
        print(f"Order Id: {self.ID}")

        customer = restaurant.find_customer_by_id(self.customer_id)

        print(f"Customer: {customer.firstname} {customer.lastname}")
        print("Order:")
        for dish in self.order:
            print(f"({dish.category.value}) - {dish.name} - {dish.price}€ ")
        print(f"Total price: {self.get_price()}€")
        print("------------------\n")

    def print_invoice(self, restaurant):
        self.status = True,
        customer = restaurant.find_customer_by_id(self.customer_id)
        customer.add_to_note(self)

        # invoice printing
        print("\n -------YOUR INVOICE------")
        print("----STARTERS----")

    def to_dict(self):
        order_dict = {
            'order_id': self.ID,
            'customer_id': self.customer_id,
            'is_payed': self.status,
            'order_items': {"Starter": {}, "Main course": {}, "Dessert": {}}
        }

        for category, dishes in self.order.items():
            category_dict = []
            for dish, quantity in dishes.items():
                dish_dict = {
                    'quantity': quantity,
                    'dish': dish.to_dict()
                }
                category_dict.append(dish_dict)

            if category_dict:
                order_dict['order_items'][category] = category_dict

        return order_dict

    @classmethod
    def from_dict(cls, json_data):
        if json_data['order_id'] >= Order.ID:
            Order.ID = json_data['order_id']

        order = cls(
            json_data['customer_id'],
            json_data['order_id'],
            None,
            json_data['is_payed']
        )

        for category, dish_list in json_data['order_items'].items():
            for dish_data in dish_list:
                dish = Dish.from_dict(dish_data['dish'])
                quantity = dish_data['quantity']
                order.add_to_order(dish, quantity)

        return order
