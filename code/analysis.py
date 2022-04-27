
import os
import pandas as pd

for root,dirs,files in os.walk(r'C:\Users\Suiu\PycharmProjects\ML-for-Good-Hackathon\code\data', topdown=False):
    for name in files:
        file_name = os.path.join(root, name)
        writer = pd.ExcelWriter(os.path.join('output/',name))
        df = pd.read_excel(file_name)
        df.dropna()
        df_mean = df.mean()
        pd.options.display.float_format = '{:,.2f}'.format
        df_median = df.median()
        df_min = df.min()
        df_max = df.max()
        df_max.describe()
        df_mean.to_excel(writer,'mean')
        df_median.to_excel(writer,'median')
        pd.DataFrame(df_min).to_excel(writer,'min')
        pd.DataFrame(df_max).to_excel(writer, 'max')
        writer.save()






