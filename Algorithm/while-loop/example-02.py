# Accept input from user
# If the input is equal to "exit", program should terminates and print out provided input
# If the input is equal to "exit-no-print", program terminates without printing out anything
# If the input is equal to "no-print", program moves to next loop iteration without printing anything
# If the input is different than "exit", "exit-no-print" and "no-print", program repeats
user_input = ""
while user_input != "exit":
    user_input = input("Provide input: ")
    if user_input == "exit-no-print":
        break
    if user_input == "no-print":
        continue
    print(user_input)
else:
    print("Done")