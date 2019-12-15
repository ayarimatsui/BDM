import pygame.mixer
import time

class SlowWalk():
    
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load('/home/pi/BDM/sound_maker/sample_sound/zun.mp3')
        
    def play(self):
        pygame.mixer.music.play(1)
        time.sleep(0.3)
        pygame.mixer.music.stop()
 