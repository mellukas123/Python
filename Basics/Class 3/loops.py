#while condition:
 #  instruction
number = 0
while number <= 100:
    print(number)
    number += 1

while True:
    user_input = input("a - for addition, s - for subtraction, x - to Quit: ")
    if user_input == 'a':
        print(f"2+2={2 + 2}")
    elif user_input == 's':
        print(f"2-2={2 - 2}")
    elif user_input == 'x':
        print("Thank you for using our services")
        break
    else:
        print("Text was wrong, try one of possible options")

# do:
# instructions
# while condition

# for condition:
#    instruction
cars = ["VW", "Audi", "BMW"]
# print(cars[0], cars[1], cars[2])
for car in cars:
    for parts in car:
        for dust in parts:
            print(car)
    print(car)

for index, car in enumerate(cars):
    print(index, car)

some_text = "This is, a ! very !cool ,text!"
#["This", "is", "a", "very", "cool", "text!"]
new_text = ""
for char in some_text:
    if char == "o":
        new_text += char.upper()
    elif char in "xlT":
        new_text += "@"
    else:
        new_text += char
print(new_text)

# in the brackets write a place you want the text to be split
for word in some_text.split():
    print(word.strip("!,"))
variable = range (5, 101, 20)
print(list(variable))

for number in range(2):
    print(cars[number])

# list comprehension OR one line loop
numbers = []
for i in range (100):
    numbers.append(i)

numbers = [i for i in range (1000)]
print(numbers)