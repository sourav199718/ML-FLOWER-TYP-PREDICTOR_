# -*- coding: utf-8 -*-
"""IRIS PROJ.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18qMFCp-UMCGmi2MHv6qkUtizvMpw9RfE
"""

from google.colab import files
uploaded = files.upload()

import pandas as pd
df = pd.read_csv('IRIS.csv')
df

df['species'].unique()

len(df['species'])

df['species'].replace({'Iris-setosa':'1', 'Iris-versicolor':'2', 'Iris-virginica':'3'},inplace = True)

df

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(df[['sepal_length','sepal_width','petal_length',	'petal_width']],df['species'],test_size=0.2)

len(x_train)

len(x_test)

from sklearn.linear_model import LogisticRegression
lg = LogisticRegression()
lg.fit(x_train,y_train)

lg.predict(x_test)

lg.score(x_test,y_test)

