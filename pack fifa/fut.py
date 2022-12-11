import re

import pandas as pd
import requests

from bs4 import BeautifulSoup
 


base_url = "https://sofifa.com/players?offset="
 

for i in range(0, 1):
    url = base_url + str(i * 60)
    source_code = requests.get(url)
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
        for row in soupe.findAll('div',class_='block-quarter'):
            for row in row.findAll('ul',class_='pl' ):
                for row in row.findAll('li'):
                    gendetail=row.find('span')
                    print(gendetail)
           
