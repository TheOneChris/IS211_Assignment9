import requests
from bs4 import BeautifulSoup

url = 'https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html5lib')

def main(url):
    for tr in soup.find_all('tr', class_='TableBase-bodyTr', limit=30):
        #print(tr)
        name = tr.find('span', class_='CellPlayerName--long').a.text.strip()
        #print("Name: ", name)
        position = tr.find('span', class_='CellPlayerName-position').text.strip()
        #print("Postion: ", position)
        team = tr.find('span', class_='CellPlayerName-team').text.strip()
        #print("Team: ", team)
        find_tds = tr.find_all('td')
        ratings = find_tds[12].get_text().strip()
        #print("Rating", ratings)

        print(f'''
        <---------------------------------------------------------------------->
        |Name: {name}, |Position: {position}, |Team: {team}, |Rating: {ratings}
        <---------------------------------------------------------------------->
        ''')

if __name__ == "__main__":
    main(url)