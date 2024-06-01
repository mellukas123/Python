import requests
import random

# Function to download quotes from the URL
def download_quotes(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to download quotes.")
        return []

# Function to order quotes by length
def order_quotes_by_length(quotes):
    return sorted(quotes, key=len)

# Function to print a random quote to the console
def print_random_quote(quotes):
    random_quote = random.choice(quotes)
    print("Random Quote:", random_quote)

# Function to save quotes to a file
def save_quotes_to_file(quotes, filename):
    with open(filename, 'w') as file:
        for quote in quotes:
            file.write(quote + '\n')

def main():
    # Download quotes from the URL
    url = "https://ron-swanson-quotes.herokuapp.com/v2/quotes/50"
    quotes = download_quotes(url)

    # Order quotes by length
    ordered_quotes = order_quotes_by_length(quotes)

    # Print a random quote to the console
    print_random_quote(quotes)

    # Save quotes to a file
    filename = "ordered_quotes.txt"
    save_quotes_to_file(ordered_quotes, filename)

if __name__ == "__main__":
    main()
