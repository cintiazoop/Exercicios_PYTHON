# Faça um prg que converta uma temperatura digitada em °C e converta para °F.

c = float(input('Informe a temperatura em °C -> '))
f = ((9 * c) / 5) + 32      # Conversão de °C para

print('A temperatura de {}ºC corresponde a {}°F!'.format(c, f))