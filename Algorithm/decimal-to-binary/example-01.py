def decimal_to_binary(decimal):
    binary = "" # Initialize an empty string to store the binary value

    # Special case for 0
    if decimal == 0:
        return "0"

    while decimal > 0:
        remainder = decimal % 2
        binary = str(remainder) + binary # prepend the remainder to the binary string
        decimal = decimal // 2
    return binary

decimal_number = 45
binary_representation = decimal_to_binary(decimal_number)
print(f"The binary representation of {decimal_number} is: {binary_representation}")
