def is_anagrams(first, second):
    if sorted(first) == sorted(second):
        return True
    return False


text1 = input("Enter the first word: ")
text2 = input("Enter the second word: ")



text = "cba"
print(sorted(text))

if sorted('cba') == sorted('bac'):
    print("Yes")