# Faça um prg que leia o peso de cinco pessoas. No final mostre qual foi o maior e o menor peso lido

menor_peso = 0
maior_peso = 0

for pessoa in range(1, 6):
    peso = float(input(f'Peso da {pessoa}ª pessoa-> '))
    if pessoa == 1:            # quer dizer que ela é a primeira pessoa
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

print(f'O maior peso lido foi de {maior_peso}')
print(f'O menor peso lido foi de {menor_peso}')

