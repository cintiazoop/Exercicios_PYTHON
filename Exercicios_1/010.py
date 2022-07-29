# Crie um prg que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.

dolar = 5.00
carteira = float(input('Quanto dinheiro vc tem na carteira? -> R$ '))

print('Com R${:.2f}, vc consegue comprar US${:.2F}'.format(carteira, (carteira/dolar)))