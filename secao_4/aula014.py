# json.dump e json.load com arquivos
import json
import os

NOME_ARQUIVO = 'aula014.json'
CAMINHO_ARQUIVO = os.path.abspath(
    os.path.join(os.path.dirname(__file__), NOME_ARQUIVO),
    )

filme = {

    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',
    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None

}

with open(CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(filme, arquivo, ensure_ascii=False, indent=2)

with open(NOME_ARQUIVO, 'r') as arquivo:
    json_str = json.load(arquivo)
    print(json_str)
