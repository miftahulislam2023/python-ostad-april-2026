# Parent Class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"{self.brand} {self.model}-এর ইঞ্জিন চালু হয়েছে...")

# Child Class (Vehicle কে ইনহেরিট করছে)
class Car(Vehicle):
    pass

# Grand Child Class (Car কে ইনহেরিট করছে)
class ElectricCar(Car):
    pass

# Grand Grand Child Class (Car কে ইনহেরিট করছে)
class Tesla(ElectricCar):
    pass

my_tesla = Tesla("Tesla", "Model S")
my_tesla.start_engine()