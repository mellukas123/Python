def reverse_string(text):
    return text[::-1]

def is_polindrome(text):
    if check_text == reverse_string(check_text):
        print("The text is a palindrome")
    else:
        print("Nah bro")

check_text = input("Check if this is palindrome:")
is_polindrome(check_text)