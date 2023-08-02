import numpy as np
import pandas as pd
import yfinance as yf
yf.pdr_override()
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

stock = pd.read_csv("stocks.csv")

main_players = ["spy", "ivv", "qqq"]

stock['volume'] = stock['volume'].replace(',', '', regex=True).astype(int)

volume = stock[stock['volume'] > 1000000]

m_health = volume[volume['sector'] == 'Healthcare']
m_tech = volume[volume['sector'] == 'Technology']

healthcare = m_health['ticker'].tolist()
tech = m_tech['ticker'].tolist()

begin = "1980-01-01"



tech = wb.DataReader(tech, data_source='yahoo', start='1995-1-1')['Adj Close']


health = wb.DataReader(healthcare, data_source='yahoo', start='1995-1-1')['Adj Close']


sum_tech = tech.sum(axis = 1)
sum_health = health.sum(axis = 1)


plt.plot(sum_tech.index, sum_tech.values)
plt.plot(sum_health.index, sum_health.values)
plt.yscale('log')
plt.xlabel('date')
plt.ylabel('price')

plt.title('tech and health')

plt.show()


