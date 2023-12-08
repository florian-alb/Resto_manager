from Models import Customer, Dish
from Models.Dish import *


class Order:
    ID = 0

    def __init__(self, customer_id: int, order_id=None, order=None, status=False):
        if order is None:
            self.order = {"Starter": [], "Main course": [], "Dessert": []}
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
        dish_category = dish.category.value
        self.order[dish_category].append(dish)
        print(self.order)

    def remove_from_order(self, dish: Dish):
        self.order.remove(dish)

    def get_order_by_customer_id(self, customer_id: int):
        if self.customer_id == customer_id:
            return self
        return None

    def get_price(self):
        total_price = 0.0
        for category, dishes in self.order.items():
            for item in dishes:
                total_price += item.price
        return total_price

    def show_order(self, restaurant):
        print(f"Order Id: {self.ID}")

        customer = restaurant.find_customer_by_id(self.customer_id)

        print(f"Customer: {customer.firstname} {customer.lastname}")
        print("Order:")

        self.print_sorted_order(self.sort_order())

        print(f"Total price: {self.get_price()}€")
        print("------------------\n")

    def sort_order(self):
        consolidated_order = {"Starter": [], "Main course": [], "Dessert": []}
        for category, dish_list in self.order.items():
            for dish in dish_list:
                found = False
                for item in consolidated_order[category]:
                    if dish.name in item:
                        item[dish.name]['quantity'] += 1
                        found = True
                        break

                if not found:
                    consolidated_order[category].append({dish.name: {'quantity': 1, 'price': dish.price}})

        return consolidated_order

    @staticmethod
    def print_sorted_order(consolidated_order):
        for category, dish_data in consolidated_order.items():
            print("- " + category.upper())
            for item in dish_data:
                for dish_name, data in item.items():
                    print(f"    {dish_name} --- Quantity: "
                          f"{data['quantity']} - "
                          f"Price: {data['price']}€ "
                          f"--- TOTAL PRICE: {data['quantity'] * data['price']}€")

    def print_invoice(self, restaurant):
        self.status = True,
        customer = restaurant.find_customer_by_id(self.customer_id)
        customer.add_to_note(self)

        # invoice printing
        print("\n-------YOUR INVOICE------")
        print(f"-- Invoice n°: {self.ID} --")
        print(f"-- Customer : {customer.firstname} {customer.lastname} {customer.phone_number}")
        self.print_sorted_order(self.sort_order())
        print(f"\n---- TOTAL: {self.get_price()} ----\n")
        print("--Thank you--")

    def to_dict(self):
        order_items = {}
        for category, dish_list in self.order.items():
            dishes = [dish.to_dict() for dish in dish_list]
            order_items[category] = dishes

        return {
            'order_id': self.ID,
            'customer_id': self.customer_id,
            'is_payed': self.status,
            'order_items': order_items
        }

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
            dishes = [Dish.from_dict(dish_data) for dish_data in dish_list]
            order.order[category] = dishes

        return order
