# Faça um prg que leia 6  números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor for impar, desconsidere-o.

soma = 0
contador = 0
for elem in range(1, 7):
    numero = int(input(f'Digite o número {elem} -> '))
    if numero % 2 == 0:
        soma = soma + numero
        contador = contador + 1

print(f'Você informou {contador} números PARES e a somo foi {soma}')



# OU



numero_1 = int(input('Digite o PRIMEIRO número -> '))
numero_2 = int(input('Digite o SEGUNDO número -> '))
numero_3 = int(input('Digite o TERCEIRO número -> '))
numero_4 = int(input('Digite o QUARTO número -> '))
numero_5 = int(input('Digite o QUINTO número -> '))
numero_6 = int(input('Digite o SEXTO número -> '))

soma = 0
contador = 0

if numero_1 % 2 == 0:
    soma = soma + numero_1
    contador = contador + 1

if numero_2 % 2 == 0:
    soma = soma + numero_2
    contador = contador + 1

if numero_3 % 2 == 0:
    soma = soma + numero_3
    contador = contador + 1

if numero_4 % 2 == 0:
    soma = soma + numero_4
    contador = contador + 1

if numero_5 % 2 == 0:
    soma = soma + numero_5
    contador = contador + 1

if numero_6 % 2 == 0:
    soma = soma + numero_6
    contador = contador + 1

print(f'Você informou {contador} números PARES e a somo foi {soma}')