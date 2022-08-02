# Faça um prg que leia o nome da cidade e diga se ela começa ou não com o nome "SANTO"

cidade = str(input("Em que cidade você nasceu? ")).strip()  # strip para retirar os espaços da frente e de trás

print(cidade[:5].upper() == 'SANTO')                       # cidade[:5] ele vai contar até o item 5 buscando SANTO, upper (ele vai colocar tudo em maiúsculo e depois comparar com "SANTOS"