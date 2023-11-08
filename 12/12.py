class Employee:
    name = "Viktor"
    surname = "Letniy"
    age = 32
    salary = 12000

    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    def ShowName(self):
        print(self.name)

    def ShowSurname(self):
        print(self.surname)

    def AddSalary(self):
        self.salary = int(round(self.salary * 1.1))
        print(self.salary)

employee = Employee("Iggy", "Pop", 30000)
employee.ShowName()
employee.ShowSurname()
employee.AddSalary()

