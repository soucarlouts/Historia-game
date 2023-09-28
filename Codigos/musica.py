import pygame

pygame.init()
pygame.mixer.music.load("C:\Historia-game\Som\drusila_audiogame.mp3")
pygame.mixer.music.play()
input()
pygame.mixer.music.stop()
pygame.quit()