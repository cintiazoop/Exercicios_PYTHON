# Faça um prg que leia 2 valores e mostre um menu como o abaixo:
# O prg deverá realizar a operação solicitada em cada caso.
# [ 1 ] Somar
# [ 2 ] Multiplicar
# [ 3 ] Maior
# [ 4 ] Novos números
# [ 5 ] Sair do programa


n1 = int(input("Digite o PRIMEIRO número -> "))
n2 = int(input("Digite o SEGUNDO número -> "))
opcao = 0

while opcao != 5:
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa
    ''')

    opcao = int(input("Digite a opção -> "))

    if opcao == 1:
        print(f'A soma dos números {n1} + {n2} é {n1+n2}')

    elif opcao == 2:
        print(f'A multiplicação dos números {n1} x {n2} é {n1 * n2}')

    elif opcao == 3:
        if n1 > n2:
            print(f'O maior número entre {n1} e {n2} é {n1}')
        elif n2 > n1:
            print(f'O maior número entre {n1} e {n2} é {n2}')
        else:
            print(f'Não existe maior número entre {n1} e {n2}, pois eles são iguais!')

    elif opcao == 4:
        n1 = int(input("Informe o primeiro valor -> "))
        n2 = int(input("Informe o segundo valor -> "))
        print(f'Os novos números informados são {n1} e {n2}')

    elif opcao == 5:
        print('FIM!')

    else:
        print('Opção incorreta!')