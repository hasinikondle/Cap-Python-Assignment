import logging

logging.basicConfig(
    filename="Employee.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Employee:

    hra_percentage = 20

    def __init__(self, name, basic_salary, leaves=0):

        if basic_salary <= 0:
            logging.error("Invalid salary for %s", name)
            raise ValueError("Salary must be positive")

        if leaves < 0:
            logging.error("Negative leaves for %s", name)
            raise ValueError("Leaves cannot be negative")

        if leaves > 10:
            logging.warning("High number of leaves for %s", name)

        self.name = name
        self.basic_salary = basic_salary
        self.leaves = leaves

        logging.info("Employee created: %s", name)

    def calculate_salary(self):
        hra = self.basic_salary * self.hra_percentage / 100
        return self.basic_salary + hra

    def apply_leave_deduction(self):
        deduction = self.leaves * 500
        if deduction > 5000:
            logging.warning("High deduction for %s", self.name)
        return deduction

    def display_payslip(self):
        gross = self.calculate_salary()
        deduction = self.apply_leave_deduction()
        net = gross - deduction

        if net <= 0:
            logging.error("Net salary invalid for %s", self.name)
        else:
            logging.info("Payslip generated for %s | Net: %s", self.name, net)

        return net

    @classmethod
    def update_hra_percentage(cls, new_hra):

        if new_hra < 0:
            logging.error("Invalid HRA update attempt")
            raise ValueError("HRA cannot be negative")

        if new_hra > 50:
            logging.warning("Unusually high HRA set: %s%%", new_hra)

        cls.hra_percentage = new_hra
        logging.info("HRA updated to %s%%", new_hra)

emp1 = Employee("Hasini", 30000, 12)
emp1.display_payslip()

Employee.update_hra_percentage(60)

emp2 = Employee("Ravi", 40000, 1)
emp2.display_payslip()

