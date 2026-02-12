import logging

logging.basicConfig(
    filename="MovieTicket.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class MovieTicket:

    ticket_price = 200
    total_seats = 100        
    occupied_seats = 0      

    def __init__(self, movie_name, seats):

        if seats <= 0:
            logging.error("Invalid seats for movie %s", movie_name)
            

        self.movie_name = movie_name
        self.seats = seats
        self.is_booked = False

        logging.info("Movie ticket created for %s", movie_name)

    def book_seat(self):

        available = MovieTicket.total_seats - MovieTicket.occupied_seats

        if self.seats > available:
            logging.error("Not enough seats available for %s", self.movie_name)
            print("Seats not available")
            return

        MovieTicket.occupied_seats += self.seats
        self.is_booked = True

        logging.info("Seats booked for %s | Seats: %s",
                     self.movie_name, self.seats)

    def cancel_booking(self):

        if not self.is_booked:
            logging.warning("No booking exists to cancel for %s", self.movie_name)
            return

        MovieTicket.occupied_seats -= self.seats
        self.is_booked = False

        logging.warning("Booking cancelled for %s", self.movie_name)

    def calculate_ticket_price(self):

        total = self.seats * MovieTicket.ticket_price
        logging.info("Total ticket price for %s: %s",
                     self.movie_name, total)
        return total

    @classmethod
    def update_ticket_price(cls, new_price):

        if new_price <= 0:
            logging.error("Invalid ticket price update attempt")
            raise ValueError("Price must be positive")

        cls.ticket_price = new_price
        logging.info("Ticket price updated to %s", new_price)

movie1 = MovieTicket("Pushpa 2", 3)
movie1.book_seat()
movie1.calculate_ticket_price()

MovieTicket.update_ticket_price(300)
movie1.calculate_ticket_price()

movie1.cancel_booking()
movie1.cancel_booking()   

movie2 = MovieTicket("Salaar 2", 200)
movie2.book_seat()        

movie3 = MovieTicket("Animal 2", -5)  
