# Crie um prg que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ela.

algo = input('Digite algo -> ')
print('O tipo primitivo de algo é ', type(algo))        # Verifica o tipo de algo


print('Algo é só espaço? ', algo.isspace())             # Verifica se algo SÓ tem espaços, se esta vazio. (True ou False)

print('Algo é um numero?', algo.isnumeric())            # Verifica se algo SÓ tem numeros. (True ou False)

print('Algo é uma letra?', algo.isalpha())              # Verifica se algo SÓ tem letras. (True ou False)

print('Algo é uma letra e numero?', algo.isalnum())     # Verifica se algo tem letras e numeros. (True ou False)

print('Algo esta tudo em maiusculo?', algo.isupper())    # Verifica se algo esta tudo em MAIUSCULO. (True ou False)

print('Algo esta tudo em minusculo?', algo.islower())    # Verifica se algo esta tudo em minusculo. (True ou False)

print('Algo esta capitalizada?', algo.istitle())         # Verifica se algo esta com cada palavra iniciando com letra maiuscula (True ou False)

