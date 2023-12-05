from Models import Customer, Recipie


class Order:
    ID = 0
    total_price = 0

    def __init__(self, customer: Customer):
        self.order = []
        self.customer = customer
        Order.ID += 1
        self.ID = Order.ID

    def add_to_order(self, recipie: Recipie):
        self.order.append(recipie)
        self.total_price += recipie.price

    def remove_from_order(self, recipie: Recipie):
        self.order.remove(recipie)
        self.total_price -= recipie.price

    def show_order(self):
        print(f"Order Id: {self.ID}")
        print(f"Customer: {self.customer.firstname} {self.customer.lastname}")
        print("Order:")
        for recipie in self.order:
            print(f"({recipie.category.value}) - {recipie.name} - {recipie.price}€ ")
        print(f"Total price: {self.total_price}€")
        print("------------------\n")
