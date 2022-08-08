# Faça um prg que faça o compútador jogar JOKENPÔ com vc.

from random import randint             # random biblioteca p/ gerar aleatoriamente um número inteiro dentro de um intervalo

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)              # Sortea aleatoriamente um número entre 0 e 2.

print('''Suas Opções:
[ 0 ] - PRDRA
[ 1 ] - PAPEL
[ 2 ] - TESOURA ''')
jogador = int(input('Qual é a sua jogada? '))

print('Computador jogou {}'.format(itens[computador]))     # itens[computador] vai pegar a escolha de 0 a 2 e mostrar o indice do numero escolhido
print('Jogador jogou {}'.format(itens[jogador]))           # itens[jogador] vai pegar a escolha de 0 a 2 e mostrar o indice do numero escolhido

if computador == 0:                                        # Computador jogou PEDRA
    if jogador == 0:                                       # Jogador também jogou PEDRA
        print('EMPATE!')                                   # EMPATE os 2 jogaram pedra
    elif jogador == 1:
        print('JOGADOR VENCE!')                            # Computador jogou PEDRA e o jogador PAPEL,
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')

if computador == 1:                                       # Computador jogou PAPEL
    if jogador == 0:                                      # Jogador também jogou PEDRA
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')

if computador == 2:                                        # Computador jogou TESOURA
    if jogador == 0:                                       # Jogador também jogou PEDRA
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')