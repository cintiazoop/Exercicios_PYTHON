# Faça um prg que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão.
# 1 para binário            /     Binário (base 2)              /   0,1,10,11,100,101,110,111,1000
# 2 para octal              /     Octal (base 8)                /   0,1,2,3,4,5,6,7,10,11,12,13,14,15,16,17
# 3 para hexadecimal        /     Hexadecimal (base 16)         /   0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F

numero = int(input('Digite um número inteiro -> '))

print('''Escolha uma das bases para conversão:
[1] - Converte para BINÁRIO
[2] - Converte para OCTAL
[3] - Converte para HEXADECIMAL ''')

opcao = int(input('Digite sua opção -> '))

if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero, bin(numero)[2:]))       # bin(numero) converte automatico o numero p/ binario. [2:] para ñ mostrar no resultado os 2 digitos que aparece na frente do resultado (Ex p/ o numero 10: ob1010)
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:]))         # oct(numero) converte automatico o numero p/ octal. [2:] para ñ mostrar no resultado os 2 digitos que aparece na frente do resultado (Ex p/ o numero 10: 0o12)
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:]))   # hex(numero) converte automatico o numero p/ hexadecimal. [2:] para ñ mostrar no resultado os 2 digitos que aparece na frente do resultado (Ex p/ o numero 10: 0xa)
else:
    print('Opção inválida! Tente novamente')
