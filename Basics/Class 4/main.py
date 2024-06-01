#Register users - Write a program where when it starts user is given a couple of options:
# [Register new user, Display users, Q for close the program]
#if register new user is selected ask user some basic information:
# name, age, city, amount of potatoes consumed yesterday.
# Append that data to users list, print thanks to user and return to main menu asking user for his action.

# The participant {name}, aged {age} years old, coming from {city} have destroyed {amount_of_potatoes} potatoes yesterday.

import main_functions as fns

entries = []
host_name = input("What is your name?: ")
fns.greet(host_name)

while True:
    user_action = fns.get_action()
    if user_action == '1':
        entries.append(fns.get_entry_details())
    elif user_action == '2':
        fns.show_entries(entries)
    elif user_action == '3':
        print("Thank you for using our services! BYE :)")
        break