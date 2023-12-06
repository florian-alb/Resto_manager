import json

from Models.Customer import Customer
from Models.Dish import Dish


def save_menu_to_json(menu):
    dish_json = json.dumps([dish.to_dict() for dish in menu], indent=2)
    with open('Data/jsons/plats.json', 'w') as json_file:
        json_file.write(dish_json)


def save_customer_to_json(customers):
    dish_json = json.dumps([customer.to_json() for customer in customers], indent=2)

    with open('Data/jsons/clients.json', 'w') as json_file:
        json_file.write(dish_json)


def menu_from_json():
    try:
        with open('Data/jsons/plats.json', 'r') as json_file:
            data = json.load(json_file)
            return [Dish.from_dict(dish_data) for dish_data in data]
    except FileNotFoundError:
        print("Dishes file not found. No dishes loaded")
        return []

# def customers_from_json():
#     customers = []
#     try:
#         with open('Data/jsons/clients.json', 'r') as json_file:
#             data = json.load(json_file)
#             for customers_data in data:
#                 customers.append(Customer.from_json(customers_data))
#         return customers
#     except FileNotFoundError:
#         print("Customers file not found. No customers loaded")
#         return customers
