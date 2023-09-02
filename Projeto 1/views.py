from utils import load_data, load_template, build_response, append_json
from urllib.parse import unquote_plus
from database import *
import urllib
from database import *

db = Database('banco')

def index(request):
    if request.startswith('POST'):
        request = request.replace('\r', '')
        partes = request.split('\n\n')
        corpo = partes[1]
        params = {}

        for chave_valor in corpo.split('&'):
            if chave_valor[0][0] == 't':
                titulo = unquote_plus(chave_valor)
                params['titulo'] = titulo[7:]
            else:
                detalhe = unquote_plus(chave_valor)
                params['detalhes'] = detalhe[9:]

        # append_json(params) só usado em casos que for utilizado o json
        note = Note(title=params['titulo'], content=params['detalhes'])
        db.add(note)
        return build_response(code=303, reason='See Other', headers='Location: /')

    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados.title, details=dados.content, id=dados.id)
        for dados in db.get_all()
    ]
    notes = '\n'.join(notes_li)

    body = load_template('index.html').format(notes=notes)
    return build_response(body=body)


def delete(id):
    db.delete(id)
    return build_response(code=303, reason='See Other', headers='Location: /')

def update(id, request):
    id = int(id)
    request = request.replace('\r', '')
    partes = request.split('\n\n')
    corpo = partes[1]
    params = {}
    for chave_valor in corpo.split('&'):
        if 'titulo' in chave_valor:
            chave_valor = unquote_plus(chave_valor)
            params['titulo'] = chave_valor[7:]
        if 'detalhes' in chave_valor:
            chave_valor = unquote_plus(chave_valor)
            params['detalhes'] = chave_valor[9:]
    # append_json(params) só usado em casos que for utilizado o json
    note = Note(title=params['titulo'], content=params['detalhes'], id=id)
    db.update(note)
    note_template = load_template('components/note.html')
    lista_notas = [
        note_template.format(title=note.title, details=note.content, id=note.id)
        for note in db.get_all()
    ]
    notes = '\n'.join(lista_notas)

    body = load_template('index.html').format(notes=notes)
    return build_response(code=303, reason='See Other', headers='Location: /')

def edit(id):
    id = int(id)
    for notes in db.get_all():
        if notes.id == id:
            note = notes
    body = load_template('edit.html').format(title=note.title, content=note.content, id=note.id)
    return build_response(body=body)

def error404():
    body = load_template('404.html')
    return build_response(body=body, code=404)
