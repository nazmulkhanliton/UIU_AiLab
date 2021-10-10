# -*- coding: utf-8 -*-
"""logistic_regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CXul2QZn3olB4mLfghvAp0TVTWMNgPrf
"""

#Load Irish Dataset from Sklearn
import matplotlib
import matplotlib.pyplot as plt
from sklearn import datasets
import pandas as pd
import numpy as np
import math

iris = datasets.load_iris()

x = iris.data[:, :2]
y = (iris.target != 0) * 1
print(y)
print(len(x))

#plz X dataset
x1 = iris.data[:, :1]
y1 = iris.data[:, 1:2]
print(len(x1))
print(len(y1))
#print(x1)
#print(y1)
plt.scatter(x1,y1)
plt.title('X1 VS Y1')
plt.xlabel('X1', c='r')
plt.ylabel('Y1', c='r')
plt.show()

#initialization with 1

x_updated = []


for i in range(len(x)):
  temp_Value = []
  temp_Value.append(1)
  temp_Value.append(x[i][0]) 
  temp_Value.append(x[i][1])
  x_updated.append(temp_Value)

print(x_updated)

#Dataset split
import random 

x_train_set = []
y_train_set = []
x_val_set = []
y_val_set = []
x_test_set = []
y_test_set = []


for s in range(len(x)):
  R = random.uniform(0, 1)
  if R>=0 and R<=0.6:
    x_train_set.append(x_updated[s])
    y_train_set.append(y[s])
  elif R>0.6 and R<=0.8:
    x_val_set.append(x_updated[s])
    y_val_set.append(y[s])
  else:
    x_test_set.append(x_updated[s])
    y_test_set.append(y[s])


print('x_train_set', + len(x_train_set))
print('x_val_set', + len(x_val_set))
print('x_test_set', + len(x_test_set))
print('Total:', + len(x_train_set) + len(x_val_set) + len(x_test_set))

#print('x_train', + len(x_train))

#Theta initialization

theta = [0.4913279309, 0.165426577, 0.202296275]
print(theta)

#Model Training

lr = 0.00001
train_set_loss = []


for iteration in range(100000):
  tj = 0
  for i in range(len(x_train_set)):
    z = np.dot(x_train_set[i],theta)
    h = 1 / (1 + math.exp(-z))

    j = (-y_train_set[i] * np.log(h)) - ((1-y_train_set[i]) * np.log(1-h))
    tj = tj + j

    dv = np.array(x_train_set[i])*(h-y_train_set[i])
    theta = theta - (np.array(dv) * lr)



  tj = tj/len(x_train_set)
  train_set_loss.append(tj)

print(train_set_loss)
print(theta)

#For Validation 

correctly_classified = 0
for i in range(len(x_val_set)):
  z = np.dot(x_val_set[i],theta)
  h = 1 / (1 + math.exp(-z))
  if h>= 0.5:
    h = 1
  else:
    h = 0
  
  if h == y_val_set[i]:
    correctly_classified = correctly_classified + 1

validation_accuracy = (correctly_classified / len(x_val_set)) * 100


#print(len(y_val_set))
print(validation_accuracy)

#l.r. and validation_accuracy table:
from tabulate import tabulate
print('Validation Accuracy Table')
print(tabulate([['0.1', 97.14], ['0.01', 100.00], ['0.001', 96.55 ], ['0.0001', 92.34], ['0.00001', 67.56]], headers=['L.R.','Accuracy']))

#test code

correctly_classified = 0
for i in range(len(x_test_set)):
  z = np.dot(x_test_set[i],theta)
  h = 1 / (1 + math.exp(-z))
  if h>= 0.5:
    h = 1
  else:
    h = 0
  
  if h == y_test_set[i]:
    correctly_classified = correctly_classified + 1

validation_accuracy = (correctly_classified / len(x_test_set)) * 100


print(len(y_test_set))
print(validation_accuracy)

# train_loss vs epoch graph plot for the best l.r
# train_set_loss, epoch
print(len(train_set_loss))
epoch = np.arange(1, 100001, 1).tolist()

print(epoch)

plt.plot(train_set_loss, epoch)
plt.title('Train loss vs Epoch graph plot for the best l.r', c='green')
plt.xlabel('Train set loss', c='r')
plt.ylabel('Epoch / Initialization', c='r')
plt.show()