import pygame

pygame.init()
pygame.mixer.music.load("drusila_audiogame.mp3")

pygame.mixer.music.play()

input("pressione enter para para a musica . . . ")

pygame.mixer.music.stop()

pygame.quit()