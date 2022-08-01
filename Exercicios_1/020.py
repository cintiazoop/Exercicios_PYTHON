# O mesmo professor do exercicio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um prg que leia o nome dos 4 alunos e mostre qa ordem sorteada.


from random import shuffle   # random biblioteca p/ gerar aleatoriamente um número inteiro dentro de um intervalo. Shuffe, função que embaralha a "lista_alunos"

nome_1 = str(input("Digite o PRIMEIRO aluno -> "))
nome_2 = str(input("Digite o SEGUNDO aluno -> "))
nome_3 = str(input("Digite o TERCEIRO aluno -> "))
nome_4 = str(input("Digite o QUARTO aluno -> "))

lista_alunos = [nome_1, nome_2, nome_3, nome_4]

shuffle(lista_alunos)         # shuffle embaralha a "lista_alunos"

print('A ordem de apresentação será:')
print(lista_alunos)
