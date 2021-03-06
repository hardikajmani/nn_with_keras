# -*- coding: utf-8 -*-
"""Neural_Net_keras.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SkHU43xvWML2jzcCW1G1szMu2GzMInw9

This is the code created with keras.
Our basic aim is to predict customer churn for a certain bank i.e. which customer is going to leave this bank service. Dataset is small(for learning purpose) and contains 10000 rows with 14 columns. I am not explaining data in detail as dataset is self explanatory.
Dataset is uploaded into the drive
"""

#importing libraries

import keras
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



#@title uploading dataset
from google.colab import files
uploaded = files.upload()

df = pd.read_csv("Churn_Modelling.csv")

#@title Default title text
# allocating x and y matrices 
X = df.iloc[:, 3:13].values
y = df.iloc[:, 13].values

#label encoding all the string elements

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X1 = LabelEncoder()
X[:, 1] = labelencoder_X1.fit_transform(X[:, 1])
print(X[:,1])
labelencoder_X2 = LabelEncoder()
X[:, 2] = labelencoder_X2.fit_transform(X[:, 2])
print(X[:, 2])

oneHot = OneHotEncoder(categorical_features = [1])
X = oneHot.fit_transform(X).toarray()
X = X[:, 2:]

#splitting the dataset into the training set and test set

from sklearn.model_selection import train_test_split

X_train,X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

#Feature scaling

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from keras.models import Sequential
from keras.layers import Dense

#Initializing Neural Network

classifier = Sequential()

#Adding the input layer and the first hidden layer
classifier.add(Dense(output_dim = 6, init = 'uniform', activation = 'relu', input_dim = 11))

# Adding the second hidden layer
classifier.add(Dense(output_dim = 6, init = 'uniform', activation = 'relu'))

# Adding the output layer
classifier.add(Dense(output_dim = 1, init = 'uniform', activation = 'sigmoid'))

#compiling neural network

classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

#fitting or training our model

classifier.fit(X_train, y_train, batch_size = 10, nb_epoch = 100)

#predicting the test set results

y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

# Creating the confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

print("Accuracy: " + str((cm[0,0] + cm[1,1])/2000 * 100))