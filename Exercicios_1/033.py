# Faça um prg que leia 3 números e mostre qual é o MAIOR e o MENOR número.

a = int(input('Digite o PRIMEIRO valor -> '))
b = int(input('Digite o SEGUNDO valor -> '))
c = int(input('Digite o TERCEIRO valor -> '))

menor = a

if b < a and b < c:        # Verifica quem é menor
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))