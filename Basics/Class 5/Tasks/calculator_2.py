print("Hello, Welcome to Calculator 2.0")

while True:
    number_one = float(input("Please provide first number: "))
    number_two = float(input("Please provide the second number: "))
    action = input("Select the action to do: \n"
                   "a - Add \n"
                   "s - Subtract \n"
                   "d - Divide \n"
                   "m - Multiply \n"
                   ":")
    if action == 'a':
        print(f"The Sum of these numbers is", number_one + number_two)
    elif action == 's':
        print(f"The Subtraction of these numbers is", number_one - number_two)
    elif action == 'd':
        print(f"The Division of these numbers is", number_one / number_two)
    elif action == 'm':
        print(f"The Multiplication of these numbers is", number_one * number_two)

    is_again = input("Would you like to do one more? Y or N: ")
    if is_again.upper() == "Y":
        continue
    break
