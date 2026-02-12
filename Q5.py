import logging

logging.basicConfig(
    filename="order.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Order:

    tax_percentage = 5

    def __init__(self, product, price, quantity):
        if price <= 0 or quantity <= 0:
            logging.error("Invalid price or quantity")
            raise ValueError("Price and Quantity must be positive")

        self.product = product
        self.price = price
        self.quantity = quantity
        self.status = " "

        logging.info("Order created for %s", product)

    def place_order(self):
        self.status = "Placed"
        logging.info("Order placed for %s", self.product)

    def cancel_order(self):
        self.status = "Cancelled"
        logging.warning("Order cancelled for %s", self.product)

    def calculate_total_price(self):
        subtotal = self.price * self.quantity
        tax = subtotal * Order.tax_percentage / 100
        total = subtotal + tax
        logging.info("Total calculated for %s: %s", self.product, total)
        return total

    @classmethod
    def update_tax_percentage(cls, new_tax):
        cls.tax_percentage = new_tax
        logging.info("Tax updated to %s%%", new_tax)


order1 = Order("Laptop", 50000, 1)
print(order1.status)
order1.place_order()
order1.calculate_total_price()

print()

Order.update_tax_percentage(12)
order1.calculate_total_price()

order1.cancel_order()
