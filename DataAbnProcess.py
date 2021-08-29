#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2021/8/8
@file: DataAbnProcess.py
@author: ZEL
"""
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt

# 字体格式
matplotlib.rcParams['font.family'] = 'STSong'
matplotlib.rcParams['font.size'] = 12

# 加载数据
df_data = pd.read_csv("Data/cs-training_delnan.csv", index_col=[0])
print(df_data)
# 剔除 age=0/age>100 or MonthlyIncome=0 所在行
abn_index = df_data.query("Age<=0 or Age>100 or MonthlyIncome==0 or MonthlyIncome > 50000").index
df_data.drop(index=abn_index, inplace=True)

# 绘制箱线图
plt.figure(figsize=(8, 6), num="箱线图")
df_data[['NumberOfTime30-59DaysPastDueNotWorse',
         'NumberOfTime60-89DaysPastDueNotWorse',
         'NumberOfTimes90DaysLate']].boxplot()
plt.xticks([1, 2, 3], ['30-59', '60-89', '90+'])
plt.title('三列数据的箱线图')
plt.xlabel('逾期天数')
plt.ylabel('笔数')
plt.savefig('Figure/BoxChartOf3Cols_BeforeDeleteAbnormalVal.png')
plt.show()


# 删除明显的异常值所在的行
df_data_delabn = df_data[(df_data['NumberOfTime30-59DaysPastDueNotWorse'] < 80) &
                         (df_data['NumberOfTime60-89DaysPastDueNotWorse'] < 80) &
                         (df_data['NumberOfTimes90DaysLate'] < 80)]

# 再次绘制箱线图
plt.figure(figsize=(8, 6), num="箱线图")
df_data_delabn[['NumberOfTime30-59DaysPastDueNotWorse',
                'NumberOfTime60-89DaysPastDueNotWorse',
                'NumberOfTimes90DaysLate']].boxplot()
plt.xticks([1, 2, 3], ['30-59', '60-89', '90+'])
plt.ylim([0, 100])
plt.title('三列数据的箱线图-删除异常数据后')
plt.xlabel('逾期天数')
plt.ylabel('笔数')
plt.savefig('Figure/BoxChartOf3Cols_AfterDeleteAbnormalVal.png')
plt.show()

# 保存数据
df_data_delabn.to_csv('Data/cs-training_delabn.csv', index=True)
