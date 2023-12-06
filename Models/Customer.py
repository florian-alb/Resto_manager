from Models.Order import Order


class Customer:
    ID = 0
    total_spend = 0
    orders = []

    def __init__(self, firstname: str, lastname: str, phone_number: str, orders=None, customer_id=None):
        if customer_id is None:
            Customer.ID += 1
            self.ID = Customer.ID
        else:
            self.ID = customer_id

        if orders is None:
            orders = []

        self.firstname = firstname
        self.lastname = lastname
        self.phone_number = phone_number
        Customer.ID += 1
        self.ID = Customer.ID
        self.orders = orders

    def add_to_note(self, order: Order):
        self.total_spend = order.total_price

    def show(self):
        print(
            f"({self.ID}) - "
            f"{self.firstname} - "
            f"{self.lastname} - "
            f"{self.phone_number} - "
            f"Order count: {len(self.orders)} - "
            f"total spend {self.total_spend}€ ")

    @staticmethod
    def create_customer():
        first_name = input("Enter the customer's first name: ")
        last_name = input("Enter the customer's last name: ")
        phone_number = input("Enter the customer's phone number: ")
        return Customer(first_name, last_name, phone_number)

    def update_customer(self):
        first_name = input("Enter the new first name of the customer: (type nothing to keep the previous name)")
        last_name = input("Enter the new last name of the customer: (type nothing to keep the previous description)")
        phone_number = input(
            "Enter the new phone number of the customer: (type nothing to keep the previous phone number)")

        if first_name != "":
            self.firstname = first_name

        if last_name != "":
            self.lastname = last_name

        if phone_number != "":
            self.phone_number = phone_number

    def to_dict(self):
        return {
            "ID": self.ID,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "phone_number": self.phone_number,
            'total_spend': self.total_spend,
            "orders": [order.to_dict() for order in self.orders]
        }
