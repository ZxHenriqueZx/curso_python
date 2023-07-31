#EXERCÍCIO 1 
# def mult(*args):
#     total = 1
#     for num in args:
#         total *= num

#     return total

# resultado = mult(1,8,6,4,7,2,55)
# print(resultado)

# print(1*2*8*5)

#EXERCÍCIO 2
def par_impar(num):
    resto = num % 2
    if resto == 1:
        return print(f'{num} é impar!')
    return print(f'{num} é par!!')

par_impar(2)
par_impar(5)
par_impar(54)
par_impar(15)
