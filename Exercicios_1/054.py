# Faça um prg que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas são maiores.

from datetime import date

atual = date.today().year
total_maior = 0
total_menor = 0

for elem in range(1, 8):                                        # Vai repetir as 7 vezes
    nascimento = int(input('Em que ano a pessoa nasceu? '))
    idade = atual - nascimento

    if idade >= 21:
        total_maior = total_maior + 1
    else:
        total_menor = total_menor + 1

print(f'Ao todo tivemos {total_maior} pessoas maiores de idade')
print(f'Ao todo tivemos {total_menor} pessoas maiores de idade')