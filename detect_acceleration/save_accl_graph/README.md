＊＊save_accl_graph.py＊＊

グラフをリアルタイムに表示しようとすると、グラフの更新頻度を1秒以上にしなければ
グラフの描画が追いつかず、処理が間に合わなかったので、リアルタイムでのグラフの表示はやめ、
プログラム終了時に、それまでに取得したデータをプロットしたグラフをgraphsディレクトリの中に
保存するようにしました。今回の場合は、0.01秒の頻度でセンサの値を取得しています。

＜手順＞
python3で、save_accl_graph.pyを実行
　↓
十分にデータが取れたと思ったら、Ctrl+cを押して、データの取得を終了
　↓
コマンドラインに次のように、最大値、最小値などが出力される
![sample1](https://github.com/ayarimatsui/BDM/blob/master/detect_acceleration/save_accl_graph/sample_images/sample1.png)

　↓
graphsディレクトリにグラフが保存される
![accl_graph](https://github.com/ayarimatsui/BDM/blob/master/detect_acceleration/save_accl_graph/sample_images/accl_graph.png)
