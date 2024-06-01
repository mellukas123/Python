# Write a program that would ask user to input text and print the amount of times the first character of user entered text is repeated.

example_text_1 = input("Give me the text! ")
example_text_2 = (example_text_1.upper())

letter = input("Give me a letter in upper case! ")

print(f"Amount of the that letter in the text is {example_text_2.count(letter)} ")

#print(f"The amount of {text[0]} in the provided text is: {text.count(text[0])}")