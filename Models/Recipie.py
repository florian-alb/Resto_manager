from enum import Enum


class Category(Enum):
    STARTER = "Starter"
    MAIN_COURSE = "Main course"
    DESSERT = "Dessert"


class Recipie:
    ID = 0

    def __init__(self, name: str, description: str, price: float, category: Category):
        self.name = name
        self.description = description
        self.price = price
        Recipie.ID += 1
        self.ID = Recipie.ID
        if not isinstance(category, Category):
            raise ValueError(f"Invalid category: {category}")
        self.category = category

    def modify_recipe_name(self, name: str):
        self.name = name

    def modify_recipe_price(self, price: float):
        self.price = price

    def show(self):
        print(f"{self.name.upper()} - {self.description} - {self.price}€ ")

    @staticmethod
    def create_recipe():
        name = input("Enter the name of the recipe: ")
        description = input("Enter the description of the recipe: ")
        price = float(input("Enter the price of the recipe: "))

        valid_categories = ', '.join(category.name for category in Category)
        while True:
            category_input = input(f"Enter the category of the dish ({valid_categories}): ")
            try:
                category = Category[category_input]
                break
            except KeyError:
                print(f"Invalid category. Please choose from: {valid_categories}")

        return Recipie(name, description, price, category)

    def update_recipe(self):
        name = input("Enter the new name of the recipe: (type nothing to keep the previous name)")
        description = input("Enter the description of the recipe: (type nothing to keep the previous description)")
        price = float(input("Enter the price of the recipe: (type nothing to keep the previous price)"))

        if name != "":
            self.name = name

        if description != "":
            self.description = description

        if price != 0:
            self.price = price

