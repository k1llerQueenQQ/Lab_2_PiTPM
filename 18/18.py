class Employee:
    __name = "Viktor"
    __age = 27
    __salary = 10000

    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getSalary(self):
        return str(self.__salary) + "$"

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        if 0 <= age <= 120:
            self.__age = age

    def setSalary(self, salary):
        self.__salary = salary


employee = Employee("Egor", 15, 0)
print(employee.getName())
print(employee.getAge())
print(employee.getSalary())
employee.setName("Nikita")
employee.setAge(25)
employee.setSalary(12000)
print(employee.getName())
print(employee.getAge())
print(employee.getSalary())

