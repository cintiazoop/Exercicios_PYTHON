# Faça um prg que leia 2 notas de um aluno e calcule sua média mostrando um mensagem no final,
# de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

nota_1 = float(input('Digite a PRIMEIRA nota -> '))
nota_2 = float(input('Digite a SEGUNDA nota -> '))
media = (nota_1 + nota_2) / 2

print('A média do aluno com as notas {} e {} é {}'.format(nota_1, nota_2, media))

if media < 5.0:
    print('O aluno esta REPROVADO!')
elif media >= 5.0 and media < 7.0:
    print('O aluno esta em RECUPERAÇÃO!')
else:
    print('O aluno esta APROVADO!')