# Faça um prg que mostre a tabuada de vários números, um de cada vez, para cada valor digitado.
# O prg será interrompido quando o número solicitado for negativo.


while True:                                                    # repetição infinita

    numero = int(input('Quer ver qual tabuada? '))

    if numero < 0:                                             # paro a repetição infinita digitando um número negativo
        break
    else:
        for elem in range(1, 11):

            print(f'{numero} x {elem} = {numero * elem}')

print('PROGRAMA ENCERRADO!!!')