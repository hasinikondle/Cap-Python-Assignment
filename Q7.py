import logging

logging.basicConfig(
    filename="Ticket.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Ticket:

    base_fare = 100

    def __init__(self, passenger_name, distance):
        if distance <= 0:
            logging.error("Invalid distance entered")
            raise ValueError("Distance must be positive")

        self.passenger_name = passenger_name
        self.distance = distance
        self.status = "Pending"

        logging.info("Ticket created for %s", passenger_name)

    def book_ticket(self):
        self.status = "Booked"
        logging.info("Ticket booked for %s", self.passenger_name)

    def cancel_ticket(self):
        self.status = "Cancelled"
        logging.warning("Ticket cancelled for %s", self.passenger_name)

    def calculate_fare(self):
        fare = self.distance * Ticket.base_fare
        logging.info("Fare calculated for %s: %s", self.passenger_name, fare)
        return fare

    @classmethod
    def update_base_fare(cls, new_fare):
        if new_fare <= 0:
            logging.error("Invalid base fare update attempt")
            raise ValueError("Base fare must be positive")

        cls.base_fare = new_fare
        logging.info("Base fare updated to %s", new_fare)

ticket1 = Ticket("Hasini", 10)

ticket1.book_ticket()
ticket1.calculate_fare()

print()

Ticket.update_base_fare(150)
ticket1.calculate_fare()

ticket1.cancel_ticket()
