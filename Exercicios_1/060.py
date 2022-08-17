# Faça um prg que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

n = int(input('Digite um número -> '))
c = n
f = 1

print(f'Calculando {n}!', end='')
while c > 0:
    print(f'{c}', end='')
    print('x' if c > 1 else ' = ', end='')       # if dentro do print - Se for maior que 1 ele vai colocando x senao ele coloca =
    f = f * c

    c = c - 1

print(f'{f}')


# OU

print("---------------------------------------------------------------")

from math import factorial                            # funções matemáticas


for elem in range(n, 0, -1):
    print(elem, end='')                               # essa linha coloca os itens lado a lado. Ex: 54321
    print('x' if elem > 1 else ' = ', end='')         # if dentro do print - Se for maior que 1 ele vai colocando x senao ele coloca = (essa linha só coloca o X e o =
print(factorial(n))





