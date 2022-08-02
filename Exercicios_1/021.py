# Faça um prg que abra e reproduza o áudio de um arquivo MP3.

# Primeiro vamos colocar o arquivo da musica na mesma pasta.

import pygame      # Pygama é utilizado para jogos e musicas e etc

pygame.init()      # inicia o uso da biblioteca do pygame
pygame.mixer.music.load('ex21.mp3')        # Aqui carrega o arquivo. 'ex21.mp3' é o nome do arquivo da musica
pygame.mixer.music.play()                  # Da o play no arquivo
pygame.event.wait()                        # Espera a musica acabar e encerra o programa

