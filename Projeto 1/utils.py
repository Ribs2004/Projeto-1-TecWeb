import json
from urllib import parse 

"""def extract_route (string):
    splt = string.split(' ')
    return splt[1][1:]"""

def extract_route(string):
    lista_split = string.split(" ")
    return lista_split[1][1:]

def read_file (path):
    with open(path, 'r+b') as f:
        return f.read()

def load_data(file_name):
    with open('data/'+file_name, 'r', encoding='utf-8') as json_file:
        content = json_file.read()
        data = json.loads(content)
        return data
    
def load_template(file):
    with open(f'templates/{file}', 'r', encoding='utf-8') as f:
        return f.read()
    
def append_json(anotacao):
    with open('data/notes.json', 'r+') as f:
        file_data = json.load(f)
        file_data.append(anotacao)
        f.seek(0)
        json.dump(file_data, f, indent=4)
    
def build_response(body='', code=200, reason='OK', headers=''):
    if headers == '':
        response = 'HTTP/1.1 ' + str(code) + ' ' + reason + '\n\n' + body
    else:
        response = 'HTTP/1.1 ' + str(code) + ' ' + reason + '\n' + headers + '\n\n' + body
    return response.encode()
