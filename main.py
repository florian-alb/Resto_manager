from Data.Save import menu_from_json, customers_from_json, get_orders
from Models.Restaurant import Restaurant
from User_menu import display_menu
from Models.Customer import *

if __name__ == '__main__':
    resto = Restaurant()

    # data load
    resto.menu = menu_from_json()
    resto.customers = customers_from_json()
    resto.orders = get_orders(resto.customers)

    while True:
        display_menu(resto)



