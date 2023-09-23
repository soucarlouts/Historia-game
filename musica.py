import pygame

pygame.init()
pygame.mixer.music.load("Black Sabbath - Electric Funeral.mp3")

pygame.mixer.music.play()

input("pressione enter para para a musica . . . ")

pygame.mixer.music.stop()

pygame.quit()