# Faça um prg que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preco_produto = int(input('Qual é o preço do produto (em centavos)? R$ '))      # Quando você trabalhar com dinheiro, sempre trabalhe com inteiro (não existe fração de centavo). Ex: 11,50 (errado) 1150 (certo)
desconto = preco_produto * 5 / 100
novo_preco = preco_produto - desconto




# print('O preço do produto é {:.2f}, com os 5% de desconto ficará R$ {:.2f}'.format(preco_produto, novo_preco))
#
# # ou
#
# print(f'O preço do produto é R${preco_produto:.2f}, com os 5% de desconto ficará R$ {novo_preco:.2f}')


print(f'O preço do produto é R${preco_produto/100:.2f}, com os 5% de desconto ficará R${novo_preco/100:.2f}')           # / 100 estou convertendo para reais. Ex: entrou 1000 e converteiu para 10.00
