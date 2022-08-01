# Faça um prg que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preco_produto = float(input('Qual é o preço do produto? R$ '))
novo_preco = preco_produto - (preco_produto * 5 / 100)

print('O preço do produto é {}, com os 5% de desconto ficará R$ {}'.format(preco_produto, novo_preco))

