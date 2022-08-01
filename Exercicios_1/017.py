# Faça um prg que leia o comprimento do cateto oposto | e do cateto adjacente __ de um triaângulo,
# calcule e mostre o comprimento da hipotenusa.
# OBS: O quadrado da hipotenusa é igual a soma dos quadrados dos catetos.

from math import hypot       # math biblioteca para funções matemáticas. hypot função do math que calcula a hipotenusa

cateto_oposto = float(input('Digite o comprimento do cateto oposto -> '))
cateto_adjacente = float(input('Digite o comprimento do cateto oposto -> '))
comp_hipotenusa = hypot(cateto_oposto, cateto_adjacente)                 # hypot (calculo da hipotenusa)

print('A hipotenusa vai medir {:.2f}'.format(comp_hipotenusa))


# OU
# Sem from math import hypot

# cateto_oposto = float(input('Digite o comprimento do cateto oposto -> '))
# cateto_adjacente = float(input('Digite o comprimento do cateto oposto -> '))
# comp_hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
#
# print('A hipotenusa vai medir {:.2f}'.format(comp_hipotenusa))