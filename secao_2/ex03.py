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

qtd_acerto = 0
for pergunta in perguntas:
    print(pergunta['Pergunta'])

    for i, op in enumerate(pergunta['Opções']):
        print(f'{i}){op}')

    try:
        resposta_indice = int(input('Resposta: '))
        if pergunta['Opções'][resposta_indice] == pergunta['Resposta']:
            print('ACERTOU!!!')
            qtd_acerto += 1
        else:
            print('ERROU!!!')
        print(30*'-')
    except ValueError:
        print('Inválido')
        print(30*'-')
    except IndexError:
        print('Inválido')
        print(30*'-')

print(f'Você acertou {qtd_acerto} de {len(pergunta)}')
