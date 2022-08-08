# Faça um prg que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.


for numero in range(1, 51):
    if numero % 2 == 0:                        # Verifica se o numero é par (se numero for divisivel por 2 com o resto 0)
        print(numero, end=' ')                 # end=' ' deixa os numeros um ao lado do outro, senao colocar o end ficara um embaixo do outro.

print('Acabou!')


# OU

for numero in range(2, 51, 2):                 # já começa no 2 (par), vai ate o 51 para mostrar ate o 50, e vai pulando de 2 em 2
        print(numero, end=' ')                 # end=' ' deixa os numeros um ao lado do outro, senao colocar o end ficara um embaixo do outro.

print('Acabou!')