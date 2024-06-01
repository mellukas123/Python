# String IF statement
if "this" in "This text is ":
    print("It is in there.")

# elif usage example. Note there can be unlimited amount of elif
number = 3
if number > 2:
    number -= 1
elif number < 2:
    number += 6
# elif condition:
#     instruction
else:
    print("You are on your own.")

print(number)

#most common simple use
number2 = int(input())
if number2 > 5:
    print("Do this")
# else: or
elif number2 <= 5:
    print("Do another")

# Multiple conditions in one if line
if number2 >= 5 and not (number2 <= 1 or number2 == "Some text"):
    print("Do this")

else:
    print("Do another")

# Examples of and AND or
# c1 = True and True # True
# c1 = True and False # False
# c1 = False and True # False
# c1 = False and False # False
#
# c1 = True or True # True
# c1 = True or False # True
# c1 = False or True # True
# c1 = False or False # False

user_input = int(input("What is your age: "))
if user_input <= 18:
    print("Here have some fun")
else:
    print("Nah brah")
    # or in one line:
print("Here have some fun") if user_input <= 18 else print("Nah brah")
print("Success Case") if user_input <= 18 else print("Fail Case")