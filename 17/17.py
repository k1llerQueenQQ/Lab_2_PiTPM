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

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age

    def setSalary(self, salary):
        self.__salary = salary


employee = Employee("Egor", 15, 0)
employee.getName()
employee.getAge()
employee.getSalary()
employee.setName("Nikita")
employee.setAge(25)
employee.setSalary(12000)
employee.getName()
employee.getAge()
employee.getSalary()

