import pandas as pd
data = pd.read_excel('E:\\PythonTestCode\\public opinion.xlsx', sheetname='public opinion', header=1)

row_num, column_num = data.shape    #数据共有多少行，多少列
print('the sample number is %s and the column number is %s' % (row_num, column_num))
#这里我们的数据共有210000行，假设要让每个文件1万行数据，即分成21个文件
for i in range(0, 21):
    save_data = data.iloc[i*10000+1:(i+1)*10000+1, :] #每隔1万循环一次
    file_name= 'E:\\PythonTestCode\\public opinion\\public opinion' + str(i) + '.xlsx'
    save_data.to_excel(file_name, sheet_name = 'public opinion', index = False)
