from Models.Order import Order


class Customer:
    ID = 0
    total_spend = 0

    def __init__(self, firstname: str, lastname: str, phone_number: str):
        self.firstname = firstname
        self.lastname = lastname
        self.phone_number = phone_number
        Customer.ID += 1
        self.ID = Customer.ID

    def add_to_note(self, order: Order):
        self.total_spend = order.total_price

    def show(self):
        print(
            f"\n({self.ID}) - "
            f"{self.firstname} - "
            f"{self.lastname} - "
            f"{self.phone_number} - "
            f"total spend {self.total_spend}€ ")

    def update_customer(self):
        first_name = input("Enter the new first name of the customer: (type nothing to keep the previous name)")
        last_name = input("Enter the new last name of the customer: (type nothing to keep the previous description)")
        phone_number = input("Enter the new phone number of the customer: (type nothing to keep the previous phone number)")

        if first_name != "":
            self.firstname = first_name

        if last_name != "":
            self.lastname = last_name

        if phone_number != "":
            self.phone_number = phone_number
