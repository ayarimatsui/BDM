# -*- coding: utf-8 -*-
"""
matplotlibで加速度センサの値をリアルタイムプロットする

"""
from __future__ import unicode_literals, print_function

import numpy as np
import matplotlib.pyplot as plt
import smbus
import time

def pause_plot():
    plt.figure(figsize=(10,8))
    plt.subplots_adjust(hspace=1)
    ax1 = plt.subplot(311)
    ax2 = plt.subplot(312)
    ax3 = plt.subplot(313)
    x = [-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0] #はじめに表示されるｘ軸の範囲の設定
    y_x = [0,0,0,0,0,0,0,0,0,0] #加速度センサのx軸の値の初期値
    y_y = [0,0,0,0,0,0,0,0,0,0] #加速度センサのy軸の値の初期値
    y_z = [0,0,0,0,0,0,0,0,0,0] #加速度センサのz軸の値の初期値
    ax1.set_xlim(-1, 0)
    ax1.set_ylim(-1, 1)
    ax2.set_xlim(-1, 0)
    ax2.set_ylim(-1, 1)
    ax3.set_xlim(-1, 0)
    ax2.set_ylim(-1, 1)
    # 初期化的に一度plotしなければならない
    # そのときplotしたオブジェクトを受け取る受け取る必要がある．
    # listが返ってくるので，注意
    lines1, = ax1.plot(x, y_x, color="red")
    ax1.set_title("acceleration x-axis")
    
    lines2, = ax2.plot(x, y_y, color="blue")
    ax2.set_title("acceleration y-axis")
    
    lines3, = ax3.plot(x, y_z, color="green")
    ax3.set_title("acceleration z-axis")
    
    I2C_ADDR=0x1C

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
    

    # ここから無限にplotする
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

        #ｘ軸の更新
        x = map(lambda p: p+0.1, x)
        
        #加速度センサｘ軸の値の更新
        y_x.pop(0)
        y_x.append(xAccl)
        
        #グラフをプロットし直す
        lines1.set_data(x, y_x)
        ax1.set_xlim(min(x), max(x))
        ax1.set_ylim(min(y_x)-10, max(y_x)+10)


        #加速度センサy軸の値の更新
        y_y.pop(0)
        y_y.append(yAccl)
        
        #グラフをプロットし直す
        lines2.set_data(x, y_y)
        ax2.set_xlim(min(x), max(x))
        ax2.set_ylim(min(y_y)-10, max(y_y)+10)

        
        #加速度センサz軸の値の更新
        y_z.pop(0)
        y_z.append(zAccl)
        
        #グラフをプロットし直す
        lines3.set_data(x, y_z)
        ax3.set_xlim(min(x), max(x))
        ax3.set_ylim(min(y_z)-10, max(y_z)+10)
        

        # 一番のポイント
        # - plt.show() ブロッキングされてリアルタイムに描写できない
        # - plt.ion() + plt.draw() グラフウインドウが固まってプログラムが止まるから使えない
        # ----> plt.pause(interval) これを使う!!! 引数はsleep時間
        time.sleep(0.1) #この値によって、何秒に１回センサの値を取得するかが変わる　今は10Hz
        plt.pause(.01)

if __name__ == "__main__":
    pause_plot()