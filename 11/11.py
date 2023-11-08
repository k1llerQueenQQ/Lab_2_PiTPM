class Employee:
    name = "Viktor"
    surname = "Letniy"
    age = 32
    salary = 12000

    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary
        print(self.name, self.surname, self.salary)

employee = Employee("Iggy", "Pop", 30000)

