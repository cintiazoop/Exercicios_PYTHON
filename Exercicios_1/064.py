# Faça um prg que leia vários números inteiros pelo teclado.
# O prg só vai parar quando o usuário digitar o valor 999, que á a condição de parada.
# No final,mostre quatos números foram digitados e qual foi a soma entre eles (desconsiderando o 999)


# Nesse caso é sem colocar o - 999. Colocando o n no final do while. Nesse caso o somatorio não recebe o 999(correto).
n = int(input('Digite um número -> '))
somatorio = 0
contador = 0
while n != 999:
    contador = contador + 1
    somatorio = somatorio + n
    n = int(input('Digite um número -> '))      # While no final

print(f'Foram digitados {contador} números. O somatórios de todos os números foi {somatorio}.')


# OU

# Nesse caso é com o - 999 (no print final). Colocando o n no inicio do while. Nesse casso o somatorio recebe o 999.
n = int(input('Digite um número -> '))
somatorio = n
contador = 0
while n != 999:
    n = int(input('Digite um número -> '))
    contador = contador + 1
    somatorio = somatorio + n


print(f'Foram digitados {contador} números. O somatórios de todos os números foi {somatorio - 999}.')        # - 999
