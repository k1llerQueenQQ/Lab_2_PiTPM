class Employee:
    name= None
    surname= None
    age= None
    salary= None
    def show(self):
        print(self.name,self.surname,self.age,self.salary)
employee=Employee()
employee.name="Кирилл"
employee.surname="Светлый"
employee.age="17"
employee.salary="19000"
employee.show()
        
