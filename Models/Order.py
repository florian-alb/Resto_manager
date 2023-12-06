from Models import Customer, Dish


class Order:
    ID = 0
    total_price = 0

    def __init__(self, customer: Customer):
        self.customer = customer
        self.order = []
        Order.ID += 1
        self.ID = Order.ID
        customer.orders.append(self)

    def add_to_order(self, dish: Dish):
        self.order.append(dish)
        self.total_price += dish.price

    def remove_from_order(self, dish: Dish):
        self.order.remove(dish)
        self.total_price -= dish.price

    def show_order(self):
        print(f"Order Id: {self.ID}")
        print(f"Customer: {self.customer.firstname} {self.customer.lastname}")
        print("Order:")
        for dish in self.order:
            print(f"({dish.category.value}) - {dish.name} - {dish.price}€ ")
        print(f"Total price: {self.total_price}€")
        print("------------------\n")

    def to_dict(self):
        return {
            'ID': self.ID,
            'dishes': [dish.to_dict() for dish in self.order],
            'total price': self.total_price,
        }
