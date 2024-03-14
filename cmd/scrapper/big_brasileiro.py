import requests
from bs4 import BeautifulSoup

url = 'https://www.futebolinterior.com.br/campeonato/brasileirao-serie-a-2024/'

def create_file(text: str, page_name: str):
    with open(f'{page_name}.html', 'w') as file:
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
    create_file(str(table), 'table')
    
    rounds = soup.find('div', class_='rounds')
    # create_file(str(rounds), 'rounds')
    print(get_rounds(rounds))
    
    
    #create_file(str(infos))
        
        
def get_rounds(rounds) -> list:
    dates = []
    info = []
    round_teams = []
    rounds = rounds.find_all('article')
    for round in rounds:
        info.append(round)
        
    create_file(str(info), 'rounds')
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
    for i in range(len(dates)):
        match = {
            'date': dates[i],
            'teams': f'{round_teams[i]} x {round_teams[i+1]}'
        }
        i+1
        matches.append(match)
     
    return matches

def get_teams():
    pass
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
def main():
    get_data()
    
main()