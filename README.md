# BDM(電子情報機器学)

"DisShoes"

![DisShoes_image](https://github.com/ayarimatsui/BDM/blob/master/IMG_1942.JPG)

歩くことが楽しくなるような靴"DisShoes"を製作しました。
靴に取り付けた3軸加速度センサーの値をリアルタイムで取得し、その値から足の動きを判定し、動きの種類に応じて、靴に取り付けられたLEDテープの光り方や音が変わるようにしています。処理は、RaspberryPi3 Model Bで行なっています。実際に動いている様子は次の動画から見ることができます。

https://www.youtube.com/watch?v=m2iPEg8bOUQ&feature=youtu.be


***
プログラムの実行の仕方は、以下の通りです。

＊実行するメインファイル
BDM/accl_led_speaker.py

sudo python accl_led_speaker.py

で実行(python3ではなくpython2系で無いと実行できないと思います)


***
加速度センサーの値から足の動きを判定する閾値の決め方ですが、BDM/detect_acceleration/save_accl_graph/save_accl_graph.pyを実行すると、BDM/detect_acceleration/save_accl_graph/graphsにプログラムを実行していた間の加速度の値のグラフが保存されるので、その値を元に閾値を適当に定め、そこから調整を繰り返し、決定しました。このグラフを描くプログラムについてはこちらで詳しく説明しています。https://github.com/ayarimatsui/BDM/blob/master/detect_acceleration/save_accl_graph/README.md



Created a pair of shoes, "DisShoes", which could change your walk into a fun activity.
By analyzing the values gotten from the acceleration sensor, distinguishes the kinds of movement, (such as whether the person walks, walks slowly, fast, or turn). The colors of the LED lights and the sound from the speaker, both attached to the shoes, changes depend on the movements. I used RaspberryPi3 Model B to get the sensor values and to control the LED lights and the sound. Here, you can get access to the demo video.

https://www.youtube.com/watch?v=m2iPEg8bOUQ&feature=youtu.be


*****
This is how to run the main program.

*main programfile*
BDM/accl_led_speaker.py

sudo python accl_led_speaker.py

(be able to run maybe only by python2, not by python3)


***
About how to decide the threshold of the values of acceleration
run BDM/detect_acceleration/save_accl_graph/save_accl_graph.py. A graph of acceleraion values during the time the previous program runs will be saved in BDM/detect_acceleration/save_accl_graph/graphs. Based on the graphs, I deceided the thresholds.
For more detail, please check https://github.com/ayarimatsui/BDM/blob/master/detect_acceleration/save_accl_graph/README.md.
