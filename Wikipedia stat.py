# Import libraries
import requests
from bs4 import BeautifulSoup


def scrape_page(url):
    """
    Scrape a Wikipedia page
    :param url:
    :return:
    """
    page = requests.get(url)

    # Create a BeautifulSoup object
    soup = BeautifulSoup(page.text, features='lxml')
    # Pull the table
    result_table = soup.find_all('table', class_="wikitable")
    # Get all the rows "tr"s
    rows = result_table[0].find_all('tr')
    # Parse the headers
    headers = rows[0].find_all("th")
    # print the header
    print(
        f"{headers[0].text.strip():<15} - {headers[1].text.strip():<2} - {headers[2].text.strip():} - "
        f"{headers[3].text.strip():<5}"
    )
    # Get all the cells
    for row in rows:
        cells = row.find_all("td")
        if not cells:
            continue
        print(
            f"{cells[0].text.strip():<15} - {cells[1].text.strip():<15} - "
            f"{cells[2].text.strip():<10} - {cells[3].text.strip():<15}"
        )


if __name__ == "__main__":
    """Main entry point"""
    URL = 'https://en.wikipedia.org/wiki/List_of_Intel_Core_i9_processors'
    scrape_page(URL)