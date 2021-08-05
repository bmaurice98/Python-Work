import pandas as pd
import numpy as np
import matplotlib as plt
from matplotlib.pylab import rcParams
from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense
from sklearn.preprocessing import MinMaxScaler

dataset = pd.read_csv("stock_data.csv")
dataset.head()
