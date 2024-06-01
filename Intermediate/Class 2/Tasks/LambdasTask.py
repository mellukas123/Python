# Write a program that uses the filter function to print words
# which are palindromes in the word list passed. For example,
# such words are palindromes: radar, level, rotor.

my_list = ["rotor", "level", "radar", "mama"]

is_palindrome = lambda word: word.lower().replace(" ", "") == word.lower().replace(" ", "")[::-1]

palindrome_words = list(filter(is_palindrome, my_list))

print("Palindromes:", palindrome_words)
