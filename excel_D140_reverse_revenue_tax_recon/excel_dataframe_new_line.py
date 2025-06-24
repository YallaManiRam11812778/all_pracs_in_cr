import pandas as pd
import numpy as np

# Create some Pandas dataframes from some data.
df1 = pd.DataFrame({'Data 1': [11, 12]})
df2 = pd.DataFrame({'Data 2': [21, 22, 23]})

d = {'id1': ['85643', '85644', '85643', '8564312', '8564314', '85645', '8564316', '85646', '8564318', '85647', '85648', '85649', '85655', '56731', '34566', '78931', '78931'], 'ID': ['G-00001',  'G-00001', 'G-00002', 'G-00002', 'G-00002', 'G-00001', 'G-00001', 'G-00001', 'G-00001', 'G-00001', 'G-00002', 'G-00002', 'G-00002', 'G-00002', 'G-00003', 'G-00003', 'G-00003'], 'col1': [671,  2, 5, 3, 4, 5, 60, 0, 0, 6, 3, 2, 4, 32, 3, 1, 23], 'Goal': [np.nan,  56, 78, np.nan, 89, 73, np.nan, np.nan, np.nan,  np.nan,  np.nan,  34, np.nan,  7,  84, np.nan, 5],  'col2': [793,  4, 8, 32, 43, 55, 610, 0, 0, 16, 23, 72, 48, 3, 28, 5, 3], 'col3': [500,  22, 89, 33, 44, 55, 60, 1, 5, 6, 3, 2, 4, 13, 12, 14, 98], 'Date': ['2021-06-13',  '2021-06-13', '2021-06-14', '2021-06-13', '2021-06-14', '2021-06-15', '2021-06-15', '2021-06-13', '2021-06-16', '2021-06-13', '2021-06-13', '2021-06-13', '2021-06-16', '2021-05-23', '2021-05-13', '2021-03-26', '2021-05-13']}
df3 = pd.DataFrame(data=d)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_example.xlsx', engine='xlsxwriter')

start_row = 0

# Output the data frames and keep track of the start/end row.
for df in (df1, df2, df3):
    df.to_excel(writer, sheet_name='Sheet1', startrow=start_row, index=False)
    start_row += df.shape[0] + 2

# Get the xlsxwriter workbook and worksheet objects.
workbook = writer.book
worksheet = writer.sheets['Sheet1']
worksheet.set_zoom(60)
# Add a format
merge_format = workbook.add_format({
    'bold':     True,
    'align':    'center',
    'border':   6,
    'valign':   'vcenter',
    'fg_color': '#D7E4BC',
    'font_name': 'Calibri',
    'font_size': 12,
    'text_wrap': True
})

# Write a merge range.
start_row -= 1
start_col = 0
end_col = 3

worksheet.merge_range(start_row, start_col, start_row + 1, end_col,
                      "CompanyName: ABC\nCountry: USA", merge_format)

# Adjust header and data row heights.
start_row = 0
for df in (df1, df2, df3):
    worksheet.set_row(start_row, 50)

    for row_num in range(start_row + 1, start_row + df.shape[0] + 1):
        worksheet.set_row(row_num, 35)

    start_row += df.shape[0] + 2

# Close the Pandas Excel writer and output the Excel file.
writer._save()