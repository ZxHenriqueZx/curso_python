perguntas = [
    {
        'Pergunta': 'Quanto que é 2x6?',
        'Opções' : ['24', '4', '8', '12'],
        'Resposta' : '12'
    },
    
    {
        'Pergunta': 'Qual é a capital do Brasil?',
        'Opções': ['Brasília', 'Rio de Janeiro', 'São Paulo', 'Brasilândia'],
        'Resposta': 'Brasília'
    }, 

    {
        'Pergunta': 'Qual é a resposta de tudo?',
        'Opções': ['Deus', 'Matemática', '42', 'James da Salada de Fruta'],
        'Resposta': '42'
    }
]

for pergunta in perguntas:
    print(pergunta['Pergunta'])
    
    for i, op in enumerate(pergunta['Opções']):
        print(f'{i}){op}')

    resposta_indice = int(input('Resposta: '))
    
    if pergunta['Opções'][resposta_indice] == pergunta['Resposta']:
        print('certo')
    
    