import pandas as pd
import glob

location = "C:\\Users\\abduh\\OneDrive\\Desktop\\Task NBU\\*.xlsx"
excel_files = glob.glob(location)
# print(excel_files)

pd.set_option("display.max_rows", 91)

df1 = pd.DataFrame()

for excel_file in excel_files:
    df2 = pd.read_excel(excel_file)
    df1 = pd.concat([df1, df2], ignore_index=True)

df1.to_excel(
    "C:\\Users\\abduh\\OneDrive\\Desktop\\Task NBU\\src\\combined sleep data\\all_sleep_data.xlsx", index=True
)


print(df1)
