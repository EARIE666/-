
class Vehicle:
    def move(self):
        print("Moving...")
    
    def fuel_type(self):
        return "Unknown"

class Car(Vehicle):
    def move(self):
        print("Driving...")
    
    def fuel_type(self):
        return "Petrol"

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling...")
    
    def fuel_type(self):
        return "None"
