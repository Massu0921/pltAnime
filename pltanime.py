import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import animation


class Animation():
    '''matplotlibを用いたグラフの動的描画

    Parameters
    ----------
    x_data : list
        x軸のデータのリスト
    y_data : list
        y軸のデータのリスト
    update_freq : int
        グラフの更新間隔[ms] (Default: 10)
    figsize : tuple of int
        グラフのサイズ (Default: (10, 6))

    '''

    def __init__(self, x_data: list, y_data: list, update_freq=10, figsize=(10, 6)):
        self.x_datalist = x_data
        self.y_datalist = y_data
        self.update_freq = update_freq
        self.figsize = figsize

    def animation(self):
        '''アニメーショングラフを表示
        '''
        # 描画領域
        fig = plt.figure(figsize=self.figsize)

        # 描画用データリスト
        x = []
        y = []

        params = {
            'fig': fig,
            'func': self.__update_scatter,
            'fargs': (x, y),
            'interval': self.update_freq,
            'frames': np.arange(0, len(self.x_datalist), 1),
            'repeat': False,
        }
        anime = animation.FuncAnimation(**params)

        # グラフを表示する
        plt.show()

    def __update_scatter(self, frame, x, y):
        # グラフ初期化
        plt.cla()
        # 次のデータを追加
        x.append(self.x_datalist[frame])
        y.append(self.y_datalist[frame])
        # 再描画
        plt.scatter(x, y, s=5, marker="x")
