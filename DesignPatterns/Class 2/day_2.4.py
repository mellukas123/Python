from abc import ABC, abstractmethod


class Car(ABC):
    @abstractmethod
    def go(self):
        pass


class SportsCar(Car):
    def go(self):
        print('WROOOOOM!')


class Bus(Car):
    def go(self):
        print('That will be quite slow')


class Taxi(Car):
    def go(self):
        print('Hello, taxi driver ')


class CarFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass


class SportsFactory(CarFactory):
    def create_car(self):
        return SportsCar()


class BusFactory(CarFactory):
    def create_car(self):
        return Bus()


class TaxiFactory(CarFactory):
    def create_car(self):
        return Taxi()


type = input("Give a category:")
if type == 'sport':
    factory = SportsFactory()
elif type == 'bus':
    factory = BusFactory()
elif type == 'taxi':
    factory = TaxiFactory()
else:
    raise NotImplementedError(f"there is no such factory like {type}")

car = factory.create_car()
car.go()