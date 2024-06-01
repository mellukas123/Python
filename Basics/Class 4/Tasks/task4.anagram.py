#Create a function that checks if
# two given strings are anagrams of each other.
# Allow the user to input two strings and use the function
# to determine if they are anagrams.
def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted characters of both strings are equal
    return sorted(str1) == sorted(str2)


# Get input strings from the user
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Check if the strings are anagrams using the function
if are_anagrams(str1, str2):
    print("The strings are anagrams of each other.")
else:
    print("The strings are not anagrams.")
