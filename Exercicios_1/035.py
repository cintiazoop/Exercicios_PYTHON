# Faça um prg que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo.

reta_1 = float(input('Primeiro seguimento -> '))
reta_2 = float(input('Segundo seguimento -> '))
reta_3 = float(input('Terceiro seguimento -> '))

if reta_1 < reta_2 + reta_3 and reta_2 < reta_1 + reta_3 and reta_3 < reta_1 + reta_2:      # Cada um dos segmentos tem que ser menor do que a soma do comprimento dos outros 2
    print('Os segmentos acima PODEM FORMAR um triâmgulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triâmgulo!')