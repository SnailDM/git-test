import pandas as pd

data0 = pd.read_excel('E:\\PythonTestCode\\public opinion\\public opinion0.xlsx', sheetname='public opinion')
data1 = pd.read_excel('E:\\PythonTestCode\\public opinion\\public opinion1.xlsx', sheetname='public opinion')
data = pd.concat([data0, data1])

for i in range(2, 21):
    file_name = 'E:\\PythonTestCode\\public opinion\\public opinion' + str(i) + '.xlsx'
    data2 = pd.read_excel(file_name)
    data = pd.concat([data, data2])
data.to_excel('E:\\PythonTestCode\\public opinion\\public opinion-concat.xlsx', index = False)
