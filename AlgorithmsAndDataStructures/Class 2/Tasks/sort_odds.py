# Given an array of numbers.
# You have to sort the odd numbers in ascending order while leaving the even numbers
# at their original positions.
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

def sort_array(source_array):
    # Extract the odd numbers and sort them
    odd_numbers = sorted([num for num in source_array if num % 2 != 0])

    # Iterator for the sorted odd numbers
    odd_iter = iter(odd_numbers)

    # Replace the odd numbers in the original array with the sorted odd numbers
    result = [next(odd_iter) if num % 2 != 0 else num for num in source_array]

    return result


# Example usage
print(sort_array([7, 1]))  # [1, 7]
print(sort_array([5, 8, 6, 3, 4]))  # [3, 8, 6, 5, 4]
print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))  # [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
