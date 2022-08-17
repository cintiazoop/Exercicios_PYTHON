# Faça um prg que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


resposta = "S"
somatorio = 0
contador = 0
maior = 0
menor = 0

while resposta in "Ss":
    numero = int(input('Digite um número -> '))
    somatorio = somatorio + numero
    contador = contador + 1
    if contador == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = str(input('Quer continuar? [S/N]'))

media = somatorio / contador                                       # A média não pode ser colocada lá encima, pois a variavél começa com '0' e nao pode ser dividida por 0
print(f'Você digitou {contador} números e a média foi {media}')
print(f'O maior numero digitado foi {maior} e o menor foi {menor}')