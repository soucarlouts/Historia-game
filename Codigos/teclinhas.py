import pygame
import pygame_menu
import keyboard
import time

pygame.init()

som_letra = pygame.mixer.Sound("Historia-game/som_digitado.mp3")
volume_tecla = 0.2
som_letra.set_volume(volume_tecla)

texto = "olá, mundo!"

def reproduz_som_de_letra(letra):
    if letra.isalpha(): 
        som_letra.play()
    elif letra.isspace(): 
        time.sleep(0.05)

for letra in texto:
    print(letra, end='', flush=True)
    time.sleep(0.05)
    reproduz_som_de_letra(letra)

pygame.quit()

