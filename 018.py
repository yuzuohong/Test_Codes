import time
import pandas as pd
import quandl
import math, datetime
import numpy as np
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

df = quandl.get('WIKI/GOOGL')

df = df[['Adj. Open','Adj. Close','Adj. High','Adj. Low','Adj. Volume']]

df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.00

df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.00

df = df[['Adj. Open', 'Adj. Close', 'HL_PCT', 'PCT_change','Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-9999, inplace=True)

#forecast_out = int(math.ceil(0.0095*len(df)))

df['label'] = df[forecast_col]



X = np.array(df.drop(['label'],1))

X = preprocessing.scale(X)

#X = X[:-forecast_out]

X_lately = X

df.dropna(inplace=True)
y = np.array(df['label'])
y = np.array(df['label'])

#t_size = float(input('Please specify the test size (%):'))

start_time = time.time()

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

#clf = classifier

clf0 = LinearRegression()
clf0.fit(X_train, y_train)


#R2
accuracy0 = clf0.score(X_test, y_test)

#print(accuracy0)

forecast_set = clf0.predict(X_lately)

print(forecast_set, accuracy0)

df['Forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Calendar Date')
plt.ylabel('Stock Price')
plt.title('Google Stock Price Forecast')
plt.show()











