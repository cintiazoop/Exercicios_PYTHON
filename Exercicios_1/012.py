# Faça um prg que leia o preço de um produto e mostre seu novo preço com 5% de desconto

preco_produto = float(input('Qual é o preço do produto? R$ '))
desconto = preco_produto * 5 / 100
novo_preco = preco_produto - desconto

print('O preço do produto é {:.2f}, com os 5% de desconto ficará R$ {:.2f}'.format(preco_produto, novo_preco))

# ou

print(f'O preço do produto é R${preco_produto:.2f}, com os 5% de desconto ficará R$ {novo_preco:.2f}')



# Se o preço do produto for 1.10, quanto fica com desconto?