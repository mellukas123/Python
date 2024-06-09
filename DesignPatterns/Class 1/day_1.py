
def make_pretty(function):
    def inner():
        print("I got decorated")
        function()

    return inner


# base function
def ordinary():
    print("I am ordinary")


decorated_func = make_pretty(ordinary)
decorated_func()

# ordinary()


# 2 example
# decorator
def smart_divide(func):
    def inner_func(a, b):
        print(f"I am going to divide {a} and {b}.")
        if b == 0:
            print("Error, cannot divide!")
            return
        return func(a, b)
    return inner_func


# base function
@smart_divide
def divide(a, b):
    print(a/b)
    return a/b


divide(2, 3)
divide(6, 2)
# divide (2, 0)


# example 3

def decorate_cake(func):
    def some_cake():
        func()
        ingredients = ['pineapple', 'blueberries', ' crumble']

        for i in ingredients:
            print(f"Giving a {i}")
        print("Oh, I got decorated!")

    return some_cake


@decorate_cake
def sponge_cake():
    print("I am simple sponge cake.")


sponge_cake()

# *args?


def print_invitation(name, surname):
    print(f"Hi sweetie, {name}, {surname}")


print_invitation("Ola", "Duda")
print_invitation("ola", "duda")
