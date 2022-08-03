# Faça um prg que leia o nome completo de uma pessoa e mostre o primeiro w o ultimo nome separadamente.
# Ex: Ana Maria de Souza
# primeiro = Ana
# ultimo = Souza

n = str(input('Digite seu nome completo -> ')).strip()       # strip para retirar os espaços da frente e de trás
nome = n.split()                                             # o split vai jogar dentro de uma lista cada pedaço do nome
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))              # nome[0] pega a primeira posição da lista
print('Seu último nome é {}'.format(nome[-1]))               # nome[-1] pega a última posição da lista
