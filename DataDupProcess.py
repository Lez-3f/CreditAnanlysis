#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2021/8/6
@file: DataDupProcess.py
@author: ZEL
"""
import pandas as pd

# 加载数据集，查看数据集基本信息
df_data_init = pd.read_csv('Data/cs-training.csv', index_col=[0])
print("数据的基本信息:\n")
df_data_init.info()

# 输出前5行数据,输出数据的描述性统计
print("前5行数据:\n", df_data_init.iloc[0:5, :])
print("数据的描述性统计:\n", df_data_init.describe())

# 重复行处理:如果存在重复行，保留一行，删除其余重复行
dup_row = df_data_init.duplicated(keep=False)

if dup_row.sum() == 0:
    print('数据没有重复行')
    df_data_delDup = df_data_init
else:
    print('将重复行保留一行，其余删除')
    df_data_delDup = df_data_init.drop_duplicates(keep='first')

# 将处理后的数据集保存至新的csv文件
df_data_delDup.to_csv('Data/cs-training_delDup.csv', index=True)


