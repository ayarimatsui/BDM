# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

import numpy as np
import matplotlib.pyplot as plt
import smbus
import time
import math
import pygame.mixer

I2C_ADDR=0x1D #センサが入力されている場所の設定　場所は、i2cdetect -y 1 で確認

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
        
        if yAccl>=1500:
            pygame.mixer.init()
            pygame.mixer.music.load('sound-maker/sample_sound/Motion-Pop32-1.mp3')
            pygame.mixer.music.play(1) # ()内は再生回数 -1:ループ再生
            time.sleep(0.5)
            pygame.mixer.music.stop() # 再生の終了
            
        time.sleep(0.01)