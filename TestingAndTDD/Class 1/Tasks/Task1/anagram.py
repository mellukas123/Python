play_string = "ABC"

def is_anagrams(first, second):
    if sorted(first) == sorted(second):
        return True
    return False


text = "cba"
print(sorted(text))

if sorted('cba') == sorted('bac'):
    print("Yes")