# Faça um prg que calcule o valor a ser pago por um produto, considerando o seu
# PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO:
# A vista dinheiro/cheque: 10% de desconto
# A vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

preco_normal = float(input('Digite o preço das compras -> '))

print(''' FORMAS DE PAGAMENTO
[ 1 ] - A vista dinheiro/cheque
[ 2 ] - A vista no cartão
[ 3 ] - 2x no cartão
[ 4 ] - 3x ou mais no cartão ''')

condicoes_pagamento = int(input('Digite a opção de pagamento -> '))

if condicoes_pagamento == 1:
    valor_pagar = preco_normal - ((preco_normal * 10) / 100)

if condicoes_pagamento == 2:
    valor_pagar = preco_normal - ((preco_normal * 5) / 100)

if condicoes_pagamento == 3:
    valor_pagar = preco_normal
    print('Você pagara 2x R${} SEM JUROS'.format(valor_pagar / 2))

if condicoes_pagamento == 4:
    valor_pagar = preco_normal + ((preco_normal * 20) / 100)
    qtd_parcelas = int(input('Quantas parcelas -> '))
    print('Você pagara {}x R${:.2f} COM JUROS'.format(qtd_parcelas, valor_pagar / qtd_parcelas))
else:
    valor_pagar = 0
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('O valor total a pagar é R${}'.format(valor_pagar))