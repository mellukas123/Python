numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = 0

for numbers in numbers:
    if numbers % 2 == 0:
        even += 1

print(f"Even: {even}, Odd: {len(numbers) - even} ")