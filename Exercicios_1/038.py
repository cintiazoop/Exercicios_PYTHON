# Faça um prg que leia 2 números inteiros e compare-os mostrando na tela uma mensagem.
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais.

numero_1 = int(input('Digite o PRIMEIRO valor -> '))
numero_2 = int(input('Digite o SEGUNDO valor -> '))

if numero_1 > numero_2:
    print('O primeiro valor é MAIOR')
elif numero_2 > numero_1:
    print('O segundo valor é MAIOR')
else:
    print('Não existe valor maior, os dois são iguais')
