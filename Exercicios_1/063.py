# Escreva um prg que leia um número n inteiro qualquer e mostre na tela os n primeiros de uma sequencia FIBONACCI
# Ex: 0 1 1 2 3 5 8


# OBS: Fibonacci, possui o numeral 1 como o primeiro e o segundo termo da ordem, e os seguintes são originados pela soma de seus dois antecessores, observe:
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181...

n = int(input('Quantos termos você quer mostrar? '))
termo_1 = 0
termo_2 = 1
print(f'{termo_1}-> {termo_2}', end='')
contador = 3                                   # Quantidade de termos, já tenho 2 encima
while contador <= n:
    termo_3 = termo_1 + termo_2
    print(f'-> {termo_3}', end='')
    termo_1 = termo_2
    termo_2 = termo_3
    contador = contador + 1
print('-> FIM')
