import requests

consulta = requests.get('https://jsonplaceholder.typicode.com/posts')

posts = consulta.json()

