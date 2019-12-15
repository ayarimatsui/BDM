import pygame
import time

        
if __name__=="__main__":
    pygame.init()
    s=pygame.mixer.Sound('/home/pi/BDM/sound_maker/sample_sound/Motion-Pop32-1.ogg')
    for i in range(5):
        s.play()
        print(i)
            