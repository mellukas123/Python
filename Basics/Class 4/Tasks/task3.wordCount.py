# Write a function that takes a sentence as input and
# returns the count of each word in the sentence.
# Use a dictionary to store the word counts.
# Allow the user to input a sentence and display the word count results
def word_count(sentence):
    # Split the sentences into words
    words = sentence.split()
    # Storing word count
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts
#Get the sentence
user_input = input("Enter your sentence")

result = word_count(user_input)

print("Word counts: ")
for word, count in result.items():
    print(f"{word}: {count}")