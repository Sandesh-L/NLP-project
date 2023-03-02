#####THIS CODE HAS NOT BEEN TESTED YET


import requests
from bs4 import BeautifulSoup

# The URL of the website we want to scrape
url = "https://www.bluelight.org/"

# Send a GET request to the URL and store the response
response = requests.get(url)

# Create a BeautifulSoup object from the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all instances of the word "drugs" on the page
matches = soup.find_all(string="drugs")

# Print the matched strings
for match in matches:
    print(match)
