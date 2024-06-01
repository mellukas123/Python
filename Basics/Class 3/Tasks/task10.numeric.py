#Write a Python program that accepts a string and calculates the number of digits and letters.
# Use this to help to understand if character is numeric: https://www.w3schools.com/python/ref_string_isnumeric.asp
user_input = input("Enter your text: ")

digits_count = 0
letter_count = 0

for char in user_input:
    if char.isnumeric():
        digits_count += 1
    elif char.isalpha():
        letter_count += 1

print(f"Number of digits is {digits_count} and number of letters is {letter_count}.")