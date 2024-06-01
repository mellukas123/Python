#Create a calculator that would ask user for first number,
# action, second number, than do the action, display the result,
# ask user if he would like to do more actions:
# if yes, start the program again. if no, terminate the program.
# (Calculator should handle at least +-/*)

user_input = input("Choose an action: a - for addition, s - subtraction, d - division, m -multiplication:  ")
user_input_1 = int(input("Enter the first number: "))
user_input_2 = int(input("Enter the second number:"))
while True:
   if user_input == 'a':
       print(f"Total is: ", {user_input_1 + user_input_2})
   elif user_input == 's':
       print(f"Total is: {user_input_1 - user_input_2}")
   elif user_input == 'd':
       print(f"Total is: {user_input_1 // user_input_2}")
   elif user_input == 'm':
       print(f"Total is: {user_input_1 ** user_input_2}")
   break