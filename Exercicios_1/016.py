# Faça um prg que leia um número real qualquer e mostre  sua porção inteira.
# Ex: Digite 6.127, o numero 6.127 tem a portão inteira 6.

from math import trunc    # math biblioteca para funções matemáticas. trunc função do math que pega a parte inteira de "numero"

numero = float(input('Digite um número -> '))

print('O valor digitado doi {} e a sua porção inteira é {}'.format(numero, trunc(numero)))       # math.trunc pega a parte inteira de "numero"

# OU

# Sem importar nada

print('O valor digitado doi {} e a sua porção inteira é {}'.format(numero, int(numero)))       # o int pega a parte inteira de "numero"

