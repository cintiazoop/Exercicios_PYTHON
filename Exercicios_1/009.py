# Crie um prg que leia um número inteiro e mostre a sua tabuada.

numero = int(input('Digite um número -> '))

print('{} x 1 =  {}'.format(numero, (numero * 1)))
print('{} x 2 =  {}'.format(numero, (numero * 2)))
print('{} x 3 =  {}'.format(numero, (numero * 3)))
print('{} x 4 =  {}'.format(numero, (numero * 4)))
print('{} x 5 =  {}'.format(numero, (numero * 5)))
print('{} x 6 =  {}'.format(numero, (numero * 6)))
print('{} x 7 =  {}'.format(numero, (numero * 7)))
print('{} x 8 =  {}'.format(numero, (numero * 8)))
print('{} x 9 =  {}'.format(numero, (numero * 9)))
print('{} x 10 = {}'.format(numero, (numero * 10)))
print('-------------------------------------------')

# OU

numero = int(input('Digite um número -> '))

for elem in range(0, 11):

    print(f'{numero} x {elem} = {numero * elem}')




