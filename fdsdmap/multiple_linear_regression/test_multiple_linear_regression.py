#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:55:24 2019

@author: chvs
"""

import pandas as pd

df = pd.read_csv('50_Startups.csv')

df.head()


X = df.drop(['Profit'], axis = 1).values
y = df['Profit'].values


X = X.reshape((len(X), 4))
y = y.reshape((len(y), 1))

assert X.shape == (len(X), 4)
assert y.shape == (len(y), 1)

X

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

X[:, 3] = encoder.fit_transform(X[:, 3])

np.array(X[:, 3])
np.unique(X[:, 3])

from sklearn.preprocessing import OneHotEncoder
encoder = OneHotEncoder(categorical_features=[3])
X = encoder.fit_transform(X).toarray()

X

from sklearn.model_selection import train_test_split
X_train, y_train, X_test, y_test = train_test_split(X, y, test_size=0.2)

from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(X_train, y_train)

X_train.shape

y_pred = regression.predict(X_test)
y_pred
