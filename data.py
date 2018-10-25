from bottle import route, run, template, request, static_file
# from bottle import post, get, put, delete, request, response
from bottledaemon import daemon_run
import pandas as pd
import numpy as np
from pandas import *
from pylab import *
import matplotlib.pyplot as plt
from numpy.random import randn
import matplotlib.dates as mdates

# @route('/picture/<picture>')
def serve_pictures(picture):
    return static_file(picture, root='/opt/api/data/')

# def select_col(df):
#     #白紙のキャンバス？を生成
#     fig = plt.figure()
#     #1行、1列の1個目の図を描くエリアを用意
#     ax = fig.add_subplot(1,1,1)
#     #dataを用意 xとyの個数は一致しておく必要あり
#     x = df['day']
#     y = df['start_point']
#     #データをセット（プロット）
#     ax.plot(x,y)
#     return df

@route('/chart1')
def chart():
    df = pd.read_csv("/opt/api/data/01_USDJPY_D.csv")
    df['start_point'].plot()
    # df = select_col(df)

    #白紙のキャンバス？を生成
    fig = plt.figure()
    #1行、1列の1個目の図を描くエリアを用意
    ax = fig.add_subplot(1,1,1)
    #dataを用意 xとyの個数は一致しておく必要あり
    x = df['day']
    y = df['start_point']
    #データをセット（プロット）
    ax.plot(x,y)


    plt.show()
    plt.savefig("image.png")
    return serve_pictures("image.png")

@route('/chart2')
def chart():
	df = pd.read_csv("/opt/api/data/01_USDJPY_D.csv")
	df['day'['start_point','high_point','low_point','end_point']].plot(figsize=(8,4), grid=True)
	plt.show()
	plt.savefig("image2.png")
	return serve_pictures("image2.png")

@route('/chart3')
def chart():
    df = pd.read_csv("/opt/api/data/01_USDJPY_D.csv")
    df.plot(kind='hist', x='day' , bins=10, figsize=(16,4), alpha=0.5)
    # df = select_col(df)
    plt.show()
    plt.savefig("image3.png")
    return serve_pictures("image3.png")

@route('/chart4')
def chart():
    df = pd.read_csv("/opt/api/data/01_USDJPY_D.csv")
    df.plot(subplots=True, figsize=(6, 6)); plt.legend(loc='best')
    # df = select_col(df)
    plt.show()
    plt.savefig("image4.png")
    return serve_pictures("image4.png")

@route('/chart5')
def chart():
    df = pd.read_csv("/opt/api/data/01_USDJPY_D.csv")
    fig, axes = plt.subplots(nrows=2, ncols=2)
    df['start_point'].plot(ax=axes[0,0]); axes[0,0].set_title('A')
    df['high_point'].plot(ax=axes[0,1]); axes[0,1].set_title('B')
    df['low_point'].plot(ax=axes[1,0]); axes[1,0].set_title('C')
    df['end_point'].plot(ax=axes[1,1]); axes[1,1].set_title('D')
    # df = select_col(df)
    plt.show()
    plt.savefig("image5.png")
    return serve_pictures("image5.png")

if __name__ == "__main__":
    run(host='0.0.0.0', port=80)