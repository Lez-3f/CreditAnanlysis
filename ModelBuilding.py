#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2021/8/8
@file: ModelBuilding.py
@author: ZEL
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

# 加载数据
df_data = pd.read_csv('Data/cs-training_selected.csv', index_col=[0])

x = df_data[['NumberOfTime30-59DaysPastDueNotWorse',
             'NumberOfTimes90DaysLate',
             'NumberOfTime60-89DaysPastDueNotWorse']]
y = df_data['SeriousDlqin2yrs']

# 将数据分成训练集（70%）和测试集（30%）
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

# 使用训练集建立模型
model_lr = LogisticRegression(max_iter=500)
model_lr.fit(x_train, y_train)

# 预测测试集
y_predict = model_lr.predict(x_test)
print('逻辑回归模型评分（acc）:\n', model_lr.score(x_test, y_test))
print('逻辑回归模型评分:\n', metrics.accuracy_score(y_test, y_predict))

# 保存预测结果
y_test.to_csv('Data/cs-training_test.csv')
np.savetxt('Data/cs-training_predict.csv', y_predict, fmt='%0.1f', delimiter=',', newline='\n')
