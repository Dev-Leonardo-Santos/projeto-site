import pygame

print('Vamos escutar P do pecado BLZZZ!')

pygame.mixer.init()
pygame.mixer.music.load(r'C:\Users\user\OneDrive\Área de Trabalho\programação\Projeto Spoty fi 2\P do pecado.mp3')
pygame.mixer.music.play(0)

input('pressione ENTER para parar ... ')

pygame.mixer.music.stop()
