import requests
import random

# Function to fetch a random Ron Swanson quote
def fetch_random_quote():
    response = requests.get("https://ron-swanson-quotes.herokuapp.com/v2/quotes")
    if response.status_code == 200:
        return response.json()[0]  # Extract the first quote from the response
    else:
        return "Failed to fetch quote."

# Decorator function to print a random Ron Swanson quote before calling the original function
def print_random_quote(func):
    def wrapper(*args, **kwargs):
        quote = fetch_random_quote()
        print("Ron Swanson Quote:", quote)
        return func(*args, **kwargs)
    return wrapper

# Example usage of the decorator
@print_random_quote
def example_function():
    print("This is the original function.")

# Call the decorated function
example_function()
