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

def serve_pictures(picture):
    plt.show()
    plt.savefig(picture)	
    return static_file(picture, root='/opt/python_panda/')

def read_file():
    return pd.read_csv("USDJPY.csv")
    
def get_redundant_pairs(df):
    '''Get diagonal and lower triangular pairs of correlation matrix'''
    pairs_to_drop = set()
    cols = df.columns
    for i in range(0, df.shape[1]):
        for j in range(0, i+1):
            pairs_to_drop.add((cols[i], cols[j]))
    return pairs_to_drop

def get_top_abs_correlations(df, n=5):
    au_corr = df.corr().abs().unstack()
    labels_to_drop = get_redundant_pairs(df)
    au_corr = au_corr.drop(labels=labels_to_drop).sort_values(ascending=False)
    return au_corr[0:n]

@route('/chart1')
def chart():
    df = read_file()
    df['start'].plot()

    #白紙のキャンバス？を生成
    fig = plt.figure()
    #1行、1列の1個目の図を描くエリアを用意
    ax = fig.add_subplot(1,1,1)
    #dataを用意 xとyの個数は一致しておく必要あり
    x = df['date']
    y = df['start']
    #データをセット（プロット）
    ax.plot(x,y)

    return serve_pictures("image1.png")

@route('/chart2')
def chart():
	df = read_file()
	df['date'['start','high','low','end']].plot(figsize=(8,4), grid=True)
	return serve_pictures("image2.png")

@route('/chart3')
def chart():
    df = read_file()
    df.plot(kind='hist', x='date' , bins=10, figsize=(16,4), alpha=0.5)
    return serve_pictures("image3.png")

@route('/chart4')
def chart():
    df = read_file()
    df.plot(subplots=True, figsize=(6, 6)); plt.legend(loc='best')
    return serve_pictures("image4.png")

@route('/chart5')
def chart():
    df = read_file()
    fig, axes = plt.subplots(nrows=2, ncols=2)
    df['start'].plot(ax=axes[0,0]); axes[0,0].set_title('A')
    df['high'].plot(ax=axes[0,1]); axes[0,1].set_title('B')
    df['low'].plot(ax=axes[1,0]); axes[1,0].set_title('C')
    df['end'].plot(ax=axes[1,1]); axes[1,1].set_title('D')
    return serve_pictures("image5.png")

@route('/chart6')
def chart():
    df = read_file()
    print("Data Frame")
    print(df)
    print()

    print("Correlation Matrix")
    print(df.corr())
    print()

    return serve_pictures("image6.png")

if __name__ == "__main__":
    run(host='0.0.0.0', port=92)