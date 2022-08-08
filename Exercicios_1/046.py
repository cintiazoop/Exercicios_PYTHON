# Faça um prg que mostre na tela uma contagem regressiva para o estouro de fogos de artifício de 10 até 0,
# com uma pausa de 1 segundo entre elas.

from time import sleep                # sleep faz o computadar esperar o tempo que vc definir para dar o resultado (um suspense)

for contagem in range(10, -1, -1):    # ele vai contar de 10 até -1 para pegar o 0, e vai pulanlo -1
    print(contagem)
    sleep(1)                          # Vai aguardar 1 segundos antes de dar o resultado

print('BUM! BUM! POOOW!')