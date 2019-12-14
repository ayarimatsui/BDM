import pygame.mixer
import time

class Kick():
    
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load('sample_sound/byui-n.mp3')
        
    def play(self):
        pygame.mixer.music.play(1)
        time.sleep(1.5)
        pygame.mixer.music.stop()
