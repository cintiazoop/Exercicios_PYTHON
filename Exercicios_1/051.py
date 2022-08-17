# Faça um prg que leia o PRIMEIRO TERMO e a RAZÃO de uma PA.
# No final mostre os 10 primeiros termos dessa progressão (PA - prograssão aritmetica).

primeiro_termo = int(input('Digite o primeiro termo -> '))
razao = int(input('Digite a razão -> '))                               # de quanto em quantos numeros quero pular
decimo_termo = primeiro_termo + (10 - 1) * razao                       # regra matematica para calcular o decimo termo

for elem in range(primeiro_termo, decimo_termo + razao, razao):
    print(f'{elem}', end='->')
print('ACABOU!')


print(decimo_termo)