# Write a decorator that will show how many
# miliseconds(or smaller units of time) it took for
# the function to run.
# (Use Task 1 code but adjust it.)
import datetime

def time(func):
    def wrapper(*args, **kwargs):
        current_time = datetime.datetime.now()
        print("Current time:", current_time.strftime("%H:%M:%S"))
        result = func(*args, **kwargs)
        current_time = datetime.datetime.now()
        print("Time after function call:", current_time.strftime("%H:%M:%S"))
        return result

    return wrapper

@time
def example_function():
    print("This is an example function.")

example_function()

from time import time
t1_start = time()
t1_stop = time()
print(t1_stop - t1_start)