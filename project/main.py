import requests
from bs4 import BeautifulSoup


DOMAIN = 'https://pokemondb.net'
URL = '/pokedex/all'

def get_content(url):
    response = requests.get(url)

    if response.status_code == 200:
        content = response.text

        soup = BeautifulSoup(content, 'html.parser')
        return soup
    else:
        return None

def get_species_pokemon(url):
    soup = get_content(url)

    table = soup.find('table', class_='vitals-table')

    species = table.tbody.find_all('tr')[2].td.text

    return species


def show_pokemon_data():
    soup = get_content(DOMAIN + URL)

    table = soup.find('table', {'id': 'pokedex'})

    for row in table.tbody.find_all('tr', limit = 5):
        columns = row.find_all('td', limit = 3)

        name = columns[1].a.text
        type = [ a.text for a in columns[2].find_all('a') ]
        link = DOMAIN + columns[1].a['href']

        species = get_species_pokemon(link)

        print(name, '-',*type, '-',species)


if __name__ == '__main__':
    show_pokemon_data()