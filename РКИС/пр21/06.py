class Student:
    __slots__ = ('name', 'grade')

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def set_grade(self, new_grade):
        self.grade = new_grade
        print(f"Оценка студента {self.name} изменена на {self.grade}")

st = Student("Анна", 4)
st.set_grade(5)