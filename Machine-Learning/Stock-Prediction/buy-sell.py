import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("fivethirtyeight")
from datetime import datetime

FB = pd.read_csv("/Users/mizu/Python-Work/Machine-Learning/Stock-Prediction/FB.csv")

# 30 day simple moving average
A30 = pd.DataFrame()
A30["Close"] = FB["Close"].rolling(window=30).mean()

# Long term average 100days
A100 = pd.DataFrame()
A100["Close"] = FB["Close"].rolling(window=100).mean()

# Graphing Data
plt.figure(figsize=(12.5, 4.5))
plt.plot(FB["Close"], label="FB")
plt.plot(A30["Close"], label="FB")
plt.plot(A100["Close"], label="FB")
plt.title("Facebook Close Price History")
plt.xlabel("July-2012 to Nov-2018")
plt.ylabel("Close Price USD ($)")
plt.show

# New data frame for storing all data
data = pd.DataFrame()
data["FB"] = FB["Close"]
data["A30"] = A30["Close"]
data["A100"] = A100["Close"]

# function for signaling buying and selling
def Buy_Sell(data):
    sigPriceBuy = []
    sigPriceSell = []
    flag = -1

    for i in range(len(data)):
        if data["A30"][i] > data["A100"][i]:
            if flag != 1:
                sigPriceBuy.append(data["FB"][i])
                sigPriceSell.append(np.nan)
                flag = 1
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        elif data["A30"][i] < data["A100"][i]:
            if flag != 0:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(data["FB"][i])
                flag = 0
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        else:
            sigPriceBuy.append(np.nan)
            sigPriceSell.append(np.nan)
    return (sigPriceBuy, sigPriceSell)


# Store buy and sell data
buy_sell = Buy_Sell(data)
data["Buy_Signal_Price"] = buy_sell[0]
data["Sell_Signal_Price"] = buy_sell[1]

# Graph buy and sell algorithm
plt.figure(figsize=(12.6, 4.6))
plt.plot(data["FB"], label="FB", alpha=0.35)
plt.plot(data["A30"], label="A30", alpha=0.35)
plt.plot(data["A100"], label="A100", alpha=0.35)
plt.scatter(
    data.index, data["Buy_Signal_Price"], label="Buy", marker="^", color="green"
)
plt.scatter(
    data.index, data["Sell_Signal_Price"], label="Sell", marker="^", color="purple"
)
plt.title("Facebook Close Price History Buy & Sell Signals")
plt.xlabel("July-2012 to Nov-2018")
plt.ylabel("Close Price USD ($)")
plt.legend(loc="lower left")
plt.show()
