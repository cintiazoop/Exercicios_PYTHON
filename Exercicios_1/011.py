# Faça um prg que leia a largura e a altura de uma parede em metros, calcule a sua área e  quantidade de tinta necessaria
# para pinta-la, sabendo que cada litro de tinta pinta uma area de 2m²

largura = float(input('Digite a largura da parece -> '))
altura = float(input('Digite a altura da parece -> '))
area = largura * altura
qutd_tinta = area / 2

print('Sua parece tem a dimensão de {} x {} e sua área é de {} m²'.format(largura, altura, area))
print('Para pintar essa parede vc precisará de {}l de tinta'.format(qutd_tinta))