from Data.Save import save_menu_to_json, save_customer_to_json
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
    print("8. Print an order")
    print("9. Quit")

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
        restaurant.show_menu()
        dish_name = input("Enter the name of the dish to modify: ")
        dish = restaurant.find_dish_by_name(dish_name)
        if dish:
            dish.update_dish()
            dish.show()
            print("Dish modified successfully.")
        else:
            print("Dish not found.")
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
                print("Dish added to the order successfully.")
            else:
                print("Dish not found.")
        else:
            print("Order not found.")

    elif choice == "8":
        restaurant.show_orders()

    elif choice == "9":
        print("Thank you for using our program. Goodbye!")
        exit()

    else:
        print("Invalid option. Please choose a valid option.")


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
                order = Order(customer)
                restaurant.add_to_orders_list(order)
                print("Order created successfully.")
                edit_order(order, restaurant)
                #save_customer_to_json(restaurant.customers)
            else:
                print("Customer not found.")

        elif choice == "2":
            # create customer
            customer = Customer.create_customer()
            restaurant.add_to_customers_list(customer)
            print("Customer created successfully.")

            # create order
            order = Order(customer)
            restaurant.add_to_orders_list(order)
            print("Order created successfully.")

            # save the customer
            #save_customer_to_json(restaurant.customers)

            # add dish to the order
            edit_order(order, restaurant)

            # save the customer
            #save_customer_to_json(restaurant.customers)
        elif choice == "3":
            return
        else:
            print("Invalid option. Please choose a valid option.")


def edit_order(order: Order, restaurant: Restaurant):
    while True:
        restaurant.show_menu()
        dish_id = input("Enter the ID of the dish to add to the order or 0 to exit: ")
        if dish_id == "0":
            return
        dish = restaurant.find_dish_by_id(int(dish_id))
        if dish:
            order.add_to_order(dish)
            print("Dish added to the order successfully.")
        else:
            print("Dish not found.")
