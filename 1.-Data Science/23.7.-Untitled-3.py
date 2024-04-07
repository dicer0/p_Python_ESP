import pandas as pd

data = [[i, 'standards' if i % 3 == 0 else 'not standard' if i % 2 == 0 else 'olis'] for i in range(1, 11)]
df = pd.DataFrame(data, columns=['A', 'B'])

writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')

df.to_excel(writer, index=False, sheet_name='nombreSheet')

workbook = writer.book

worksheet = writer.sheets['nombreSheet']

red_format = workbook.add_format({'bg_color': '#FF0000'})
green_format = workbook.add_format({'bg_color': '#00FF00'})
blue_format = workbook.add_format({'bg_color': '#0000FF'})

worksheet.conditional_format('B2:B{}'.format(len(df) + 1), {'type': 'text',
                                                             'criteria': 'containing',
                                                             'value': 'standards',
                                                             'format': red_format})

worksheet.conditional_format('B2:B{}'.format(len(df) + 1), {'type': 'text',
                                                             'criteria': 'containing',
                                                             'value': 'not standard',
                                                             'format': green_format})

worksheet.conditional_format('B2:B{}'.format(len(df) + 1), {'type': 'text',
                                                             'criteria': 'containing',
                                                             'value': 'olis',
                                                             'format': blue_format})

writer.save()