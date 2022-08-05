# Faça um prg que leia o ano de nascimento de um atetla e mostre sua categoria de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 25 anos: SÊNIOR
# Acima: MASTER

from datetime import date

ano_atual = date.today().year        # date.today() vai pegar a data de hoje, year (só o ano)
ano_nasc = int(input('Qual o ano de nascimento? '))

idade = ano_atual - ano_nasc

if idade <= 9:
    print('Atleta MIRIM!')
elif idade > 9 and idade < 15:
    print('Atleta INFANTIL')
elif idade > 15 and idade < 20:
    print('Atleta JUNIOR')
elif idade > 20 and idade < 26:
    print('Atleta SÊNIOR')
else:
    print('Atleta MASTER')