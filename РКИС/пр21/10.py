class Employee:
    __slots__ = ('name', 'salary')

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self, percent):
        self.salary += self.salary * percent / 100
        print(f"Зарплата {self.name} увеличена до {self.salary}")

emp = Employee("Петр", 50000)
emp.increase_salary(10)