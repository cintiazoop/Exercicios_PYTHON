# Faça um prg que leia um ano qualquer e mostre se ele é BISSEXTO


from datetime import date
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual! '))

if ano == 0:
    ano = date.today().year                             # date.today() vai pegar a data de hoje, year (só o ano)

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:   # todos os anos múltiplos de 4 que também não são múltiplos de 100, com exceção dos múltiplos de 400, deverão ser anos bissextos.
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))