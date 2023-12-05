from Models.Customer import Customer
from Models.Recipie import Recipie, Category
from Models.Restaurant import Restaurant
from User_menu import display_menu

if __name__ == '__main__':
    resto = Restaurant()

    client1 = Customer("John", "Doe", "123-456-7890")
    client2 = Customer("Jane", "Smith", "987-654-3210")

    resto.add_to_customers_list(client1)
    resto.add_to_customers_list(client2)

    starter1 = Recipie("Salade César", "Salade, poulet, parmesan, croutons", 12.5, Category.STARTER)
    main1 = Recipie("Boeuf Bourguignon", "Boeuf mijoté dans du vin rouge", 18.75, Category.MAIN_COURSE)
    dessert1 = Recipie("Tiramisu", "Dessert italien au café", 8.0, Category.DESSERT)

    resto.add_to_menu(starter1)
    resto.add_to_menu(main1)
    resto.add_to_menu(dessert1)

    print(starter1.category.value)

    while True:
        display_menu(resto)



