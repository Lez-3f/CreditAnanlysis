#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2021/8/8
@file: DataFeatureAnalysis.py
@author: ZEL
"""
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# 字体格式
matplotlib.rcParams['font.family'] = 'STSong'
matplotlib.rcParams['font.size'] = 12

# 加载数据
df_data = pd.read_csv("Data/cs-training_delabn.csv", index_col=[0])

# 特征数据分析
# 绘制年龄，月收入变量的直方图
plt.figure(figsize=(12, 6), num='直方图')

plt.subplot(121)
plt.hist(df_data['Age'], bins=30, density=True,
         edgecolor='black', linewidth='1.0')
plt.xlabel('年龄')
plt.xlim([0, 100])
plt.ylabel('频数')
plt.title('年龄直方图')

plt.subplot(122)
plt.hist(df_data['MonthlyIncome'], bins=30, density=True,
         edgecolor='black', linewidth='1.0')
plt.xlabel('月收入')
plt.xlim([0, 40000])
plt.ylabel('频数')
plt.title('月收入直方图')

plt.subplots_adjust(wspace=0.3)
plt.savefig('Figure/HistogramOfAge&MonIncome')
plt.show()

# 输出各变量之间的关系矩阵
corr_matrix = df_data.corr(method='pearson')
print('各列数据之间的关系矩阵为:\n', corr_matrix)

# 特征选择
# 将与SeriousDlqin2yrs（y）之间的相关系数的绝对值低于 0.1 的剔除
corr_select = corr_matrix.query('SeriousDlqin2yrs > 0.1 | SeriousDlqin2yrs < -0.1')
selected_data = df_data[list(corr_select.index)]
print("选择后的数据为:\n", selected_data)

# 保存数据
selected_data.to_csv("Data/cs-training_selected.csv", index=True)
