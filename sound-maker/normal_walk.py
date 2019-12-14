import pygame.mixer
import time

class NormalWalk():
    
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load('sample_sound/Motion-Pop32-1.mp3')
        
    def play(self):
        pygame.mixer.music.play(1)
        time.sleep(0.5)
        pygame.mixer.music.stop()
            