# Faça um prg que simule o funcionamento de um caixa eletrônico.
# No início pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o prg vai informar quantas celulas de cada valor serão entregues.

# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

valor = int(input('Digite o valor da retirada -> '))
total = valor
total_50 = 0
total_20 = 0
total_10 = 0
total_1 = 0

while total > 0:
    if total >= 50:
        total_50 = total_50 + 1
        total = total - 50

    elif total >= 20 and total < 50:
        total_20 = total_20 + 1
        total = total - 20

    elif total >= 10 and total < 20:
        total_10 = total_10 + 1
        total = total - 10

    else:
        if total < 10:
            total_1 = total_1 + 1
            total = total - 1
print('')
print('--------------- SAQUE AUTORIZADO! ---------------')
print('')
print(f'O valor autorizado para o saque é R${valor}')
print(f'{total_50} notas de R$50,00')
print(f'{total_20} notas de R$20,00')
print(f'{total_10} notas de R$10,00')
print(f'{total_1} notas de R$1,00')


