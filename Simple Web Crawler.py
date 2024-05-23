# simple_crawler.py

import requests
from bs4 import BeautifulSoup

def get_page_title(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.title.string
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    url = input("Enter the URL: ")
    title = get_page_title(url)
    print(f"Title of the page: {title}")
