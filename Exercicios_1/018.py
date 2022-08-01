# Faça um prg que leia um ângulo qualquer e mostre o valor do seno (medida vertical),
# cosseno (medida horizoltal) e tangente desse ângulo.

import math

angulo = float(input('Digite o ângulo desejado -> '))
seno = math.sin(math.radians(angulo))         # pega o "angulo" e converte para radiano (math.radians) e depois calcula o seno (math.sin)
print('O ângulo de {} tem o seno de {:.2f}'.format(angulo, seno))

cosseno = math.cos(math.radians(angulo))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(angulo, cosseno))

tangente = math.tan(math.radians(angulo))
print('O ângulo de {} tem a tangenge de {:.2f}'.format(angulo, tangente))