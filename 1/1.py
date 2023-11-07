import tkinter
import sys
from tkinter import messagebox


class Car:
    color = "Red"
    fuel = 100
    brand = "Lada"
    driver = "Nikita"

    def go(self):
        pass

    def turn(self):
        pass

    def stop(self):
        pass

    def show_info(self):
        print(Car.color, Car.fuel, Car.brand, Car.driver)
        answer = messagebox.askyesno("Выберите:", "Хотите узнать доп. информацию о водителе?")
        if answer == True:
            Driver.show_info(self)
        else:
            sys.exit()


class Driver:
    name = "Nikita"
    surname = "Svetli"
    age = "21"

    def show_info(self):
        print(Driver.name, Driver.surname, Driver.age)


myCar = Car()
myCar.go()

myCar.show_info()
