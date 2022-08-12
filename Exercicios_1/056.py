# Faça um prg que leia o nome, idade e sexo de 4 pessoas.
# No final mostre:
# - a media de idade do grupo
# - qual é o nome do homem mais velho
# - quantas mulheres tem menos de 20 anos

total_idades = 0
media_idades = 0
maior_idade_homem = 0
nome_mais_velho = ''
qtd_muleres_20 = 0

for pessoa in range(1, 5):
    nome = str(input('Nome ->')).strip()
    idade = int(input('Ídade -> '))
    sexo = str(input('Sexo [M/F] -> ')).strip()
    total_idades = total_idades + idade

    if idade > maior_idade_homem and sexo == "m":
        maior_idade_homem = idade
        nome_mais_velho = nome

    if sexo == "f" and idade > 20:
        qtd_muleres_20 = qtd_muleres_20 + 1


media_idades = total_idades / 4


print(f'A média de idades do grupo é de {media_idades} anos')
print(f'O homem mais velho é o {nome_mais_velho} e ele tem {maior_idade_homem} anos')
print(f'Existem {qtd_muleres_20} mulheres com mais de 20 anos')