# A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).
# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
# The quick brown fox jumps over the lazy dog - True
#
# The quick brown fox jumps over the  - False

def is_pangram(s):
    # Convert the string to lowercase to make the check case-insensitive
    s = s.lower()

    # Create a set of all alphabetic characters in the string
    letters_in_s = set(char for char in s if char.isalpha())

    # Check if the set contains all 26 letters of the English alphabet
    return len(letters_in_s) == 26


# Example usage
print(is_pangram("The quick brown fox jumps over the lazy dog"))  # True
print(is_pangram("The quick brown fox jumps over the"))  # False
