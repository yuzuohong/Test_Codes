import pandas as pd
import quandl
import math
import numpy as np
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = quandl.get('WIKI/GOOGL')

df = df[['Adj. Open','Adj. Close','Adj. High','Adj. Low','Adj. Volume']]

df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.00

df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.00

df = df[['Adj. Open', 'Adj. Close', 'HL_PCT', 'PCT_change','Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-9999, inplace=True)

forecast_out = int(math.ceil(0.1*len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)

df.dropna(inplace=True)

print(df.tail(30))
