from Models.Customer import Customer
from Models.Order import Order
from Models.Recipie import Recipie
from Models.Restaurant import Restaurant


def display_menu(restaurant: Restaurant):
    print("\n------ MENU ------")
    print("1. Display the menu")
    print("2. Create a customer")
    print("3. Modify a customer")
    print("4. Create a recipe")
    print("5. Modify a recipe")
    print("6. Create an order")
    print("7. Add a recipe to an order")
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
        print("Customer created successfully.")
    elif choice == "3":
        restaurant.show_customers()
        customer_id = int(input("Enter the ID of the customer to modify: "))
        customer = restaurant.find_customer_by_id(customer_id)
        if customer:
            customer.update_customer()
            customer.show()
            print("Customer modified successfully.")
        else:
            print("Customer not found.")

    elif choice == "4":
        recipe = Recipie.create_recipe()
        restaurant.add_to_menu(recipe)
        recipe.show()
        print("Recipe created successfully.")

    elif choice == "5":
        restaurant.show_menu()
        recipie_name = input("Enter the name of the recipe to modify: ")
        recipie = restaurant.find_recipie_by_name(recipie_name)
        if recipie:
            recipie.update_recipe()
            recipie.show()
            print("Recipie modified successfully.")
        else:
            print("Recipie not found.")

    elif choice == "6":
        restaurant.show_customers()
        customer_id = int(input("Enter the ID of the customer for the new order: "))
        customer = restaurant.find_customer_by_id(customer_id)
        if customer:
            order = Order(customer)
            restaurant.add_to_orders_list(order)
            print("Order created successfully.")
        else:
            print("Customer not found.")

    elif choice == "7":
        restaurant.show_orders()
        order_id = int(input("Enter the ID of the order to which to add a recipe: "))
        order = restaurant.find_order_by_id(order_id)
        if order:
            restaurant.show_menu()
            recipe_name = input("Enter the name of the recipe to add to the order: ")
            recipe = restaurant.find_recipie_by_name(recipe_name)
            if recipe:
                order.add_to_order(recipe)
                print("Recipie added to the order successfully.")
            else:
                print("Recipie not found.")
        else:
            print("Order not found.")

    elif choice == "8":
        restaurant.show_orders()

    elif choice == "9":
        print("Thank you for using our program. Goodbye!")
        exit()

    else:
        print("Invalid option. Please choose a valid option.")
