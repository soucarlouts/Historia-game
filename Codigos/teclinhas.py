import keyboard
import pygame
import threading

# Função para reproduzir o áudio em segundo plano
def play_audio():
    pygame.mixer.init()
    audio_path = "C:\Historia-game\Som\som-teclas.mp3"
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()
    pygame.event.wait()

# Iniciar a reprodução de áudio em uma thread separada
audio_thread = threading.Thread(target=play_audio)
audio_thread.start()
print("heeeeeeeelllllllllloooooooooooo world")

# Aguardar a tecla "Esc" no programa principal
keyboard.wait("esc")

# Aguardar a conclusão da thread de áudio
audio_thread.join()

