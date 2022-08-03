# Faça um prg que faça o cnputador "pensar" em um número inteiro entre 0 e 5 e peça para o usuario tentar
# descobrir qual foi o número escolhido pelo computador. O prg deverá escrever na tela se o usuario venceu ou perdeu.

from random import randint       # random biblioteca p/ gerar aleatoriamente um número inteiro dentro de um intervalo
from time import sleep           # sleep faz o computadar esperar o tempo que vc definir para dar o resultado (um suspense) OPCIONAL

computador = randint(0, 5)       # Sortea aleatoriamente um número entre 0 e 5.

print('-=-' * 20)                # Coloca uma linha na tela para organizar (opcional)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)                # Coloca uma linha na tela para organizar (opcional)

jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(5)                          # Vai aguardar 5 segundos antes de dar o resultado

if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))
