class Student:
    name = "Viktor"
    surname = "Letniy"

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

student = Student("ALexandra", "Smith")
print(student.name, student.surname)
