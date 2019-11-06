import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('50_Startups.csv')

dataset.head()

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()

# mostrar o X no console:
# X

# realizar o fit_transform
X[:, 3] = labelencoder.fit_transform(X[:, 3])

# mostrar o X no console:
# X


onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()


# Avoiding the Dummy Variable Trap
# The Dummy Variable trap is a scenario in which the 
# independent variables are multicollinear - a scenario in 
# which two or more variables are highly correlated; 
# in simple terms one variable can be predicted from the others.
X = X[:, 1:]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
y_pred
