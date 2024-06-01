example_text = "Blood type is Beer!"

# Length of the string
length = len(example_text)
print(length)

# What is the index of this character(first one)
print(f"Index of letter 'y' in the text is {example_text.index('y')}")

# What is the amount of letters in this text
print(f"Amount of letter 'B' in the text is {example_text.count('B')} ")

# What is the character at the index 6 of the text
print(f"Amount of character at index 6 is {example_text[6]}")

# What are the characters at the index range
print(f"The text in the range is '{example_text[6:13]}'")

# What are the every second character in the index range
print(f"The text in the range is '{example_text[6:13:2]}'")
print(f"The text in the range is '{example_text[::5]}'")
# text[fromIndex_toIndex:step]

# String reversed
print(f"This is a reversed text {example_text[::-1]} ")

# Upper/lower case
print("Converting text to lower case from upper case")
print(example_text.lower())
print(example_text.upper())
print(example_text.capitalize())