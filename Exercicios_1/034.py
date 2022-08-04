# Faça um prg que pergunte o salário de um funcionario e calcule o valor do seu aumento.
# Para salarios superiores a R$1.250,00 calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Qual é o salário do funcionario? R$ '))

if salario <= 1250:
    novo_salario = (salario * 15 / 100) + salario
else:
    novo_salario = (salario * 10 / 100) + salario

print('Quem ganhava R${:.2f} pass a ganhar R${:.2f}'.format(salario, novo_salario))
