# Faça um prg que calcule a soma entre os números impares que são multiplos de 3 e que se encontram no internalo de 1 até 500.

soma = 0
contador = 0
for numero in range(1, 501, 2):                 # já começa no 2 (par), vai ate o 51 para mostrar ate o 50, e vai pulando de 2 em 2
        if numero % 3 == 0:
                print(numero, end=' ')         # end=' ' deixa os numeros um ao lado do outro, senao colocar o end ficara um embaixo do outro.
                contador = contador + 1        # contador soma +1 (aqui vai contar quantos numeros foram encontrados)
                soma = soma + numero           # acumulador soma os valores (aqui vai somar todos os valores)
print('Acabou!')
print(f'A soma de todos os {contador} encontrados entre os números 1 e 500 que são multiplos de três é {soma}.')