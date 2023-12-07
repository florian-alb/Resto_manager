import json
from json import JSONDecodeError

from Models.Customer import Customer
from Models.Dish import Dish
from Models.Order import Order


def save_menu_to_json(menu):
    dish_json = json.dumps([dish.to_dict() for dish in menu], indent=2)
    with open('Data/jsons/plats.json', 'w') as json_file:
        json_file.write(dish_json)


def save_customer_to_json(customers):
    dish_json = json.dumps([customer.to_dict() for customer in customers], indent=2)
    with open('Data/jsons/clients.json', 'w') as json_file:
        json_file.write(dish_json)


def save_order_to_json(orders):
    order_json = json.dumps([order.to_dict() for order in orders], indent=2)
    with open('Data/jsons/commandes.json', 'w') as json_file:
        json_file.write(order_json)


def menu_from_json():
    try:
        with open('Data/jsons/plats.json', 'r') as json_file:
            data = json.load(json_file)
            return [Dish.from_dict(dish_data) for dish_data in data]
    except FileNotFoundError:
        print("Dishes file not found. No dishes loaded")
        return []


def customers_from_json():
    try:
        with open('Data/jsons/clients.json', 'r') as json_file:
            data = json.load(json_file)
            return [Customer.from_dict(customers_data) for customers_data in data]
    except FileNotFoundError:
        print("Customers file not found. No customers loaded")
        return []
    except JSONDecodeError:
        print("Customers file is empty. No customers loaded")
        return []


def orders_from_json():
    try:
        with open('Data/jsons/commandes.json', 'r') as json_file:
            data = json.load(json_file)
            return [Order.from_dict(order_data) for order_data in data]
    except FileNotFoundError:
        print("Orders file not found. No order loaded")
        return []
    except JSONDecodeError:
        print("Orders file is empty. No order loaded")
        return []
