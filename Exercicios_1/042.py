# Faça um prg que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo.
# Mostre que tipo de triângulo será formado.
# EQUILÁTERO: Todos os lados iguais
# ISÓSCELES: 2 lados iguais
# ESCALENO: Todos os lados diferentes

reta_1 = float(input('Primeiro seguimento -> '))
reta_2 = float(input('Segundo seguimento -> '))
reta_3 = float(input('Terceiro seguimento -> '))

if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2:      # Cada um dos segmentos tem que ser menor do que a soma do comprimento dos outros 2
    print('Os segmentos acima PODEM FORMAR um triâmgulo! ', end='')                         # end='' junta o proximo print sem pular a linha
    if reta_1 == reta_2 and reta_2 == reta_3:
        print('EQUILÁTERO!')
    elif reta_1 != reta_2 and reta_2 != reta_3 and reta_3 != reta_1:
        print('ESCALENO!')
    else:
        print('ISOSCELES!')

else:
    print('Os segmentos acima NÃO PODEM FORMAR um triâmgulo!')