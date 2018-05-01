#-*- coding: utf-8 -*-
#基于3sigma的异常值检测

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt #导入绘图库

n = 3 # n*sigma

catering_sale = 'E:\\PythonTestCode\\dadm\\chapter3\\chapter3\\demo\\data\\catering_sale.xls' #数据路径

data = pd.read_excel(catering_sale, index_col = False) #读取数据
data_y = data[u'销量']
data_x = data[u'日期']

ymean = np.mean(data_y)
ystd = np.std(data_y)
threshold1 = ymean - n * ystd
threshold2 = ymean + n * ystd

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