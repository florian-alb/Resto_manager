from Models.Order import Order


class Customer:
    ID = 0
    total_spend = 0

    def __init__(self, firstname: str, lastname: str, phone_number: str, customer_id=None):
        if customer_id is None:
            Customer.ID += 1
            self.ID = Customer.ID
        else:
            self.ID = customer_id

        self.firstname = firstname
        self.lastname = lastname
        self.phone_number = phone_number

    def add_to_note(self, order: Order):
        self.total_spend += order.get_price()

    def show(self):
        print(
            f"({self.ID}) - "
            f"{self.firstname} - "
            f"{self.lastname} - "
            f"{self.phone_number} - "
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
            "customer_id": self.ID,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "phone_number": self.phone_number,
            'total_spend': self.total_spend,
        }

    @classmethod
    def from_dict(cls, json_data):
        if json_data['customer_id'] >= Customer.ID:
            Customer.ID = json_data['customer_id']
        return cls(
            json_data['firstname'],
            json_data['lastname'],
            json_data['phone_number'],
            json_data['customer_id']
        )
