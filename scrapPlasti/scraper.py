
import requests
from bs4 import BeautifulSoup

def scrape_website():
    url = 'https://www.plastimac.com.ar/ecommerce/camisetas---30'  # Reemplaza con la URL que deseas scrapear
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        # Convert the soup object to a string to get the entire HTML
        html_content = str(soup.prettify())
        return html_content
    else:
        return None

if __name__ == "__main__":
    html_content = scrape_website()
    if html_content:
        print(html_content)
    else:
        print("Failed to retrieve the HTML content")
