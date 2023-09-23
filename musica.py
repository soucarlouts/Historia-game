import pygame

pygame.init()
pygame.mixer.music.load("Black Sabbath - Electric Funeral.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pass

pygame.quit()