# Faça um prg que leia o sexo de uma pessoa, mas só aceite os falores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input("Informe seu sexo [M/F] -> ")).strip().upper()[0]    # strip para retirar os espaços da frente e de tras. upper()[0] passar as letras para MAIUSCULO e pega só a primeir aletra. Ex: masculino (pega só a letra M)

while sexo not in 'FfMm':                                             # vai aceitar F ou f ou M ou m
    print('Tente novamente')
    sexo = str(input("Informe seu sexo -> "))