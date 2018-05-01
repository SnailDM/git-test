#-*- coding: utf-8 -*-
#基于箱型图的异常值检测

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt #导入绘图库

catering_sale = 'D:/PythonTestCode/dadm/chapter3/chapter3/demo/data/catering_sale.xls' #数据路径

data = pd.read_excel(catering_sale, index_col = False) #读取数据
data_y = data[u'销量']
data_x = data[u'日期']

statistics = data_y.describe() #保存基本统计量
IQR = statistics.loc['75%']-statistics.loc['25%']   #四分位数间距
QL = statistics.loc['25%']  #下四分位数
QU = statistics.loc['75%']  #上四分位数
threshold1 = QL - 1.5 * IQR #下阈值
threshold2 = QU + 1.5 * IQR #上阈值
outlier = [] #将异常值保存
outlier_x = []

for i in range(0, len(data_y)):
    if (data_y[i] < threshold1)|(data_y[i] > threshold2):
        outlier.append(data_y[i])
        outlier_x.append(data_x[i])
    else:
        continue

print('\n异常数据如下：\n')
print(outlier)
print(outlier_x)

plt.plot(data_x, data_y)
plt.plot(outlier_x, outlier, 'ro')
for j in range(len(outlier)):
    plt.annotate(outlier[j], xy=(outlier_x[j], outlier[j]), xytext=(outlier_x[j],outlier[j]))
plt.show()


