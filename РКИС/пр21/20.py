class Student:
    __slots__ = ('name', 'age', 'grades')

    def __init__(self, name, age, grades=None):
        self.name = name
        self.age = age
        self.grades = grades if grades is not None else []

    def add_grade(self, value):
        self.grades.append(value)
        print(f"Добавлена оценка {value} для {self.name}")

    def average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

student1 = Student("Алексей", 20, [4, 5, 3, 5])
student2 = Student("Елена", 19, [5, 5, 4])
student3 = Student("Дмитрий", 21, [3, 4, 4, 5, 3])

student2.add_grade(5)

print(f"{student1.name}: средний балл = {student1.average():.2f}")
print(f"{student2.name}: средний балл = {student2.average():.2f}")
print(f"{student3.name}: средний балл = {student3.average():.2f}")

# Проверка: нельзя добавить новый атрибут
try:
    student1.new_attr = "test"
except AttributeError as e:
    print(f"Нельзя добавить новый атрибут: {e}")