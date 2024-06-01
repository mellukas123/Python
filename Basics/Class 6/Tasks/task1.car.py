# Create a class called "Car" with attributes like "make," "model," and "year."
# Create an instance of the Car class and print its attributes.
# Add a method to the Car class that calculates the car's age based on the current year.
# Create a subclass of Car called "ElectricCar" with an additional attribute for battery capacity.
# Override the Car class's method in the ElectricCar subclass to also calculate the remaining battery life.

from datetime import datetime
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def age(self):
        current_year = datetime.now().year
        return current_year - self.year

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def age(self):
        current_year = datetime.now().year
        age = current_year - self.year
        return f"The car is {age} years old."

    def remaining_battery_life(self, current_battery_health):
        # Assuming a linear model for simplicity
        max_battery_capacity = 100
        remaining_life_percent = (current_battery_health / max_battery_capacity) * 100
        return f"Remaining battery life: {remaining_life_percent}"
# Creating an instance of Car
my_car = Car("Porsche","Taycan", 2022)
print("Car attributes: ")
print("Make: ", my_car.make)
print("Model: ", my_car.model)
print("Year: ", my_car.year)
print("Age: ", my_car.age())

# Creating an instance of ELectricCar
my_electric_car =ElectricCar("Tesla","Model X",2021,100)
print("\nElectric Car attributes:")
print("Make: ", my_electric_car.make)
print("Model: ", my_electric_car.model)
print("Year: ", my_electric_car.year)
print("Battery Capacity: ", my_electric_car.battery_capacity)
print("Age: ", my_electric_car.age())
print(my_electric_car.remaining_battery_life(90))  # Assuming current battery level is 90%