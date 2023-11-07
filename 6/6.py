class Employee:
    def show(self,name,surname,salary,age):
        return name + " " + surname + " " + salary + " " + age
employee1=Employee()
employee1.name="Кирилл"
employee1.surname="Светлый"
employee1.age="17"
employee1.salary="21000"
print(employee1.show(employee1.name,employee1.surname,employee1.age,employee1.salary))       
print()

        
