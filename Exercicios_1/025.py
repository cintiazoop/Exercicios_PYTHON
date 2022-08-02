# Faça um prg que leia um nome e diga se ela tem "Silva" no nome.

nome = str(input("Digite seu nome completo -> ")).strip()           # strip para retirar os espaços da frente e de trás

print("Seu nome tem 'SILVA'? {}".format('silva' in nome.lower()))   # in nome (verifica se "silva" esta em nome), lower coloca todas as letras em minúsculo
