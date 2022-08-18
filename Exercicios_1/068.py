# Faça um prg que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

# OBS: Funcionamento do jogo: O jagador escolhe um número e escolhe se é Par ou impar. O sistema soma os números e informa se o total é impar ou par


from random import randint

vitorias = 0
while True:                                         # repetição infinita
    jogador = int(input('Diga o valor -> '))
    computador = randint(0, 10)                     # O sorteio será feito de 0 a 10. São os numeros de dedos.
    total = jogador + computador
    resposta = str(input('Par ou impar? [P/I] '))

    if total % 2 == 0 and resposta in 'Pp' or total % 2 == 1 and resposta in 'Ii':
        print(f'O Jogador jogou {jogador} e o computador jogou {computador}. O total = {total}')
        print('DEU PAR!' if total % 2 == 0 else 'DEU IMPAR!')
        print('VC VENCEU!')
        vitorias = vitorias + 1

    else:
            print(f'O Jogador jogou {jogador} e o computador jogou {computador}. O total deu {total}')
            print('DEU PAR!' if total % 2 == 0 else 'DEU IMPAR!')
            print('VC PERDEU!')
            break

print(f'Vc perdeu a última jogada, mas teve {vitorias} vitoria(s) consecutivas')


