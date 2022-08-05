# Faça um prg que leia o peso e a altura da pessoa, calcule seu IMC e mostre seu status de acoro com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

peso = float(input('Qual é seu peso? '))
altura = float(input('Qual é a sua altura? '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc <= 18.5:
    print('Você esta ABAIXO DO PESO normal')
elif imc > 18.5 and imc < 25:
    print('Você esta com PESO IDEAL')
elif imc > 25 and imc < 30:
    print('Você esta com SOBREPESO')
elif imc > 30 and imc < 40:
    print('Você esta com OBESIDADE')
else:
    print('Você esta com OBESIDADE MÓRBIDA')
