#Cats - Write a program that will correctly display the sentence "Alice has x cats" depending on the number of cats, it can show: Alice has 1 cat, Alice has 2 cats, Alice has 10 cats. use user input to get amount of cats. ** After number 20 entered, the output should be "Alice has a cat shelter"

user_input = int(input("How many cats Alice has? "))
if user_input <= 20 :
     print(f"Alice has {user_input} cats")
elif user_input >= 20 :
     print("Alice has a cat shelter.")


