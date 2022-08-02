# Faça um prg que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas
# Quantas letras ao sem considerar espaços
# Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo -> ')).strip()                          # o strip vai retirar todos os espaçoes existentes antes e depois do nome
print('Analisando seu nome...')
print('Seu nome em maiúsculo é {}'.format(nome.upper()))                           # upper coloca todas as letras em MAIÚSCULO
print('Seu nome em maiúsculo é {}'.format(nome.lower()))                           # lower coloca todas as letras em minúsculo
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))        # len vai contar quantos caracteres total (com espaços), nome.count(' ') vai contar quantos espaços tem
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))                    # (nome.find(' ') para encontrar o primeiro espaço

# OU posso achar o primeiro nome de outra forma

separa_nome = nome.split()        # o split vai jogar dentro de uma lista os nomes inteiros
print('Seu primeiro nome tem {} letras'.format(len(separa_nome[0])))               # (len(separa_nome[0]) conta os caracteres da posição 0