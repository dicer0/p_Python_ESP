import pandas as pd

# Crear un DataFrame de ejemplo
data = {'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10],
        'C': [11, 12, 13, 14, 15],
        'D': [1, 1, 1, 4, 1]}
df = pd.DataFrame(data)

# Crear un objeto ExcelWriter
writer = pd.ExcelWriter('resultado.xlsx', engine='xlsxwriter')

# Escribir el DataFrame en una hoja de Excel
df.to_excel(writer, sheet_name='Sheet1', index=False)

# Obtener el objeto workbook y la hoja de Excel
workbook = writer.book
worksheet = writer.sheets['Sheet1']

# Definir formatos de celda
blue_format = workbook.add_format({'bg_color': '#0000FF'})
green_format = workbook.add_format({'bg_color': '#00FF00'})
grey_format = workbook.add_format({'bg_color': '#D3D3D3'})
yellow_format = workbook.add_format({'bg_color': '#FFFF00'})

# Aplicar formato a las celdas de datos
(num_rows, num_cols) = df.shape

# Primera fila azul (encabezados de columnas)
worksheet.conditional_format(0, 0, 0, num_cols - 1, {'type': 'no_blanks', 'format': blue_format})

# Primera columna verde
worksheet.conditional_format(1, 0, num_rows, 0, {'type': 'no_blanks', 'format': green_format})

# Segunda columna gris
worksheet.conditional_format(1, 1, num_rows, 1, {'type': 'no_blanks', 'format': grey_format})

# Resto de las columnas amarillas
for col in range(2, num_cols):
    worksheet.conditional_format(1, col, num_rows, col, {'type': 'no_blanks', 'format': yellow_format})

# Guardar el archivo
writer.save()