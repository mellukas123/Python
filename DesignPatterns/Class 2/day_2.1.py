from abc import ABC, abstractmethod


class Strategy(ABC):

    @abstractmethod
    def execute(self, name):
        pass


class Ambulance(Strategy):
    def execute(self, name):
        return f"{name} is calling Ambulance"


class FirstAid(Strategy):
    def execute(self, name):
        return f"{name} is doing first aid"


class Default(Strategy):
    def execute(self, name):
        return f"{name} is looking at the situation ready to help!"

# for setting strategies and executing it


class Context:
    strategy: Strategy

    def __init__(self, name):
        self.person_name = name

    def set_strategy(self, strategy: Strategy = None):
        if strategy is not None:
            self.strategy = strategy
        else:
            self.strategy = Default()

    def execute_strategy(self):
        print(self.strategy.execute(self.person_name))


person1 = Context("Ann")
person2 = Context("Ola")
person3 = Context("Jack")

# we told people what to do
person1.set_strategy()
person2.set_strategy(FirstAid())
person3.set_strategy(Ambulance())

# they are doing it
person1.execute_strategy()
person2.execute_strategy()
person3.execute_strategy()

person1.set_strategy(FirstAid())
person1.execute_strategy()

# Make your own strategy, context and test setting strategy,
# executing it (change it also) :)
