import pandas as pd
import numpy as np
import matplotlib as plt
from matplotlib.pylab import rcParams

plt.style.use("fivethirtyeight")

from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense
from sklearn.preprocessing import MinMaxScaler

rcParams["figure.figsize"] = 20, 10


dataset = pd.read_csv("stock_data.csv")
# dataset.head()
print(dataset)

# dataset["date"] = dataset.to_datetime(df.Date, format="%Y-%m-%d")
