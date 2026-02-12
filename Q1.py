class BankAccount:
    
    bank_name = "IOB"
    branch = "Hyderabad"
    country = "India"
    
    def __init__(self, name, age, phone, acc_no, balance):
        self.name = name
        self.age = age
        self.phone = phone
        self.acc_no = acc_no
        self.balance = balance
    
  
    @classmethod
    def set_minimum_balance(cls, amount):
        cls.minimum_balance = amount
        print("Minimum Balance Set To:", amount)
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount Deposited Successfully")
        else:
            print("Invalid Deposit Amount")
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid Withdrawal Amount")
        elif self.balance - amount < BankAccount.minimum_balance:
            print("Cannot Withdraw!")
        else:
            self.balance -= amount
            print("Withdrawal Successful")
    
    def display_details(self):
        print("Name:", self.name)
        print("Account No:", self.acc_no)
        print("Balance:", self.balance)
        print("Minimum Balance:", BankAccount.minimum_balance)



BankAccount.set_minimum_balance(1000)

ob1 = BankAccount("Hasini", 22, 9876543210, "IOB12345", 50000)

ob1.display_details()
print()

ob1.withdraw(49500)
ob1.display_details()
