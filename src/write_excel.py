import os
import pandas as pd
import openpyxl

cwd = os.path.abspath('')
# print(cwd)
files = os.listdir(cwd)
print(files)


df = pd.DataFrame()
for file in files:
    if file.endswith('.xlsx'):
        df = df.append(pd.read_excel(file), ignore_index=True)

df.to_excel('total_sales.xlsx')

