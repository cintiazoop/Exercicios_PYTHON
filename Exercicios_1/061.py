# Refaça o EXERCICIO 051, lendo o primeiro term e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando while.


# ESTE É O E EXERCICIO 051 UTILIFANDO O FOR
primeiro_termo = int(input('Digite o primeiro termo -> '))
razao = int(input('Digite a razão -> '))                               # de quanto em quantos numeros quero pular
decimo_termo = primeiro_termo + (10 - 1) * razao                       # regra matematica para calcular o decimo termo

for elem in range(primeiro_termo, decimo_termo + razao, razao):
    print(f'{elem}', end='-> ')
print('ACABOU!')


# ESTE É O E EXERCICIO 061 UTILIFANDO O WHILE

print('--------------------------------------------------------------')
print('--------------------------------------------------------------')

termo = primeiro_termo
contador = 1

while contador <= 10:
    print(f'{termo} ->', end='')
    termo = termo + razao
    contador = contador + 1
print('ACABOU!')
