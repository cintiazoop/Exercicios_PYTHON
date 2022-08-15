# Faça um prg que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

n = int(input('Digite um número -> '))
c = n
f = 1

print(f'Calculando {n}!', end='')
while c > 0:
    print(f'{c}', end='')
    print('x' if c > 1 else ' = ', end='')       # Se for maior que 1 ele vai colocando x senao ele coloca =
    f = f * c

    c = c - 1

print(f'{f}')


