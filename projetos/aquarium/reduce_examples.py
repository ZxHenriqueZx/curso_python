from functools import reduce 

numbers = [1, 3, 5, 9, 5, 2]

def soma(a, b):
    return a + b

soma_1 = reduce(soma, numbers)
print(soma_1)
