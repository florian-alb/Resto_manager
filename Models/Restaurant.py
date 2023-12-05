from typing import Any

from Models.Customer import Customer
from Models.Order import Order
from Models.Recipie import Recipie, Category


class Restaurant:
    customers = []
    menu = []
    orders = []

    def add_to_menu(self, recipie: Recipie):
        self.menu.append(recipie)

    def add_to_customers_list(self, customer: Customer):
        self.customers.append(customer)

    def add_to_orders_list(self, order: Order):
        self.orders.append(order)

    def show_menu(self):
        print("\n------MENU------")
        print("\n------Starters------")
        for recipe in self.menu:
            if recipe.category.value == "Starter":
                recipe.show()
        print("\n------Mains------")
        for recipe in self.menu:
            if recipe.category.value == "Main course":
                recipe.show()
        print("\n------Desserts------")
        for recipe in self.menu:
            if recipe.category.value == "Dessert":
                recipe.show()

    def show_orders(self):
        print("\n------ORDERS LIST------")
        for order in self.orders:
            order.show_order()

    def show_customers(self):
        print("\n------CUSTOMER LIST------")
        for customer in self.customers:
            customer.show()

    def find_customer_by_id(self, customer_id: int) -> Customer | None:
        for customer in self.customers:
            if customer.ID == customer_id:
                return customer
        return None

    def find_recipie_by_name(self, recipie_name: str) -> Recipie | None:
        for recipie in self.menu:
            if recipie.name == recipie_name:
                return recipie
        return None

    def find_order_by_id(self, order_id: int) -> Order | None:
        for order in self.orders:
            if order.ID == order_id:
                return order
        return None
