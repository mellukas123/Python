# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
# For example, the score of abad is 8 (1 + 2 + 1 + 4).
# You need to return the highest scoring word as a string.
# If two words score the same, return the word that appears earliest in the original string.

# Cupcake ipsum dolor sit amet cake. Gummies cotton candy carrot cake soufflé pie bear claw chocolate ice cream. Dessert shortbread wafer tiramisu chupa chups. I love candy canes bonbon carrot cake caramels jelly beans. Cake chocolate cake shortbread cupcake carrot cake candy canes I love. Sweet cake cheesecake I love cupcake. Carrot cake muffin tart shortbread bonbon tart topping chocolate carrot cake.

def highest_scoring_word(s):
    # Split the string into words
    words = s.split()

    # Function to calculate the score of a word
    def word_score(word):
        return sum(ord(char) - ord('a') + 1 for char in word)

    # Variables to track the highest score and corresponding word
    highest_score = 0
    highest_word = ""

    for word in words:
        score = word_score(word)
        if score > highest_score:
            highest_score = score
            highest_word = word

    return highest_word


# Example usage
s = "cupcake ipsum dolor sit amet cake. gummies cotton candy carrot cake soufflé pie bear claw chocolate ice cream. dessert shortbread wafer tiramisu chupa chups. i love candy canes bonbon carrot cake caramels jelly beans. cake chocolate cake shortbread cupcake carrot cake candy canes i love. sweet cake cheesecake i love cupcake. carrot cake muffin tart shortbread bonbon tart topping chocolate carrot cake."
print(highest_scoring_word(s))
