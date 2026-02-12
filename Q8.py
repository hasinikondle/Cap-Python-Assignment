import logging
logging.basicConfig(
    filename="Hostel.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
class HostelRoom:

    room_rent = 5000

    def __init__(self, student_name, months):
        if months <= 0:
            logging.error("Invalid months for %s", student_name)
            raise ValueError("Months must be positive")

        self.student_name = student_name
        self.months = months
        self.status = "Pending"

        logging.info("Room request created for %s", student_name)

    def allocate_room(self):
        self.status = "Allocated"
        logging.info("Room allocated to %s", self.student_name)

    def vacate_room(self):
        self.status = "Vacated"
        logging.warning("Room vacated by %s", self.student_name)

    def calculate_total_fee(self):
        total = self.months * HostelRoom.room_rent
        logging.info("Fee calculated for %s: %s", self.student_name, total)
        return total

    @classmethod
    def update_room_rent(cls, new_rent):
        cls.room_rent = new_rent
        logging.info("Room rent updated to %s", new_rent)

room1 = HostelRoom("Hasini", 6)

room1.allocate_room()
room1.calculate_total_fee()

print()

HostelRoom.update_room_rent(6000)
room1.calculate_total_fee()

room1.vacate_room()
