def gcd(a, b):
    if (a == 0):
        return b
    if b == 0:
        return a
    # base case
    if a == b:
        return a
    # if a > b
    if a > b:
        return gcd(a-b, b)
    return gcd(a, b-a)


a = 12
b = 8
if(gcd(a, b)):
    print(f"GCD of a and b is {gcd(a, b)}")
else:
    print("Not found")