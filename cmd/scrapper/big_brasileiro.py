import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.futebolinterior.com.br/campeonato/brasileirao-serie-a-2024/'

def create_file(text: str, page_name: str, extension: str):
    with open(f'{page_name}.{extension}', 'w') as file:
        file.write(text)

def download_page(url):
    response = requests.get(url)
    #create_file(response.text)
    return response.text

def get_data():
    infos = []
    response = download_page(url)
    soup = BeautifulSoup(str(response), 'html.parser')
    
    table = soup.find('table', class_='table-classification--expansive')
    create_file(str(table), 'table', 'html')
    
    rounds = soup.find('div', class_='rounds')
    # create_file(str(rounds), 'rounds')
    print(get_rounds(rounds))
    print(get_table(table))
    
    #create_file(str(infos))
        
        
def get_rounds(rounds) -> list:
    dates = []
    info = []
    round_teams = []
    rounds = rounds.find_all('article')
    for round in rounds:
        info.append(round)
        
    create_file(str(info), 'rounds', 'html')
    for i in range(len(info)):
        dates.append(info[i].find('time').text)
        info[i] = info[i].find_all('figcaption')
    
    for j in range(len(dates)):
        dates[j] = dates[j].replace('\n', '').strip()
        dates[j] = dates[j].replace(' ', '').strip()
    
    
    for x in info:
        for y in x:
            round_teams.append(y.text)
    
    matches = []
    for i in range(len(round_teams)):
        match = {
            'date': utils_date(dates[int(i / 2)]),
            'teams': f'{round_teams[i - 1]} x {round_teams[i]}'
        }
        matches.append(match)
        
    del matches[0::2]
    jsonify = json.dumps(matches, indent=4)
    create_file(str(jsonify), 'matches', 'json')
    return matches

def get_table(table) -> list:
    pass
        

def utils_date(date: str) -> str:
    i = date.split('-')
    if i[1] == '00h00':
        i[1] = 'A definir'
        
    return f'{i[0]} - {i[1]}'      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
def main():
    get_data()
    
main()