#Write a program where when it starts user is given a couple of options:
# [Register new user, Display users, Q for close the program]
#if register new user is selected ask user some basic information:
# name, age, city, amount of potatoes consumed yesterday.
# Append that data to users list, print thanks to user and return to main menu asking user for his action.
# Empty list to store users
users = []
while True:
    user_input = input("1 - Register new user, 2 - Display users, Q - Close the program: ")

    if user_input == '1':
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        city = input("Enter where are you from: ")
        amount_of_potatoes = input("Enter how many potatoes you consumed yesterday: ")

        # Add user's info
        user_info = {
            "name": name,
            "age": age,
            "city": city,
            "amount_of_potatoes": amount_of_potatoes
        }
        users.append(user_info)

        print("Your user is registered!")

    elif user_input == '2':
        print("Registered users")
        for user in users:
            print(f"Name: {user['name']}, Age: {user['age']}, City: {user['city']}, Amount of potatoes: {user['amount_of_potatoes']}")

    elif user_input == 'Q':
        print("Thank you! See you soon!")
        break

