import re

import pandas as pd
import requests
from bs4 import BeautifulSoup

# je donne l'url et les colonne
base_url = "https://sofifa.com/players?offset="
columns = ['Nom', 'Age', 'Nationalité', 'General', 'Potentiel', 'Club',  'Valeur', 'Salaire']
data = pd.DataFrame(columns = columns)

# je recupère un par un se dont j'ai besoin
for i in range(0, 335):
    url = base_url + str(i * 60)
    source_code = requests.get(url)
    texte = source_code.text
    soup = BeautifulSoup(texte, 'html.parser')
    table_body = soup.find('tbody')
    for row in table_body.findAll('tr'):
        td = row.findAll('td')
        nationality = td[1].find('img').get('title')
        name = td[1].find("a").get("aria-label")
        age = td[2].text
        overall = td[3].text.strip()
        potential = td[4].text.strip()
        club = td[5].find('a').text
        value = td[6].text.strip()
        wage = td[7].text.strip()
        player_data = pd.DataFrame([[name, age,  nationality,  overall, potential, club, value, wage]])
        player_data.columns = columns
        data = data.append(player_data, ignore_index=True)
    print("ok pour"+str(i),end="\r")
data = data.drop_duplicates()
data.head()

#je transfere les donne dans un fiche csv

data.to_csv('data.csv', encoding='utf-8-sig')