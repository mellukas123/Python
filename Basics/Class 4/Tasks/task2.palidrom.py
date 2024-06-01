#Create a function that checks if a given string is a palindrome (reads the same backward as forward).
# Use this function to check whether a user-inputted string is a palindrome.
def is_palindrome(text):
    return text == text [::-1]

user_input = input("Enter your text: ")

if is_palindrome(user_input):
    print("The text is a palindrome.")
else:
    print("The text isn't a palindrome")