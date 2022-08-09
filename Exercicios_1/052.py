# Faça um prg que leia um número inteiro e diga se ele é ou não um número primo.

# OBS: são aqueles que apresentam apenas dois divisores: um e o próprio número.


numero = int(input('Digite um número -> '))
contador = 0
for elem in range(1, numero + 1):
    if numero % elem == 0:
        contador = contador + 1

print(f'O número {numero} é divisivel por {contador} vezes')
if contador == 2:                                                 # para ser primo o numero tem que ser divisivel apenas por 1 e por ele mesmo (2 vezes), se for 2 é primo, senao não é primo
    print('Numero é primo')
else:
    print('Numero não é primo')













