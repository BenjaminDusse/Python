# import pandas as pd

# path = "C: \Users\abduh\OneDrive\Desktop\Task NBU\src\new.xlsx"
# print(pd.ExcelWriter(path, engine=None))

# with pd.ExcelWriter(
#     "new.xlsx",
#     engine='openpyxl',
#     mode="a"
# )


import xlsxwriter

workbook = xlsxwriter.Workbook('1.xlsx')
worksheet = workbook.add_worksheet()

# worksheet.set_column("A:H", 20)

worksheet.write("E1", "Hello")

workbook.close()