from datetime import datetime
from Models import Customer, Dish
from Models.Dish import *

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle

class Order:
    ID = 0

    def __init__(self, customer_id: int, order_id=None, order=None, status=False, order_date=None):
        if order is None:
            self.order = {"Starter": [], "Main course": [], "Dessert": []}
        else:
            self.order = order

        if order_date is None:
            self.order_date = datetime.now()
        else:
            self.order_date = order_date

        if order_id is None:
            Order.ID += 1
            self.ID = Order.ID
        else:
            self.ID = order_id
        self.customer_id = customer_id
        self.status = status

    def add_to_order(self, dish: Dish, quantity=1):
        dish_category = dish.category.value
        self.order[dish_category].append(dish)
        print(self.order)

    def remove_from_order(self, dish: Dish):
        self.order.remove(dish)

    def get_order_by_customer_id(self, customer_id: int):
        if self.customer_id == customer_id:
            return self
        return None

    def get_price(self):
        total_price = 0.0
        for category, dishes in self.order.items():
            for item in dishes:
                total_price += item.price
        return total_price

    def show_order(self, restaurant):
        print(f"Order Id: {self.ID}")

        customer = restaurant.find_customer_by_id(self.customer_id)

        print(f"Customer: {customer.firstname} {customer.lastname}")
        print("Order:")

        self.print_sorted_order(self.sort_order())

        print(f"Total price: {self.get_price()}€")
        print("------------------\n")

    def sort_order(self, consolidated_order=None):
        if consolidated_order is None:
            consolidated_order = {"Starter": [], "Main course": [], "Dessert": []}

        for category, dish_list in self.order.items():
            for dish in dish_list:
                found = False
                for item in consolidated_order[category]:
                    if dish.name in item:
                        item[dish.name]['quantity'] += 1
                        found = True
                        break

                if not found:
                    consolidated_order[category].append({dish.name: {'quantity': 1, 'price': dish.price}})

        return consolidated_order

    @staticmethod
    def print_sorted_order(consolidated_order):
        for category, dish_data in consolidated_order.items():
            print("- " + category.upper())
            for item in dish_data:
                for dish_name, data in item.items():
                    print(f"    {dish_name} --- Quantity: "
                          f"{data['quantity']} - "
                          f"Price: {data['price']}€ "
                          f"--- TOTAL PRICE: {data['quantity'] * data['price']}€")

    def print_invoice(self, restaurant):
        self.status = True,
        customer = restaurant.find_customer_by_id(self.customer_id)
        customer.add_to_note(self)

        # invoice printing
        print("\n-------YOUR INVOICE------")
        print(f"-- Invoice n°: {self.ID} -- Date: {self.order_date.strftime('%A %d %B %Y')}")
        print(f"-- Customer : {customer.firstname} {customer.lastname} {customer.phone_number}")
        self.print_sorted_order(self.sort_order())
        print(f"\n---- TOTAL: {self.get_price()} ----\n")
        print("--Thank you--")

    def to_dict(self):
        order_items = {}
        for category, dish_list in self.order.items():
            dishes = [dish.to_dict() for dish in dish_list]
            order_items[category] = dishes

        return {
            'order_id': self.ID,
            'customer_id': self.customer_id,
            'date': self.order_date.strftime('%d-%m-%Y'),
            'is_payed': self.status,
            'order_items': order_items
        }

    @classmethod
    def from_dict(cls, json_data):
        if json_data['order_id'] >= Order.ID:
            Order.ID = json_data['order_id']

        order = cls(
            json_data['customer_id'],
            json_data['order_id'],
            None,
            json_data['is_payed'],
            datetime.strptime(json_data['date'], '%d-%m-%Y')
        )

        for category, dish_list in json_data['order_items'].items():
            dishes = [Dish.from_dict(dish_data) for dish_data in dish_list]
            order.order[category] = dishes

        return order

    def generate_invoice_pdf(self, filename, restaurant):
        filename = "Invoices/" + filename

        customer = restaurant.find_customer_by_id(self.customer_id)

        if customer is None:
            print("Error: Customer not found")
            return

        invoice_data = {
            "invoice_number": str(self.ID),
            "invoice_date": self.order_date.strftime("%A %d %B %Y"),
            "customer": f"{customer.firstname} {customer.lastname}",
            "items": self.sort_order(),
            "total": self.get_price(),
        }

        document = SimpleDocTemplate(filename, pagesize=letter)

        style_normal = ParagraphStyle(name='Normal')
        style_centered = ParagraphStyle(name='Center', alignment=1)

        content = []

        header_text = "-------YOUR INVOICE-------"
        content.append(Paragraph(header_text, style_centered))
        content.append(Spacer(1, 12))

        invoice_info = [
            f"-- Invoice n°: {invoice_data['invoice_number']} -- Date: {invoice_data['invoice_date']}",
            f"-- Customer : {invoice_data['customer']}",
        ]
        for info in invoice_info:
            content.append(Paragraph(info, style_normal))

        content.append(Spacer(1, 12))

        item_data = []
        for category, dishes in invoice_data['items'].items():
            for item in dishes:
                item_row = [
                    category,
                    list(item.keys())[0],
                    f"Quantity: {item[list(item.keys())[0]]['quantity']}",
                    f"Price: {item[list(item.keys())[0]]['price']}€",
                    f"TOTAL PRICE: {item[list(item.keys())[0]]['quantity'] * item[list(item.keys())[0]]['price']}€",
                ]
                item_data.append(item_row)

        item_table = Table(item_data, colWidths=[100, 150, 100, 100, 150])
        item_table.setStyle(TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('BACKGROUND', (0, 0), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ]))

        content.append(item_table)
        content.append(Spacer(1, 12))

        total_text = f"---- TOTAL: {invoice_data['total']} ----"
        content.append(Paragraph(total_text, style_centered))

        content.append(Spacer(1, 12))
        content.append(Paragraph("--Thank you--", style_centered))

        document.build(content)
        print(f"The receipt was created under the name '{filename}'")

