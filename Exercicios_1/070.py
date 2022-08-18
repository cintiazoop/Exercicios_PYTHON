# Faça um prg que leia o NOME e PREÇO de VÁRIOS PRODUTOS.
# O prg deverá perguntar se o usuário vai continuar.
# No final mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1.000.
# C) Qual é o nome do produto mais barato.


preco_total_produto = 0
qtd_mais_de_1000 = 0
qtd_total_produto = 0
nome_produto_barato = ''

while True:                                                           # Irá repetir sem fim até que algo faça ele parar. Vai parar com o break la de baixo
    nome_produto = str(input('Digite o nome do pruduto -> '))
    preco_produto = int(input('Digite o preço do pruduto (Em centavos) -> '))
    preco_total_produto = preco_total_produto + preco_produto
    qtd_total_produto = qtd_total_produto + 1

    if preco_produto > 1000:
        qtd_mais_de_1000 = qtd_mais_de_1000 + 1

    if qtd_total_produto == 1:
        nome_produto_barato = nome_produto
        preco_total_produto = preco_produto

    if qtd_total_produto > 1:
        if preco_produto > preco_total_produto:
            nome_produto_barato = nome_produto

    resposta = str(input('Deseja CONTINUAR cadastrando pruduto? [S/N] ')).strip().upper()[0]    # strip p/ retirar os espaços da frente e de trás da entrada. upper()[0] coloca tudo em maiusculo e analisa somente a 1ª letra.
    if resposta in 'Nn':
        break

print('')
print('----------FIM DA LISTA ----------')
print(f'O total gasto com todos produtos é R${preco_total_produto/100:.2f}')
print(f'Temos {qtd_mais_de_1000} produto que custa mais de R$1000,00.')
print(f'Temos {nome_produto_barato} como produto mais barato.')