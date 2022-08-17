# Melhore o EXERCICIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O prg encerra quando ele disser que quer mostrar '0' termos.


primeiro_termo = int(input('Digite o primeiro termo -> '))
razao = int(input('Digite a razão -> '))                               # de quanto em quantos numeros quero pular
termo = primeiro_termo
contador = 1

total = 0
mais = 10

while mais != 0:
    total = total + mais
    while contador <= total:
        print(f'{termo} ->', end='')
        termo = termo + razao
        contador = contador + 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais?  '))
print('Programa finalizado!')