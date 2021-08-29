#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2021/8/6
@file: DataNanProcess.py
@author: ZEL
"""
import pandas as pd

# 加载除重复行后的数据集
df_data = pd.read_csv('Data/cs-training_deldup.csv', index_col=[0])

# 统计缺失值总数
s_data_nan = pd.Series(df_data.isnull().sum())
print("缺失值总数: ", s_data_nan.sum())

# 输出有缺失值的列，及该列缺失值的个数
col_has_nan = list(df_data.columns[df_data.isnull().sum() > 0])
print("含有缺失值的列:")
for col in col_has_nan:
    print(col, df_data[col].isnull().sum())

# 缺失值处理
for col in col_has_nan:
    # 对缺失值小于100的列，直接删除该列缺失值所在的行
    if df_data[col].isnull().sum() < 100:
        df_data.dropna(subset=[col], inplace=True)
    # 对缺失值大于等于100的列，用列均值填充缺失值
    else:
        mean_val = df_data[col].mean()
        df_data[col].fillna(mean_val, inplace=True)

# 保存缺失值处理后的数据至新的csv文件
df_data.to_csv('Data/cs-training_delNan.csv', index=True)
