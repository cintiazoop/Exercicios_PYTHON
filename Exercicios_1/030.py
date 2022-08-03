# Faça um prg que leia um número inteiro e mostre se ele é PAR ou IMPAR.

numero = int(input('Digite um número -> '))
resultado = numero % 2                         # resto da divisão por 2

if resultado == 0:                             # o resto de qualquer numero par por 2 é 0, e o numero impar é 1
    print('O número {} é PAR'.format(numero))
else:
    print('O número {} é IMPAR'.format(numero))