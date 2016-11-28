#coding:utf-8
import tensorflow as tf
import numpy as np
import random
import math
import time
import wave
import pyaudio

import wave
from numpy import *
from pylab import *

def printWaveInfo(wf):
    """WAVEファイルの情報を取得"""
    print "チャンネル数:", wf.getnchannels()
    print "サンプル幅:", wf.getsampwidth()
    print "サンプリング周波数:", wf.getframerate()
    print "フレーム数:", wf.getnframes()
    print "パラメータ:", wf.getparams()
    print "長さ（秒）:", float(wf.getnframes()) / wf.getframerate()

if __name__ == '__main__':
    wf = wave.open("./data_set/bird.wav", "r")
    printWaveInfo(wf)

    buffer = wf.readframes(wf.getnframes())
    print len(buffer)  # バイト数 = 1フレーム2バイト x フレーム数

    # bufferはバイナリなので2バイトずつ整数（-32768から32767）にまとめる
    data = frombuffer(buffer, dtype="int16")

    # プロット
    # plot(data)
    # 5周期のみプロット
    # plot(data[0:500])
    # 指定周期のみプロット
    plot(data[100:100*2000])

    show()
