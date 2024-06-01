# Web Scraper: Create a web scraper that retrieves data from multiple URLs simultaneously using multithreading.
# Each thread should handle the scraping of one URL, and the scraped data should be stored or processed in some way.
import threading
import requests
from bs4 import BeautifulSoup

class Scraper(threading.Thread):
    def __init__(self, url):
        super(Scraper, self).__init__()
        self.url = url

    def run(self):
        print(f"Scraping {self.url}...")
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                # Process the scraped data here
                title = soup.title.string.strip() if soup.title else "No title found"
                print(f"Title of {self.url}: {title}")
            else:
                print(f"Failed to scrape {self.url}. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error scraping {self.url}: {e}")

def main():
    urls = [
        "https://example.com",
        "https://google.com",
        "https://github.com",
        "https://openai.com"
    ]

    threads = []
    for url in urls:
        thread = Scraper(url)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()
