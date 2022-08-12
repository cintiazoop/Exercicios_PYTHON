# Faça um prg que leia um frase qualquer e diga se ela é um palindrome, desconsiderando os espaços.

# Palíndromos são palavras ou frases que podem ser lidas da esquerda para a direita ou da direita para a esquerda.
# Ex: Ana
# apos a sopa

frase = str(input('Digite uma frese: ')).strip().upper()      # o strip vai retirar todos os espaçoes existentes antes e depois do nome, upper vai colocar todas as letras em maiusculo
palavras = frase.split()                                      # o split divide uma string em uma lista.
junto = ''.join(palavras)                                     # o join vai unir as palavras separendo pelo item '' (sem espaço)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):                   # vai da última até a primeira, len(junto)-1 é o total - 1, Ex: se o total é 10, começo a contar do 0 ate 9 (-1 de tras pra frente), -1 é o final, -1 ele vai andar de
    inverso = inverso + junto[letra]

if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é palíndromo!')