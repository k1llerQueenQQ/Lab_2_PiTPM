class Employee:
    __name = "Viktor"
    __age = 27
    __salary = 10000

    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def getName(self):
        print(self.__name)

    def getAge(self):
        print(self.__age)

    def getSalary(self):
        print(self.__salary)


employee = Employee("Egor", 10, 0)
employee.getName()
employee.getAge()
employee.getSalary()
