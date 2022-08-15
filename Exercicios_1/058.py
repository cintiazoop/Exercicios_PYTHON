# Melhore o jogo EXERCICIO 028 onde o computador vai 'pensar' em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessarios p/ vencer.

from random import randint

computador = randint(0, 10)                               # Ele vai sorter aleatóriamente um número entre 0 e 10

resposta = False                                          # Já inicia com false
qtd_palpite = 0
while resposta == False:                                  # Vai repetir enquanto a resposta for FALSE
    jogador = int(input("Digite seu palpite -> "))
    if jogador == computador:
        resposta = True
        print(f"Você ACERTOU! O computador escolheu {computador} e você escolheu {jogador}.")
        qtd_palpite = qtd_palpite + 1
    else:
        print("Vc errou! Tente outro palpite")
        qtd_palpite = qtd_palpite + 1

print(f'Para acertar você utilizou {qtd_palpite} palpites.')