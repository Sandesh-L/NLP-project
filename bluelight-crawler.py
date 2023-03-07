import requests
from bs4 import BeautifulSoup

# The URL of the website we want to scrape
url = "https://www.bluelight.org/"

page = requests.get(url)

print(page.text)