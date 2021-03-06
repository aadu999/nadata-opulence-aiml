#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 22:33:33 2018

@author: admin
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Salary_Data.csv')
x=dataset.iloc[:,:-1].values
y=dataset.iloc[:,1].values

from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.33,random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)
y_predict = regressor.predict(x_test)

plt.subplot(121)
plt.scatter(x_train,y_train,color='red')
plt.plot(x_train,regressor.predict(x_train),'green')
plt.xlabel('years of exp')
plt.ylabel('Salary')
plt.subplot(122)
plt.scatter(x_test,y_test,color='red')
plt.plot(x_test,y_predict,'green')
plt.xlabel('years of exp')
plt.ylabel('Salary')
    
