from Data.Save import menu_from_json
from Models.Restaurant import Restaurant
from User_menu import display_menu

if __name__ == '__main__':
    resto = Restaurant()

    # data load
    resto.menu = menu_from_json()
    #resto.customers = customers_from_json()

    while True:
        display_menu(resto)



