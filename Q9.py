import logging
logging.basicConfig(
    filename="Recharge.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
class Recharge:

    plans = {"Basic": 199, "Premium": 399}

    def __init__(self, user, balance):
        self.user = user
        self.balance = balance
        self.validity_days = 0

        logging.info("Recharge account created for %s", user)

    def do_recharge(self, amount):
        if amount <= 0:
            logging.warning("Invalid recharge amount")
            return

        self.balance += amount

        if amount >= 599:
            self.validity_days += 84
            logging.info("Recharge done for %s | Amount: %s", self.user, amount)
        elif amount >= 399:
            self.validity_days += 60
            logging.info("Recharge done for %s | Amount: %s", self.user, amount)
        elif amount >= 199:
            self.validity_days += 30
            logging.info("Recharge done for %s | Amount: %s", self.user, amount)
        else:
            logging.warning("Recharge too low for validity extension")


        

    def check_validity(self):
    
        if self.validity_days < 0:
            logging.error("Validity expired")
            print("Validity expired")

        elif self.validity_days == 0:
            logging.warning("Validity expires today")

        else:
            logging.info("Validity remaining: %s days", self.validity_days)
            print(f"Valid for {self.validity_days} more days")

    def show_balance(self):

        if self.balance < 0:
            logging.error("Negative balance detected")
            print("Invalid balance")

        elif self.balance == 0:
            logging.warning("Balance is zero.Recharge required")

        else:
            logging.info("Current balance: %s", self.balance)
            print(f"Available balance: {self.balance}")

    @classmethod
    def update_recharge_plan(cls, plan_name, price):
        cls.plans[plan_name] = price
        logging.info("Plan updated: %s = %s", plan_name, price)

user1 = Recharge("Hasini", 100)

user1.show_balance()
user1.do_recharge(299)
user1.check_validity()

print()
user1.do_recharge(0)
user1.do_recharge(500)
user1.check_validity()
Recharge.update_recharge_plan("Gold", 599)

