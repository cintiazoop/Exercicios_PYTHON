# Faça um prg que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual é o salário do funcionário? R$ '))
novo_salario = salario + (salario * 15 / 100)

print('Um funcionário que recebe R$ {:.2F}, com 15% de aumento, passa a receber R$ {:.2F}'.format(salario, novo_salario))