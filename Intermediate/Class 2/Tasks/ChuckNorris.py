import requests


def get_random_chuck_norris_quote():
    # API endpoint
    url = "https://api.chucknorris.io/jokes/random"

    # Make the HTTP GET request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data.get('value', 'Failed to fetch Chuck Norris quote.')
    else:
        return 'Failed to fetch Chuck Norris quote.'


def main():
    # Get a random Chuck Norris quote
    chuck_norris_quote = get_random_chuck_norris_quote()

    # Display the quote
    print("Random Chuck Norris Quote:")
    print(chuck_norris_quote)


if __name__ == "__main__":
    main()
