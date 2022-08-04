# Faça um prg para aprovar o emprestimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal, não pode exceder 30% do salário ou entao o emprestimo será negado.


valor_casa = float(input('Digite o valor da casa R$ '))
salario = float(input('Digite o salário R$ '))
prazo_pagamento = int(input('Digite o prazo para o pagamento '))
prestacao = valor_casa / (prazo_pagamento * 12)
minimo = salario * 30 / 100

print('Para pagar um casa de R${:.2f} em {} anos. '.format(valor_casa, prazo_pagamento), end='')    # end='' (não vai fazer nada no final da linha), ele não pula a linha, ficam os 2 prints um depois do outro.
print('A prestaçãp será de R${:.2f}'.format(prestacao))

if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO!')