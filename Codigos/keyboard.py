import keyboard
import pygame

pygame.mixer.init()

audio_path = ""
pygame.mixer.music.load(audio_path)

def play_audio(e):
    if e.event_type == keyboard.KEY_DOWN:
        pygame.mixer.music.play()
        
        
keyboard.hook(play_audio)

keyboard.wait("esc")        