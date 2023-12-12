from enum import Enum


class Category(Enum):
    STARTER = "Starter"
    MAIN_COURSE = "Main course"
    DESSERT = "Dessert"


class Dish:
    ID = 0

    def __init__(self, name: str, description: str, price: float, category: Category, dish_id=None):
        if dish_id is None:
            Dish.ID += 1
            self.ID = Dish.ID
        else:
            self.ID = dish_id
        self.name = name
        self.description = description
        self.price = price

        if not isinstance(category, Category):
            raise ValueError(f"Invalid category: {category}")
        self.category = category

    def modify_dish_name(self, name: str):
        self.name = name

    def modify_dish_price(self, price: float):
        self.price = price

    def show(self):
        print(f"({self.ID}) - {self.name.upper()} - {self.description} - {self.price}€ ")

    @staticmethod
    def create_dish():
        name = input("Enter the name of the dish: ")
        description = input("Enter the description of the dish: ")
        price = float(input("Enter the price of the dish: "))

        valid_categories = ', '.join(category.name for category in Category)
        while True:
            category_input = input(f"Enter the category of the dish ({valid_categories}): ")
            try:
                category = Category[category_input]
                break
            except KeyError:
                print(f"Invalid category. Please choose from: {valid_categories}")
        return Dish(name, description, price, category)

    def update_dish(self):
        name = input("Enter the new name of the dish: (type nothing to keep the previous name)")
        description = input("Enter the description of the dish: (type nothing to keep the previous description)")
        price = input("Enter the price of the dish: (type nothing to keep the previous price)")

        if name != "":
            self.name = name

        if description != "":
            self.description = description

        if price != "":
            try:
                self.price = float(price)
            except ValueError:
                print(f"Invalid price. Please enter numeric value. Dish price in not updated.")

    def to_dict(self):
        return {
            'ID': self.ID,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'category': self.category.value
        }

    @classmethod
    def from_dict(cls, json_data):
        if json_data['ID'] >= Dish.ID:
            Dish.ID = json_data['ID']
        return cls(
            json_data['name'],
            json_data['description'],
            json_data['price'],
            Category(json_data['category']),
            json_data['ID']
        )
