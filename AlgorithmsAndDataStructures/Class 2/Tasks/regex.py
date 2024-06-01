# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.
# If the function is passed a valid PIN string, return true, else return false.
# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false

def validate_pin(pin):
    # Check if the length of the pin is exactly 4 or 6
    if len(pin) == 4 or len(pin) == 6:
        # Check if all characters in the pin are digits
        return pin.isdigit()
    return False

# Example usage
print(validate_pin("1234"))   # True
print(validate_pin("12345"))  # False
print(validate_pin("a234"))   # False
print(validate_pin("123456")) # True
print(validate_pin("12a456")) # False
