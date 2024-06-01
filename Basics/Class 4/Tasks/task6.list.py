#Implement a function that takes a list of numbers as input
# and returns the sum, average, maximum, and minimum values.
# Use this function on a list entered by the user.
def analyze_numbers(numbers):
    if not numbers:
        return None, None, None, None

    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return total_sum, average, maximum, minimum


# Get input from the user and convert it to a list of numbers
user_input = input("Enter a list of numbers separated by spaces: ")
numbers = [float(num) for num in user_input.split()]

# Call the function and unpack the returned values
total_sum, average, maximum, minimum = analyze_numbers(numbers)

# Display the results
if total_sum is not None:
    print("Sum:", total_sum)
    print("Average:", average)
    print("Maximum:", maximum)
    print("Minimum:", minimum)
else:
    print("No numbers were entered.")
