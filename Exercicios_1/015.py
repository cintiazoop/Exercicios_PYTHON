# Faça um prg que pergunte a quantidade de KM percorrido por um carro alugado e a quantidade de dias pelas quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado.

dias = int(input('Quantos dias alugados -> '))
km = float(input('Quantos km rodados -> '))
pago_diaria = (dias * 60) + (km * 0.15)     # Valor das diarias + valor dos kms

print('O total a pagar é de R${:.2f}'.format(pago_diaria))
