import pandas as pd

# excel_file = '1.xlsx'

number_of_files = int(input("Enter number to read excel files: "))
# data = pd.read_excel("1.xlsx", sheet_name=0, index_col=None, na_values=["Mavjud emas"])
# print(data)

file = "{}.xlsx"
for i in range(1, number_of_files + 1):
    data = pd.read_excel(
        file.format(i),  sheet_name=None, usecols="B:H"
    )
    print(data)

# data = pd.read_excel(excel_file)
# rows = pd.read_excel(excel_file, sheet_name=0, index_col=1)
# print(rows)
# print(data)

# df = pd.DataFrame(data, columns=['Международные резервы Республики Узбекистан', ])
# print(df)

