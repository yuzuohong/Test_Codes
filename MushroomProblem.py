from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from numpy.random import permutation
from numpy import array_split, concatenate
from sklearn.metrics import roc_curve, auc, mean_squared_error
import pandas as pd
import numpy as np

class MushroomProblem:
	def __init__(self, data_file):
		self.dataFrame = pd.read_csv(data_file)
		for k in self.dataFrame.columns[1:]:
			self.dataFrame[k], _ = pd.factorize(self.dataFrame[k])
		sorted_cats = sorted(pd.Categorical(self.dataFrame['class']).categories)
		self.classes = np.array(sorted_cats)
		self.features = self.dataFrame.columns[self.dataFrame.columns != 'class']
	def __factorize(self, data):
		y, _ = pd.factorize(pd.Categorical(data['class']), sort=True)
		return y

class MushroomProblem:
	# __init__
	def validation_data(self, folds):
		df = self.dataFrame
		response = []
		assert len(df) > folds
		perms = array_split(permutation(len(df)), folds)
		for i in range(folds):
			train_idxs = range(folds)
			train_idxs.pop(i)
			train = []
			for idx in train_idxs:
				train.append(perms[idx])
			train = concatenate(train)
			test_idx = perms[i]
			training = df.iloc[train]
			test_data = df.iloc[test_idx]
			y = self.__factorize(training)
			classifier = self.train(training[self.features], y)
			predictions = classifier.predict(test_data[self.features])
			expected = self.__factorize(test_data)
			response.append([predictions, expected])
		return response

