import pandas as pd
pd.set_option('display.max_columns', None)

#将每一份文本的标签隔开，转换成列表
def readlabel(path,label_name, id_name):
    read_data = pd.read_csv(path)
    read_data[label_name] = read_data[label_name].apply(lambda x: '/' + x)
    data_concat = read_data.groupby(by=id_name).sum()
    data_concat[label_name] = data_concat[label_name].apply(lambda x: x[1:])
    data_concat.index = range(len(data_concat[label_name]))
    row_num = len(data_concat[label_name])
    data = []
    for i in range(0, row_num):
        data.append(data_concat.loc[i,label_name])
    return (data)

#建立关于标签的字典
def dic(readpath, label_name):
    label_data = pd.read_csv(readpath)
    label_list = list(set(label_data[label_name].values.tolist()))
    labeldic = {}
    pos = 0
    for i in label_list:
        pos = pos+1
        labeldic[pos] = str(i)
    # print(labeldic)
    return labeldic

#构建空矩阵用于存放标签的共现矩阵
def buildmatrix(x, y):
    return [[0 for j in range(y)] for i in range(x)]

#将标签分行列构建初始共现矩阵用于存放计算结果
def inimatrix(matrix, dic, length):
    matrix[0][0] = 'label'
    for i in range(1, length):
        matrix[0][i] = dic[i]
    for i in range(1, length):
        matrix[i][0] = dic[i]

    return matrix

#计算标签与标签之间的共现次数
def countmatirx(matrix, dic, mlength, keylis):
    for i in range(1, mlength):
        for j in range(1, mlength):
            count = 0
            for k in keylis:
                ech = str(k).split('/')

                if str(matrix[0][i]) in ech and str(matrix[j][0]) in ech and str(matrix[0][i]) != str(matrix[j][0]):
                    count = count+1
                else:
                    continue
            matrix[i][j] = int(count)
    return matrix

#取出标签之间的共现值用于PMI计算
def label_concurrence_value(data, a, b):
    con_value = data.loc[a,b]
    return con_value

def main():
    readpath = r'E:\gitfile\test.csv'   #原始输入数据
    save_path = r'E:\gitfile\concurrence_data.xlsx' #存放共现矩阵
    co_calcul_path = r'E:\gitfile\test1.xlsx'   #需要计算PMI值的文档
    co_result_path = r'E:\gitfile\test_result.xlsx' #存放计算结果
    label_list = readlabel(readpath, label_name='label', id_name='id')   #将每一份文本的标签隔开，转换成列表
    label_dict = dic(readpath, label_name='label')   #建立关于标签的字典
    length = len(label_dict)+1
    matrix = buildmatrix(length, length)    #构建空矩阵用于存放标签的共现矩阵
    matrix = inimatrix(matrix, label_dict, length)  #将标签分行列构建初始共现矩阵用于存放计算结果
    matrix = countmatirx(matrix, label_dict, length, label_list)    #计算标签与标签之间的共现次数
    concurrence_data = pd.DataFrame(matrix, columns=matrix[0], index=matrix[0])
    concurrence_data = concurrence_data.drop(['label'], axis=0)
    concurrence_data = concurrence_data.drop(['label'], axis=1)
    # print(concurrence_data)
    concurrence_data.to_excel(save_path)
    co_data = pd.read_excel(co_calcul_path)
    row_num = co_data.shape[0]

    for j in range(0,row_num):
        data1 = co_data.loc[j, 'A标签']
        data2 = co_data.loc[j,'B标签']
        con_value = label_concurrence_value(concurrence_data, data1, data2)
        co_data.loc[j,'共现频次'] = con_value
    print(co_data)
    co_data = co_data[['A标签','B标签','共现频次']]
    co_data.to_excel(co_result_path)

if __name__ == '__main__':
    main()