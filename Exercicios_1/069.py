# Faça um prg que leia a IDADE e o SEXO de várias pessoas.
# A cada pessoa cadastrada, o prg deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.

soma_maior = 0
soma_masculino = 0
soma_mulheres_menos_20 = 0

while True:                                        # Irá repetir sem fim até que algo faça ele parar.
    idade = int(input('Qual é a idade? '))
    sexo = str(input('Qual é a sexo? [F/M] ')).strip().upper()[0]            # strip p/ retirar os espaços da frente e de trás da entrada. upper()[0] coloca tudo em maiusculo e analisa somente a 1ª letra
    if idade > 18:
        soma_maior = soma_maior + 1

    if sexo in "Mm":
        soma_masculino = soma_masculino + 1

    if sexo in "Ff" and idade < 20:
        soma_mulheres_menos_20 = soma_mulheres_menos_20 + 1

    resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]   # strip p/ retirar os espaços da frente e de trás da entrada. upper()[0] coloca tudo em maiusculo e analisa somente a 1ª letra
    if resposta in "Nn":
        break

print(f'Temos {soma_maior} pessoas maiores de 18 anos.')
print(f'Temos {soma_masculino} homens cadastrados.')
print(f'Temos {soma_mulheres_menos_20} mulheres com menos de 20 anos..')