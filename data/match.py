import json

class Match:
  def __init__(self, date, home, away, params):
    self.date = date
    self.home = home
    self.away = away
    self.params = params
  
  def __str__(self):
    return f'{self.date} - {self.home} x {self.away}'
  
  
  def loads():
    with open('matches.json', 'r') as file:
      data = json.load(file)
      matches = []
      for match in data:
        date = match['date']
        home = match['teams'].split('x')[0].strip()
        away = match['teams'].split('x')[1].strip()
        
        print(match)
        matches.append(Match(date, home, away, {}))
        
        
      return matches
   
Match.loads()