def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) # 5 * 4 * 3 * 2 * 1


print(f"Factorial of 5! is: {factorial(5)}")
