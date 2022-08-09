# Crie um prg que leia as 2 notas de um aluno, calcule e mostre a média.

nota_1 = float(input('Digite a primeira nota - > '))
nota_2 = float(input('Digite a segunda nota - > '))
media = (nota_1 + nota_2) / 2

print('A média das notas {:.1f} e {:.1f} é -> {:.1f} '. format(nota_1, nota_2, media))      # {:.1f} depois do ponto usar 1 casa decimal

# OU

print(f'A média das notas {nota_1} e {nota_2} é -> {media}')                                # usando F-string