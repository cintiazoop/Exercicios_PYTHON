# Faça um prg que tenha uma TUPLA totalmente preenchida com uma contagem por extenso, de ZERO até VINTE.
# Seu prg deverá ler um número pelo teclado (entre 0 a 20) e mostra-lo por extenso.

lista_numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    numero = int(input('Digite um número entre 0 e 20 -> '))
    if numero <= 20:
        print(f'Vocẽ digitou o número "{lista_numeros[numero]}"!')
        break
    else:
        print('Número digitado diferente de 0 a 20, tente novamente!')

