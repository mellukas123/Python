#Write a function that takes a string as input and returns its reverse.
# Use this function to reverse a string entered by the user.
def reverse_string(text):
    reversed_text = text[::-1]
    return reversed_text

user_text = input("Enter the text: ")

reversed_text = reverse_string(user_text)

print("Your text is reversed: ", reversed_text)