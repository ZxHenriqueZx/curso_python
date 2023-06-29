import math

palavras = ['Reviver', 'socos', 'ana', 'Luis', 'Omissíssimo', 'Carro']    

#MINHA SOLUÇÃO
def verf_palindromo(palavra):
    palavra = palavra.upper()
    palavra_invertida = palavra[::-1]                
    if palavra == palavra_invertida:
        return f'{palavra} é um palíndromo {palavra_invertida}'
    else:
        return f'{palavra} não é um palíndromo {palavra_invertida}'

#SOLUÇÃO 1 VÍDEO
def verf_palindromo_2(palavra):
    palavra = palavra.upper()
    j = len(palavra) - 1
    score = 0
    for i in range(len(palavra)):
        if palavra[i] == palavra[j]:
            score += 1
        if i >= j:
            break
        j -= 1

    if score == math.ceil(len(palavra) / 2):
        return f'{palavra} é um palíndromo {palavra[::-1]}'
    else:
        return f'{palavra} não é um palíndromo {palavra[::-1]}'

#SOLUÇÃO 2 VÍDEO
def verf_palindromo_3(palavra):
    palavra = palavra.upper()
    if len(palavra) <= 1:
        return True
    else:
        return palavra[0] == palavra[-1] and verf_palindromo_3(palavra[1:-1])
        
                
for word in palavras:
    print(verf_palindromo_3(word))
    
