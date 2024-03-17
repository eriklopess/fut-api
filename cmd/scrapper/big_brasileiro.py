import requests
import json
import os
import uuid
from bs4 import BeautifulSoup
from utils import today, create_file

url = 'https://www.futebolinterior.com.br/campeonato/brasileirao-serie-a-2024/'

def download_page(url):
    response = requests.get(url)
    return response.text

def get_data():
    infos = []
    response = download_page(url)
    soup = BeautifulSoup(str(response), 'html.parser')
    
    table = soup.find('table', class_='table-classification--expansive')
    get_table(table)
    
    rounds = soup.find('div', class_='rounds')
    get_rounds(rounds)
    
        
        
def get_rounds(rounds) -> list:
    dates = []
    info = []
    round_teams = []
    rounds = rounds.find_all('article')
    for round in rounds:
        info.append(round)
        
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
            'id': str(uuid.uuid4()),
            'date': utils_date(dates[int(i / 2)]),
            'teams': f'{round_teams[i - 1]} x {round_teams[i]}'
        }
        matches.append(match)
        
    del matches[0::2]
    jsonify = json.dumps(matches, indent=4)
    
    create_file(str(jsonify), f'rodada_{today()}', 'json')
    return matches

def get_table(table) -> list:
    table = table.find_all('tr')
    tabela = {}
    teams = []
    for i in table:
        teams.append(i.text)
    
    for j in range(len(teams)):
        teams[j] = teams[j].replace('\n', '-').strip()
        teams[j] = teams[j].replace(' ', '').strip()
        teams[j] = teams[j].replace('\r', '').strip()
    
    for k in range(len(teams)):
        teams[k] = teams[k].split('-')
        teams[k] = list(filter(None, teams[k]))
        
    for l in range(len(teams)):
        if len(teams[l]) is 11:
            teams[l] = {
                'position': teams[l][0],
                'team': teams[l][1],
                'points': teams[l][2],
                'played': teams[l][3],
                'won': teams[l][4],
                'drawn': teams[l][5],
                'lost': teams[l][6],
                'goals_for': teams[l][7],
                'goals_against': teams[l][8],
                'goals_difference': teams[l][9],
                # 'percentage': teams[l][10],
                # 'last_games': teams[l][11]
            }
        else:
            teams[l] = {
                'position': teams[l][0],
                'team': teams[l][1],
                'city': teams[l][2],
                'points': teams[l][3],
                'played': teams[l][4],
                'won': teams[l][5],
                'drawn': teams[l][6],
                'lost': teams[l][7],
                'goals_for': teams[l][8],
                'goals_against': teams[l][9],
                'goals_difference': teams[l][10],
                # 'percentage': teams[l][11],
                # 'last_games': teams[l][12]
            }
    tabela['tabela'] = teams
    jsonify = json.dumps(tabela, indent=4)
    
    create_file(str(jsonify), f'tabela_{today()}', 'json')
    return tabela
        

def utils_date(date: str) -> str:
    i = date.split('-')
    if i[1] == '00h00':
        i[1] = 'A definir'
        
    return f'{i[0]} - {i[1]}'      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
def main():
    get_data()
    
main()