class Vehicle:
    """
    Base class for all vehicles.

    Attributes:
    - speed: maximum speed of the vehicle in km/h.
    - number_of_wheels: number of wheels on the vehicle.
    """

    def __init__(self, speed, number_of_wheels):
        self.speed = speed
        self.number_of_wheels = number_of_wheels

    def fuel_consumption(self):
        """Abstract method to calculate fuel consumption."""
        raise NotImplementedError("This method should be implemented in a subclass.")

    def vehicle_info(self):
        """Returns a summary of the vehicle's details."""
        return f"{self.__class__.__name__} with {self.number_of_wheels} wheels, speed: {self.speed} km/h."


class Car(Vehicle):
    """
    Class representing a car.

    Additional attributes:
    - fuel_efficiency: fuel consumption in liters per 100 km.
    """

    def __init__(self, speed, fuel_efficiency):
        super().__init__(speed, 4)  # Cars typically have 4 wheels
        self.fuel_efficiency = fuel_efficiency

    def fuel_consumption(self, distance):
        """Calculates fuel consumption for a given distance (in km)."""
        return (distance / 100) * self.fuel_efficiency


class Bicycle(Vehicle):
    """
    Class representing a bicycle.

    Additional attributes:
    - requires_human_power: whether the bicycle is human-powered.
    """

    def __init__(self, speed):
        super().__init__(speed, 2)  # Bicycles have 2 wheels

    def fuel_consumption(self, distance):
        """Bicycles don't consume fuel, so return 0."""
        return 0


class Truck(Vehicle):
    """
    Class representing a truck.

    Additional attributes:
    - fuel_efficiency: fuel consumption in liters per 100 km.
    """

    def __init__(self, speed, fuel_efficiency):
        super().__init__(speed, 6)  # Trucks typically have 6 wheels
        self.fuel_efficiency = fuel_efficiency

    def fuel_consumption(self, distance):
        """Calculates fuel consumption for a given distance (in km)."""
        return (distance / 100) * self.fuel_efficiency


# Example Usage
car = Car(180, 8)  # Speed in km/h, fuel efficiency in L/100km
bicycle = Bicycle(25)  # Speed in km/h
truck = Truck(120, 30)  # Speed in km/h, fuel efficiency in L/100km

print(car.vehicle_info())
print("Fuel consumption for 200 km:", car.fuel_consumption(200))

print(bicycle.vehicle_info())
print("Fuel consumption for 200 km:", bicycle.fuel_consumption(200))

print(truck.vehicle_info())
print("Fuel consumption for 200 km:", truck.fuel_consumption(200))
