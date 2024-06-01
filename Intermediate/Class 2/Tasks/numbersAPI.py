import requests


def get_interesting_fact_about_today():
    # API endpoint with today's date
    url = "http://numbersapi.com/{month}/{day}/date".format(month='4', day='1')  # Example date: April 1st

    # Make the HTTP GET request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        return response.text
    else:
        return 'Failed to fetch interesting fact about today.'


def main():
    # Get an interesting fact about today
    interesting_fact = get_interesting_fact_about_today()

    # Display the fact
    print("Interesting Fact About Today:")
    print(interesting_fact)


if __name__ == "__main__":
    main()
