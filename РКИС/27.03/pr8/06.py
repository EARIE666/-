
class Employee:
    def salary(self):
        return 0

class FullTimeEmployee(Employee):
    def salary(self):
        return 5000

class PartTimeEmployee(Employee):
    def salary(self):
        return 2000
