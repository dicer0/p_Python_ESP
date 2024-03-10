import pandas as pd

data = {'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10],
        'C': [11, 12, 13, 14, 15],
        'D': [1, 1, 1, 4, 1]}
df = pd.DataFrame(data)

writer = pd.ExcelWriter('resultado.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1', index=False)
workbook = writer.book
worksheet = writer.sheets['Sheet1']
blue_format = workbook.add_format({'bg_color': '#0000FF'})
green_format = workbook.add_format({'bg_color': '#00FF00'})
grey_format = workbook.add_format({'bg_color': '#D3D3D3'})
yellow_format = workbook.add_format({'bg_color': '#FFFF00'})

num_rows, num_cols = df.shape
worksheet.conditional_format(0, 0, 0, num_cols - 1, {'type': 'no_blanks', 'format': blue_format})
worksheet.conditional_format(1, 0, num_rows, 0, {'type': 'no_blanks', 'format': green_format})
worksheet.conditional_format(1, 1, num_rows, 1, {'type': 'no_blanks', 'format': grey_format})

for col in range(2, num_cols):
    worksheet.conditional_format(1, col, num_rows, col, {'type': 'no_blanks', 'format': yellow_format})

writer.save()