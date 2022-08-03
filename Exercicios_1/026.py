# Faça um prg que leia um frase e mostre:
# Quantas vezes aparece a letra "A
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

frase = str(input("Digite a frase -> ")).upper().strip()                              # upper vai passar a frase toda para MAIÚSCULO, strip para retirar os espaços da frente e de trás

print("A letra 'A' aparece {} vezes na frase.".format((frase.count('A'))))            # (frase.count('A') conta quanta vezes o A aparece na frase
print("A primeira letra 'A' aparece na posição {}.".format((frase.find('A') + 1)))    # Aqui a frase esta toda em MAIÚSCULO, frase.find('A') busca a primeira vez que aparece "A", + 1 pq o py começa no 0 e mostraria 1 posição a menos, colocando + 1 teremos uma posição correta para nós
print("A última letra 'A' aparece na posição {}.".format((frase.rfind('A') + 1)))     # Aqui a frase esta toda em MAIÚSCULO, frase.rfind('A') busca do final para o inicio (ao contrario) a primeira vez que aparece "A", + 1 pq o py começa no 0 e mostraria 1 posição a menos, colocando + 1 teremos uma posição correta para nós