import re

import pandas as pd
import requests

from bs4 import BeautifulSoup

# je donne l'url et les colonne
base_url = "https://sofifa.com/players?offset="
source_code = requests.get(base_url)
texte = source_code.text
soup = BeautifulSoup(texte, 'html.parser')
table_body = soup.find('tbody')
for row in table_body.findAll('tr'):
    td = row.findAll('td')
    name = td[1].find("a").get("href")
    url='https://sofifa.com'+name
    html=requests.get(url)
    tex=html.text
    soupe=BeautifulSoup(tex, 'html.parser')
    table=soupe.find("li",class_='ellipsis')
    stat=soupe.find('h5')
    print(stat.text)