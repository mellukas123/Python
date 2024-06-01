# Simple function, no return, no parameters
def test_function():
    print("Hello form the function!")


# Simple function, returns sum of 2+2, no parameters
def calculator():
    sum_of_two = 2+2
    return sum_of_two
    # a print function that will never run as it is unreachable
    print("Hello form the function!")


# Returns value, no parameters
def conditional():
    if 5 < 3:
        return "Yes"
    else:
        return "No"

# takes parameter, return value, default value
def better_conditional(number=19):
    if number < 18:
         return "Go home"
    else:
        return "Come inside"


# Returns values, has parameters
def calculator_two(number1, number2=6):
    result = number1 + number2
    return result


# test_function()
# result = calculator()
# value = conditional()
# print(value)
# number99 = 99
# number7 = 7
# result = calculator_two(number99,number7)
# print(result)
print(better_conditional())