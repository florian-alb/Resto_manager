from datetime import datetime

from Exceptions.NotFoundException import NotFoundException
from Models.Customer import Customer
from Models.Order import Order
from Models.Dish import Dish


class Restaurant:
    mort_popular = {"Starter": "", "Main course": "", "Dessert": ""}

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

    def show_menu(self, preferences=None):
        print("\n------MENU------")

        print("MOST POPULAR")
        for category, dish_name in self.mort_popular.items():
            print(f'\t-{category}: {dish_name}')

        if preferences is not None:
            print("\nYOUR PREFERENCES")
            for category, dish_name in preferences['preferences'].items():
                print(f'\t-{category}: {dish_name}')

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

    def get_most_popular(self, orders=None):
        if orders is None:
            orders = self.orders

        dishes_ordered = {"Starter": [], "Main course": [], "Dessert": []}
        most_popular_dishes = {"Starter": "", "Main course": "", "Dessert": ""}
        for order in orders:
            dishes_ordered = Order.sort_order(order, dishes_ordered)
        for category, dishes in dishes_ordered.items():
            most_popular = max(dishes, key=lambda x: list(x.values())[0]['quantity'])
            most_popular_dishes[category] = list(most_popular.keys())[0]

        return most_popular_dishes

    def set_restaurant_most_popular(self):
        self.mort_popular = self.get_most_popular()

    def get_customer_preferences(self, customer: Customer):
        try:
            customer_orders = self.get_orders_by_customer(customer)
        except NotFoundException as e:
            return {'preferences': None, "error": 'New customer; no preferences for this customer'}
        return {'preferences': self.get_most_popular(customer_orders), "error": None}
