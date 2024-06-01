#Write a Python program to count the number of even and odd numbers in a series of numbers:
#Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# Expected Output :
# Number of even numbers : 5
# Number of odd numbers : 4
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
numbers_odd = 0
numbers_even = 0
for num in numbers:
    if num // 2*2 == num:
        numbers_even += 1
    else:
        numbers_odd += 1
print("Number of even numbers:", numbers_even)
print("Number of odd numbers:", numbers_odd)
