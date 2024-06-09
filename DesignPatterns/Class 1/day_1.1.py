class Feed:
    def feed(self):
        print("Yummy, chocolate! Yay, very tasty! I am fed.")


class Hug:
    def hug(self):
        print("Give her a million hugs!!!")


class Blanket:
    def blanket(self):
        print("Man gave the blanket <3")


class Present:
    def present(self):
        print("Here is a gift for you!")


# Facade
class PeriodAction:
    def __init__(self):
        self.feed_object = Feed()
        self.hug_object = Hug()
        self.blanket_object = Blanket()
        self.present_object = Present()

    def start_action(self):
        self.feed_object.feed()
        self.blanket_object.blanket()
        self.hug_object.hug()
        self.present_object.present()

PeriodAction().start_action()
