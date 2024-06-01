# Write a decorator that will show the hour, minute and second
# before calling the code of the decorated function and
# after calling the code of the decorated function.
import datetime

# def time(func):
#     def wrapper(*args, **kwargs):
#         current_time = datetime.datetime.now()
#         print("Current time:", current_time.strftime("%H:%M:%S"))
#         result = func(*args, **kwargs)
#         current_time = datetime.datetime.now()
#         print("Time after function call:", current_time.strftime("%H:%M:%S"))
#         return result
#
#     return wrapper

@time
def example_function():
    print("This is an example function.")

example_function()

def disable_at_night(func):
    def wrapper():
        print(datetime.today().time())
        func()
        print(datetime.today().time("%H:%M:%S"))

    return wrapper()

@log_time
def printer():
    print("Some text")