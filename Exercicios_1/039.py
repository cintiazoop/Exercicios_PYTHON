# Faça um prg que leia o ano de nascimento de um jovem e informe de acordo com sua idade se ele AINDA VAI SE ALISTAR ao
# serviço militar, se é a HORA DE SE ALISTAR ou se já PASSOU DO TEMPO de alistamento.
# Seu prg também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_atual = ano = date.today().year               # date.today() vai pegar a data de hoje, year (só o ano)
ano_nasc = int(input('Qual o ano do seu nascimento -> '))
idade_atual = ano_atual - ano_nasc

print('Quem nasceu em {} tem {} em {}.'.format(ano_nasc, idade_atual, ano_atual))
if idade_atual == 18:
    print('Hora de se alistar!')
elif idade_atual < 18:
    saldo = 18 - idade_atual                     # Para saber quantos anos faltam
    ano_alistamento = ano_atual + saldo          # Para saber qual o ano do alistamento
    print('Ainda vai se alistar! Faltam {} anos para o alistamento. Seu alistamento será em {}'.format(saldo, ano_alistamento))
else:
    saldo = idade_atual - 18                     # Para saber quantos anos passou do prazo
    ano_alistamento = ano_atual - saldo          # Para saber qual o ano do alistamento
    print('Já passou o tempo de se alistar! Deveria ter se alistado a {} anos, em {}'.format(saldo, ano_alistamento))
