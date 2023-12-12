import os
from datetime import datetime

from Data.Save import save_menu_to_json, save_customer_to_json, save_order_to_json
from Exceptions.NotFoundException import NotFoundException
from Models.Customer import Customer
from Models.Order import Order
from Models.Dish import Dish
from Models.Restaurant import Restaurant


def display_menu(restaurant: Restaurant):
    print("\n------ MENU ------")
    print("1. Display the menu")
    print("2. Create a customer")
    print("3. Modify a customer")
    print("4. Create a dish")
    print("5. Modify a dish")
    print("6. Create an order")
    print("7. Add a dish to an order")
    print("8. Print an invoice")
    print("9. Get invoices for a specific date")
    print("10. Get invoices for a specific customer")
    print("0. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        restaurant.show_menu()
    elif choice == "2":
        first_name = input("Enter the customer's first name: ")
        last_name = input("Enter the customer's last name: ")
        phone_number = input("Enter the customer's phone number: ")
        customer = Customer(first_name, last_name, phone_number)
        restaurant.add_to_customers_list(customer)
        save_customer_to_json(restaurant.customers)
        print("Customer created successfully.")
    elif choice == "3":
        restaurant.show_customers()
        customer_id = int(input("Enter the ID of the customer to modify: "))
        customer = restaurant.find_customer_by_id(customer_id)
        if customer:
            customer.update_customer()
            customer.show()
            save_customer_to_json(restaurant.customers)
            print("Customer modified successfully.")
        else:
            print("Customer not found.")
    elif choice == "4":
        dish = Dish.create_dish()
        restaurant.add_to_menu(dish)
        save_menu_to_json(restaurant.menu)
        dish.show()
        print("Recipe created successfully.")
    elif choice == "5":
        modify_dish(restaurant)
    elif choice == "6":
        create_order(restaurant)

    elif choice == "7":
        restaurant.show_orders()
        order_id = int(input("Enter the ID of the order to which to add a dish: "))
        order = restaurant.find_order_by_id(order_id)
        if order:
            restaurant.show_menu()
            dish_id = input("Enter the ID of the dish to add to the order: ")
            dish = restaurant.find_dish_by_id(int(dish_id))
            if dish:
                order.add_to_order(dish)
                # save the order
                save_order_to_json(restaurant.orders)
                print("Dish added to the order successfully.")
            else:
                print("Dish not found.")
        else:
            print("Order not found.")

    elif choice == "8":
        print_order(restaurant)

    elif choice == "9":
        export_orders_by_date(restaurant)

    elif choice == "10":
        export_orders_by_customer(restaurant)

    elif choice == "0":
        print("Thank you for using our program. Goodbye!")
        exit()

    else:
        print("Invalid option. Please choose a valid option.")


def modify_dish(restaurant):
    while True:
        restaurant.show_menu()
        try:
            dish_id = int(input("Enter the id of the dish to modify or 0 to Exit: "))
            if dish_id == 0:
                return
        except ValueError:
            print('Please enter an integer')
            break
        dish = restaurant.find_dish_by_id(dish_id)
        if dish:
            dish.update_dish()
            dish.show()
            save_menu_to_json(restaurant.menu)
            print("Dish modified successfully.")
        else:
            print("Dish not found.")


def create_order(restaurant: Restaurant):
    while True:
        print("\n-----NEW ORDER-----")

        restaurant.show_customers()

        print("\n1. Existing customer")
        print("2. New customer")
        print("3: EXIT")
        choice = input("Choose an option: ")
        if choice == "1":
            restaurant.show_customers()
            customer_id = int(input("Enter the ID of the customer for the new order: "))
            customer = restaurant.find_customer_by_id(customer_id)
            if customer:

                # create order
                order = Order(customer.ID)
                restaurant.add_to_orders_list(order)
                print("Order created successfully.")
                edit_order(order, restaurant, customer)
                # order save made in edit_order()

            else:
                print("Customer not found.")

        elif choice == "2":
            # create customer
            customer = Customer.create_customer()
            restaurant.add_to_customers_list(customer)
            print("Customer created successfully.")

            # save the customer
            save_customer_to_json(restaurant.customers)

            # create order
            order = Order(customer.ID)
            restaurant.add_to_orders_list(order)
            print("Order created successfully.")

            # save the order
            save_order_to_json(restaurant.orders)

            # add dish to the order
            edit_order(order, restaurant, customer)

            # save the order
            save_order_to_json(restaurant.orders)
        elif choice == "3":
            return
        else:
            print("Invalid option. Please choose a valid option.")


def edit_order(order: Order, restaurant: Restaurant, customer: Customer):
    while True:

        pref = restaurant.get_customer_preferences(customer)

        restaurant.show_menu(pref)
        dish_id = input("Enter the ID of the dish to add to the order or 0 to exit: ")
        if dish_id == "0":
            return
        dish = restaurant.find_dish_by_id(int(dish_id))
        if dish:
            order.add_to_order(dish)
            print("Dish added to the order successfully.")
            # save the order
            save_order_to_json(restaurant.orders)
        else:
            print("Dish not found.")


def print_order(restaurant):
    restaurant.show_orders()
    while True:
        try:
            order_id = int(input("Enter the ID of the order to print or 0 to exit: "))
            if order_id == 0:
                return
            order = restaurant.find_order_by_id(order_id)
            if order:
                order.print_invoice(restaurant)

                # save the customer
                save_customer_to_json(restaurant.customers)

                # export an invoice in PDF
                pdf_filename = f"invoice_{order.ID}_customer{order.customer_id}.pdf"
                order.generate_invoice_pdf(pdf_filename, restaurant)

            else:
                print("Order not found.")
        except ValueError:
            print('Please enter an integer')


def export_orders_by_date(restaurant):
    while True:
        str_date = input("Enter the date of the order to print or 0 to exit (format DD-MM-YYYY): ")

        if str_date == '0':
            return

        try:
            date = datetime.strptime(str_date, '%d-%m-%Y')
        except ValueError:
            print('Invalid date format')
            break

        try:
            orders = restaurant.get_orders_by_date(date)
            save_order_to_json(orders, f"Data/orders_export/order_{str_date}.json")
        except NotFoundException as e:
            print(e.message)


def export_orders_by_customer(restaurant):
    while True:
        restaurant.show_customers()
        str_id = input("Enter the ID of the customer to export all his orders or print 0 to exit: ")

        if str_id == '0':
            return

        try:
            customer_id = int(str_id)
        except ValueError:
            print('Please enter an integer')
            break

        try:
            customer = restaurant.find_customer_by_id(customer_id)
            orders = restaurant.get_orders_by_customer(customer)
            save_order_to_json(orders, f"Data/orders_export/order_customer{customer.ID}.json")
        except NotFoundException as e:
            print(e.message)
