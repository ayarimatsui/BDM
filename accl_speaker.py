# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

import numpy as np
import matplotlib.pyplot as plt
import smbus
import time
import math
import pygame

get_time=[]


I2C_ADDR=0x1C #センサが入力されている場所の設定　場所は、i2cdetect -y 1 で確認

# Get I2C bus
bus = smbus.SMBus(1)

# Select Control register, 0x2A(42)
#               0x00(00)        StandBy mode
bus.write_byte_data(I2C_ADDR, 0x2A, 0x00)

# Select Control register, 0x2A(42)
#               0x01(01)        Active mode
bus.write_byte_data(I2C_ADDR, 0x2A, 0x01)

# Select Configuration register, 0x0E(14)
#               0x00(00)        Set range to +/- 2g
bus.write_byte_data(I2C_ADDR, 0x0E, 0x00)

time.sleep(0.5)

pygame.init()

normal_walk=pygame.mixer.Sound('/home/pi/BDM/sound_maker/sample_sound/Motion-Pop32-1.ogg')
slow_walk=pygame.mixer.Sound('/home/pi/BDM/sound_maker/sample_sound/zun.ogg')
fast_walk=pygame.mixer.Sound('/home/pi/BDM/sound_maker/sample_sound/tetetete.ogg')
kick=pygame.mixer.Sound('/home/pi/BDM/sound_maker/sample_sound/byui-n.ogg')

print("init")

while True:
        #加速度センサのデータを代入
        data = bus.read_i2c_block_data(I2C_ADDR, 0x00, 7)
        xAccl = (data[1] * 256 + data[2]) / 16
        if xAccl > 2047 :
            xAccl -= 4096
        yAccl = (data[3] * 256 + data[4]) / 16
        if yAccl > 2047 :
            yAccl -= 4096
        zAccl = (data[5] * 256 + data[6]) / 16
        if zAccl > 2047 :
            zAccl -= 4096
            
        w = math.sqrt(xAccl**2 + yAccl**2 + zAccl**2) #加速度の大きさ
        
        if xAccl<=-1500 and yAccl>=1500:
            current_time=time.time()
            get_time.append(current_time)
            
            if len(get_time)>=2:
                if get_time[-1]-get_time[-2]>1.5: #slow walk
                    slow_walk.play()
                    time.sleep(0.3)
                elif get_time[-1]-get_time[-2]>0.7 and get_time[-1]-get_time[-2]<=1.5: #nomal walk
                    normal_walk.play()
                    time.sleep(0.3)
                else: #fast walk
                    fast_walk.play()
                    time.sleep(0.2)
                    
        elif xAccl>=1400 and yAccl>=1400: #kick
            kick.play()
            time.sleep(1.5)
            
        time.sleep(0.01)
