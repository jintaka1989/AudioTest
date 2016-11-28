#coding:utf-8
import sys
import os
import commands as cmd

import tensorflow as tf
import numpy as np
import scipy
import random
import math
import time
import wave
import pyaudio

import wave
from numpy import *
from pylab import *

# mp3をwavに変換の実行
os.system("ffmpeg -i ./data_set/TS481035.mp3 ./data_set/output.wav")
