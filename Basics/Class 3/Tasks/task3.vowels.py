#Vowels - Write a program that will determine the number of vowels in a given string.
# vowels = ['a', 'e', 'i', 'o', 'u']

example_text = "Marzipan cheesecake liquorice marshmallow biscuit oat cake. Fruitcake halvah pastry wafer ice cream pastry candy canes. Lollipop marshmallow fruitcake bonbon cotton candy chocolate bar candy. Cotton candy gingerbread chocolate cupcake jelly-o sesame snaps tart oat cake ice cream."

length = len(example_text)
print(length)

print(f"Amount of letters 'a' in the text is {example_text.count('a')}")
print(f"Amount of letters 'e' in the text is {example_text.count('e')}")
print(f"Amount of letters 'i' in the text is {example_text.count('i')}")
print(f"Amount of letters 'o' in the text is {example_text.count('o')}")
print(f"Amount of letters 'u' in the text is {example_text.count('u')}")


def count_vowels(string):
    # Define a set of vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}

    # Initialize a counter for vowels
    vowel_count = 0

    # Iterate through each character in the string
    for char in string:
        # Check if the character is a vowel (case-insensitive)
        if char.lower() in vowels:
            vowel_count += 1

    return vowel_count


# Test the function
input_string = input("Enter a string: ")
print("Number of vowels in the string:", count_vowels(input_string))