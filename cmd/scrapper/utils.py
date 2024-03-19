import datetime
import os

def create_file(text: str, page_name: str, extension: str):
    cwd = os.getcwd()
    with open(f'{cwd}/data/{page_name}.{extension}', 'w') as file:
        file.write(text)

def today():
    return datetime.date.today().strftime('%d-%m-%Y')

def delete_past_files():
    cwd = os.getcwd()
    files = os.listdir(f'{cwd}/data')
    for file in files:
        os.remove(f'{cwd}/data/{file}')
        