class Patient:
    
    hospital_name = "Apollo Hospital"
    consultation_fee = 500   
    
    def __init__(self, name, age, disease, days_admitted):
        self.name = name
        self.age = age
        self.disease = disease
        self.days_admitted = days_admitted
        self.is_admitted = False
    
    
    def admit_patient(self):
        if not self.is_admitted:
            self.is_admitted = True
            print(self.name, "has been admitted.")
        else:
            print(self.name, "is already admitted.")
    
    
    def discharge_patient(self):
        if self.is_admitted:
            self.is_admitted = False
            print(self.name, "has been discharged.")
        else:
            print(self.name, "is not admitted.")
    
    
    def calculate_bill(self):
        if self.is_admitted:
            room_charge_per_day = 2000
            total = (self.days_admitted * room_charge_per_day) + Patient.consultation_fee
            print("Total Bill for", self.name, "is:", total)
        else:
            print("Patient not admitted.")
    
    
    @classmethod
    def update_consultation_fee(cls, new_fee):
        cls.consultation_fee = new_fee
        print("Consultation Fee Updated to:", new_fee)



p1 = Patient("Hasini", 22, "Fever", 3)

p1.admit_patient()
p1.calculate_bill()

print()


Patient.update_consultation_fee(800)

p1.calculate_bill()

print()

p1.discharge_patient()
