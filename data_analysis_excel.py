import pandas as pd
data = pd.read_excel('E:\\PythonTestCode\\public opinion.xlsx', sheetname='public opinion', usecols= ['电商平台', '品牌', '评论'])
print(data.head())

data1 = data.iloc[1:100, :]
data2 = data.iloc[101:400, :]
# data1.to_excel('E:\\PythonTestCode\\public opinion_result.xlsx', sheet_name = 'data1')
# data1.to_excel('E:\\PythonTestCode\\public opinion_result.xlsx', sheet_name = 'data2')

writer = pd.ExcelWriter('E:\\PythonTestCode\\public opinion_result.xlsx')
data1.to_excel(writer, sheet_name = 'data1', index = False)
data2.to_excel(writer, sheet_name = 'data2', index = False)
writer.save()
writer.close()

