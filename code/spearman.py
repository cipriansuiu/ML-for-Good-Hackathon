import pandas as pd
df = pd.read_excel(r'C:\Users\Suiu\PycharmProjects\ML-for-Good-Hackathon\code\date_roxana\VHB.xlsx')
df.dropna()

print(df.corr(method='spearman'))