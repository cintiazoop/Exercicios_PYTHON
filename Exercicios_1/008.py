# Crie um prg que leia um valor em metros e exiba convertido em centimetros e milimetros

medida = float(input('Digite uma distancia em metros -> '))
cm = medida * 100
mm = medida * 1000

print('A média de {} metro corresponde a {} centimetros e {} milimetro'. format(medida, cm, mm))              # {:.1f} depois do ponto usar 0 casa decimal

# OU

print('A média de {} metro corresponde a {:.0f} centimetros e {:.0f} milimetro'. format(medida, cm, mm))      # {:.1f} depois do ponto usar 0 casa decimal