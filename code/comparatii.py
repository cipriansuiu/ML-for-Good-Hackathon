
import os
import pandas as pd
from scipy.stats import ttest_ind

dataframes = []
class prettyfloat(float):
    def __repr__(self):
        return "%0.10f" % self

for root,dirs,files in os.walk(r'C:\Users\Suiu\PycharmProjects\ML-for-Good-Hackathon\code\date_roxana', topdown=False):
    for name in files:
        file_name = os.path.join(root, name)
        df = pd.read_excel(file_name)
        df.dropna()
        dataframes.append(df)
columns = dataframes[0].columns
print(columns)
for column in columns[5:68]:
    pd.options.display.float_format = '{:,.2f}'.format
    d1 = dataframes[0][column].dropna()
    d2 = dataframes[1][column].dropna()
    # print('d1')
    # print(d1)
    # print('d2')
    # print(d2)
    if not isinstance(d1,str) and not isinstance(d2,str) :
        t_stat, p = ttest_ind(d1, d2)
        if p < 0.05:
            print("-----MATCH------")
            print(column)
            print("----------------")
        print(column)
        print(f't={prettyfloat(t_stat)}, p={prettyfloat(p)}')
