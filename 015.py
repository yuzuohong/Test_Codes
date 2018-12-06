import time
import pandas as pd
import quandl
import math
import numpy as np
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

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

X = np.array(df.drop(['label'],1))

y = np.array(df['label'])

X = preprocessing.scale(X)

y = np.array(df['label'])

t_size = float(input('Please specify the test size (%):'))

start_time = time.time()

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=t_size/100)

#clf = classifier

clf0 = LinearRegression()
clf0.fit(X_train, y_train)

clf1 = svm.SVR(kernel='poly')
clf1.fit(X_train, y_train)

clf2 = svm.SVR(kernel='linear')
clf2.fit(X_train, y_train)

clf3 = svm.SVR(kernel='rbf')
clf3.fit(X_train, y_train)

#R2
accuracy0 = clf0.score(X_test, y_test)
accuracy1 = clf1.score(X_test, y_test)    
accuracy2 = clf2.score(X_test, y_test)  
accuracy3 = clf3.score(X_test, y_test)  

print('\n\n*****ACCURACY OF THE REGRESSIONS with a test size of %s percent**** \n\n'%t_size)

print('linear regression: R2 = ' + str(accuracy0) + '\n')
print('svm polynomial: R2 = ' + str(accuracy1) + '\n')
print('svm linear: R2 = ' + str(accuracy2) + '\n')
print('svm exponential: R2 = ' + str(accuracy3) + '\n')

print('regression calculation time in seconds: %s \n\n' %(time.time() - start_time)) 




