# You are the powerful person and you can change
# the weather. Write your own Context, weather strategies
# (Rainy, sunny etc) and test them
from abc import ABC, abstractmethod


class Strategy(ABC):

    @abstractmethod
    def execute(self, temperature):
        pass


class Sunny(Strategy):
    def execute(self, temperature):
        return f"It's {temperature} degrees and the sun is shining!"


class Rainy(Strategy):
    def execute(self, temperature):
        return f"It's {temperature} degrees and it's raining."


class Snowy(Strategy):
    def execute(self, temperature):
        return f"It's {temperature} degrees and it's snowing."


class Default(Strategy):
    def execute(self, temperature):
        return f"It's {temperature} degrees and the weather is cloudy."


class Context:
    strategy: Strategy

    def __init__(self, temperature):
        self.degrees = temperature

    def set_strategy(self, strategy: Strategy = None):
        if strategy is not None:
            self.strategy = strategy
        else:
            self.strategy = Default()

    def execute_strategy(self):
        print(self.strategy.execute(self.degrees))


day1 = Context(15)
day2 = Context(30)
day3 = Context(-7)
day4 = Context(5)

day1.set_strategy()
day2.set_strategy(Sunny())
day3.set_strategy(Snowy())
day4.set_strategy(Rainy())

day1.execute_strategy()
day2.execute_strategy()
day3.execute_strategy()
day4.execute_strategy()