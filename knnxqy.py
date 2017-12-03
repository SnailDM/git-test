# coding:utf-8
# python3 中无需调用division
from __future__ import division
from numpy import *
import numpy as np
import operator


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def clfKnn(X, data, labels, k):
    data_size = data.shape[0]
    diff = (tile(X, (data_size, 1)) - data) ** 2
    distance = (np.sum(diff, axis=1)) ** 0.5
    sort_distance = np.argsort(distance)
    vote_count = {}
    for i in range(k):
        vote_label = labels[sort_distance[i]]
        vote_count[vote_label] = vote_count.get(vote_label, 0) + 1
    sort_vote_count = sorted(vote_count.items(), key=operator.itemgetter(1), reverse=True)
    sort_result = sort_vote_count[0][0]
    return sort_result


data, labels = createDataSet()
xput = [5, 10]
k = 3
d = clfKnn(xput, data, labels, k)


# print(d)


def file2matrix(file):
    fr = open(file)
    lines = fr.readlines()
    lines_number = len(lines)
    data = zeros((lines_number, 3))
    labels = []
    #print(np.array(lines).shape)
    index = 0
    for line in lines:
        split_list = line.strip().split('\t')
        data[index, :] = split_list[0:3]
        labels.append(int(split_list[-1]))
        index += 1
    return data, labels


data, labels = file2matrix('datingTestSet2.txt')

# print(data)

import matplotlib
import matplotlib.pyplot as plt

ax = plt.subplot(2, 1, 1)
bx = plt.subplot(2, 1, 2)
ax.scatter(data[:, 0], data[:, 1], 15.0 * array(labels), 15.0 * array(labels))
bx.scatter(data[:, 0], data[:, 2], 15.0 * array(labels), 15.0 * array(labels))


# plt.grid(True)
# plt.show()

def data2norm(data):
    min_data = data.min(0)
    max_data = data.max(0)
    range_data = max_data - min_data
    data_len = data.shape[0]
    norm_data = data - tile(min_data, (data_len, 1))
    norm_data = norm_data / tile(range_data, (data_len, 1))
    return norm_data, min_data, range_data

data, labels = file2matrix('datingTestSet2.txt')
norm_data, min_data, range_data = data2norm(data)
#print("norm_data:%s, min_data:%s, range_data:%s\n" % (norm_data, min_data, range_data))

def datingClfTest(ratio):
    data, labels = file2matrix('datingTestSet2.txt')
    norm_data, min_data, range_data = data2norm(data)
    sample_num = norm_data.shape[0]
    # print(sample_num)
    test_num = int(sample_num * ratio)
    acc_num = 0
    predict_result = []
    for i in range(test_num):
        clf_result = clfKnn(norm_data[i, :], norm_data[test_num:sample_num, :], labels[test_num:sample_num], 3)
        #print("预测结果为：%s, 实际结果为：%s\n" % (clf_result, labels[i]))
        predict_result.append(clf_result)
        if clf_result == labels[i]:
            acc_num += 1
    acc_rate = acc_num/test_num
    return predict_result, acc_rate


#predict_result, acc_rate = datingClfTest(0.1)
#print("全部预测值为：%s\n" % predict_result)
#print("预测准确率为：%s\n" % acc_rate)

def clfPerson():
    result_list = ['不喜欢', '有点喜欢', '非常喜欢']
    a = float(raw_input("请输入第一个参数？"))
    b = float(raw_input("请输入第二个参数？"))
    c = float(raw_input("请输入第三个参数？"))
    data, labels = file2matrix('datingTestSet2.txt')
    data_in = array([a, b, c])
    norm_data, min_data, range_data = data2norm(data)
    person_result = clfKnn((data_in - min_data)/range_data, data, labels, 3)
    result = result_list[person_result - 1]
    return result

#result = clfPerson()
#print("你的喜欢程度是：%s\n" % result)





