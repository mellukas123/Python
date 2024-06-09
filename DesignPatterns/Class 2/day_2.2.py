class InstaSubscriber:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f" {self.name} received {message}")

class Influencer:
    def __init__(self):
        self.subscribers = set()

    def register(self, who):
        print(f"{who.name} subscribed influencer")
        self.subscribers.add(who)

    def unregister(self, who):
        print(f"{who.name} unsubscribed influencer")

        self.subscribers.discard(who)

    def dispatch(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)

class Singer(Influencer):
    products = {
        "shampoo": 100,
        "conditioner":200,
        "cream": 250
    }

    def __init__(self):
        super().__init__()
        self.total_price = 0

    def add_product(self, person, product):
        print(f"{person.name} is buying a product")
        for product_name, product_price in self.products.items():
            if product_name == product:
                self.total_price += product_price

    def discount(self, code, person):
        print(code, person.name, self.total_price)
        if code == "kazdy_spiewac_moze" and person in self.subscribers:
            return 0.75 *self.total_price
        return self.total_price



wersow = Influencer()
person1 = InstaSubscriber("Kasia")
person2 = InstaSubscriber("Adam")
person3 = InstaSubscriber("Ala")

print("Wersow is gaining subs")
wersow.register(person2)
wersow.register(person3)

print("Wersow is creating a post")
wersow.dispatch("Siemka! Zobaczcie mój najnowszy singiel - Ten jeden moment")

wersow.unregister(person3)

print("Wersow is creating a 2 post")
wersow.dispatch("Dzięki za milion wyświetleń!!! ")

wersow.register(person1)

print("Wersow is creating a 3 post")
wersow.dispatch("*** Zdjęcie z dzidziusiem *** ")

beyonce = Singer()
beyonce.add_product(person1, "shampoo")
print(beyonce.discount("spiewac_kazdy_moze", person1))
beyonce.register(person1)
print(beyonce.discount("kazdy_spiewac_moze", person1))
beyonce.register(person2)

beyonce.dispatch("Hi there!")