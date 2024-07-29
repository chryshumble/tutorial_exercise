class Pharmacy:
    def __init__(self, analgesic, antimalarial, antibiotics):
        self.analgesic = analgesic
        self.antimalarial = antimalarial
        self.antibiotics = antibiotics

    def __repr__(self):
        return print("this pharmacy dispenses {self.analgesic}, {self.antimalarial}, and {self.antibiotics}. ")

    def customer_order(self, analgesic, antimalarial, antibiotics):
        if analgesic and antimalarial:
             return print(f"{analgesic}, and {antimalarial} has been sent for dispensing")
        else:
            return print(f"you need a prescription to buy {antibiotics}".title())
        
    def pharmacy_name(self):
        name = input("whats the name of this pharmacy ")
        return print(name.title())
        
patient1 = Pharmacy(analgesic="paracetamol", antimalarial="lonart", antibiotics="cefuroxime")
patient1.customer_order(analgesic=None, antimalarial=None, antibiotics="cefuroxime")        
patient1.pharmacy_name()