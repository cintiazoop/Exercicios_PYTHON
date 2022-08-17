# Faça um prg que leia vários números inteiros pelo teclado.
# O prg só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final mostre quantos foram digitados e qual foi a soma entre eles (desconsiderando o flag (999).


# somatorio = 0
# contador = 0
#
# numero = int(input('Digite um número -> '))
#
# while numero != 999:
#     somatorio = somatorio + numero
#     contador = contador + 1
#     numero = int(input('Digite um número -> '))
#
# print(f'Foram digitados {contador} números. O somatórios de todos os números foi {somatorio}.')1
#

# OU

somatorio = 0
contador = 0

while True:                                       # repetição infinita
    numero = int(input('Digite um número -> '))
    if numero == 999:                             # paro a repetição infinita
        break
    contador = contador + 1
    somatorio = somatorio + numero

print(f'Foram digitados {contador} números. O somatórios de todos os números foi {somatorio}.')







