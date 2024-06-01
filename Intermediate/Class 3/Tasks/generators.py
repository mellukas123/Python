import random
# Generate Even Numbers: Write a generator function that yields even numbers up to a given limit.
def gen_even(number):
    start = 0
    while start <= number:
        if start % 2 == 0:
            yield start

# Reading Large Files Line by Line: Write a generator function that reads a large file line by line and yields each line.
def gen_large_file():
    with open('test.csv', 'r') as f:
        while True:
            line = f.readline()
            if line != '':
                yield f.readline().strip()

for item in gen_large_file():
    print(item)

# Infinite Range Generator: Create a generator function that generates an infinite sequence of numbers starting from a specified start value and incrementing by a specified step.
def gen_infinite(start, step):
    the_number = start
    while True:
        yield the_number
        the_number += step

# Random Number Generator: Write a generator function that generates a sequence of random numbers within a specified range.
def gen_random_with_edges(start,end):
    for _ in range(10):
        yield random.randint(start, end)

# Countdown: Create a generator function that counts down from a specified start value to 0.
def gen_to_zero(start):
    the_number = start
    while the_number != 0:
        yield the_number
        the_number -= 1