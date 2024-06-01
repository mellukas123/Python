def gcd(a, b):
    while True:
        remainder = a % b
        a = b
        b = remainder
        if b == 0:
            break
    return a

a = 48
b = 18
result = gcd(a, b)
print(f"The GCD of {a} and {b} result is {result}.")