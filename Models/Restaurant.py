from datetime import datetime

from Exceptions.NotFoundException import NotFoundException
from Models.Customer import Customer
from Models.Order import Order
from Models.Dish import Dish


class Restaurant:
    def __init__(self):
        self.customers = []
        self.orders = []
        self.menu = []

    def add_to_menu(self, dish: Dish):
        self.menu.append(dish)

    def add_to_customers_list(self, customer: Customer):
        self.customers.append(customer)

    def add_to_orders_list(self, order: Order):
        self.orders.append(order)

    def show_menu(self):
        print("\n------MENU------")
        print("\n------Starters------")
        for dish in self.menu:
            if dish.category.value == "Starter":
                dish.show()
        print("\n------Mains------")
        for dish in self.menu:
            if dish.category.value == "Main course":
                dish.show()
        print("\n------Desserts------")
        for dish in self.menu:
            if dish.category.value == "Dessert":
                dish.show()

    def show_orders(self):
        print("\n------ORDERS LIST------")
        for order in self.orders:
            order.show_order(self)

    def show_customers(self):
        print("\n------CUSTOMER LIST------")
        for customer in self.customers:
            customer.show()

    def find_customer_by_id(self, customer_id: int) -> Customer | None:
        for customer in self.customers:
            if customer.ID == customer_id:
                return customer
        return None

    def find_dish_by_id(self, dish_id: int) -> Dish | None:
        for dish in self.menu:
            if dish.ID == dish_id:
                return dish
        return None

    def find_order_by_id(self, order_id: int) -> Order | None:
        for order in self.orders:
            if order.ID == order_id:
                return order
        return None

    def get_orders_by_date(self, date: datetime):
        orders = []
        for order in self.orders:
            if order.order_date == date:
                orders.append(order)
        if len(orders) == 0:
            raise NotFoundException("No order found at this date.")
        return orders

    def get_orders_by_customer(self, customer: Customer):
        orders = []
        for order in self.orders:
            if order.customer_id == customer.ID:
                orders.append(order)
        if len(orders) == 0:
            raise NotFoundException("No order found for this customer.")
        return orders
