# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um prg que ajude lendo o nome deles e escreva o nome do escolhido.

from random import choice   # random biblioteca p/ gerar aleatoriamente um número inteiro dentro de um intervalo. Choice função q retorna um elemento selecionado aleatoriamente da sequência especificada.

nome_1 = str(input("Digite o PRIMEIRO aluno -> "))
nome_2 = str(input("Digite o SEGUNDO aluno -> "))
nome_3 = str(input("Digite o TERCEIRO aluno -> "))
nome_4 = str(input("Digite o QUARTO aluno -> "))

lista_alunos = [nome_1, nome_2, nome_3, nome_4]

aluno_escolhido = choice(lista_alunos)         # Sorteio aleatorio um aluno

print('O aluno escolhido foi {}'.format(aluno_escolhido))

