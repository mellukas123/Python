#Play with words -
# Write a program that will display the given sentence every third character will be capitalized
# and every fourth character will have an exclamation mark after it.

some_text = input("Enter your text and see the magic: ")
new_text = ''
text_length = len(some_text)
for char in some_text:
    if char == [0, -1, 3]:
        new_text += char.upper()
    elif char == [0, -1, 4]:
        new_text += "!"
    else:
        new_text += char
print(new_text)



