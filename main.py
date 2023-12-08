from Data.Save import menu_from_json, customers_from_json, orders_from_json
from Models.Restaurant import Restaurant
from User_menu import display_menu
from Models.Customer import *

if __name__ == '__main__':
    resto = Restaurant()

    # data load
    resto.menu = menu_from_json()
    resto.customers = customers_from_json()
    resto.orders = orders_from_json()

    # most popular setup
    resto.set_restaurant_most_popular()

    while True:
        display_menu(resto)



