#Write a function that accepts a string and
# replaces all spaces with underscores.
# Additionally, convert the string to lowercase.
# Display the modified string.
def replace_spaces(text):
    new_text = ""
    for symbol in text:
        if symbol == " ":
            new_text += "_"
        else:
            new_text += symbol.lower()
    return new_text

user_input = input("Enter your text to be modified: ")

print(f"Your modified text:", replace_spaces(user_input))
