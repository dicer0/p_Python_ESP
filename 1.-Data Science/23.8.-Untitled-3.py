from openpyxl import load_workbook

def ajustar_celdas_excel(ruta_excel, ancho_maximo, altura_maxima):
    # Cargar el libro de trabajo de Excel existente
    wb = load_workbook(ruta_excel)

    # Obtener la hoja activa del libro de trabajo
    ws = wb.active

    # Ajustar el ancho de la primera columna basado en el contenido
    max_length_first_col = 0
    for cell in ws[ws.cell(row=1, column=1).column]:
        try:
            if len(str(cell.value)) > max_length_first_col:
                max_length_first_col = len(str(cell.value))
        except:
            pass
    adjusted_width_first_col = min((max_length_first_col + 2) * 1.2, ancho_maximo)
    ws.column_dimensions['A'].width = adjusted_width_first_col

    # Convertir el objeto generador en una lista para poder acceder a sus elementos
    columns_list = list(ws.columns)
    # Ajustar el ancho de las columnas restantes basado en el contenido
    for col in columns_list[1:]:
        max_length = 0
        column = col[0].column_letter
        for cell in col:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = min((max_length + 2) * 1.2, ancho_maximo)
        ws.column_dimensions[column].width = adjusted_width

    # Ajustar la altura de las filas basada en el contenido y las filas fusionadas
    for row in ws.iter_rows():
        max_height = 0
        for cell in row:
            try:
                lines = str(cell.value).count('\n') + 1
                height = lines * 15
                if height > max_height:
                    max_height = height
            except:
                pass
        # Considerar filas fusionadas
        for cell in row:
            if cell.coordinate in ws.merged_cells:
                for range_ in ws.merged_cells.ranges:
                    if cell.coordinate in range_:
                        for row_ in range(range_.min_row, range_.max_row + 1):
                            # Verificar si la altura es None antes de comparar
                            if ws.row_dimensions[row_].height is not None:
                                max_height = max(max_height, ws.row_dimensions[row_].height)
        # Asignar un valor predeterminado si la altura es None
        if max_height == 0:
            max_height = 15  # Valor predeterminado
        adjusted_height = min(max_height, altura_maxima)
        ws.row_dimensions[row[0].row].height = adjusted_height

    # Guardar el libro de trabajo con los ajustes realizados
    wb.save(ruta_excel)

# Ruta del archivo Excel a ajustar
excelFilePath2 = "C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/1.-Data Science/0.-Archivos_Ejercicios_Python/23.-GUI PyQt5 Conexion DataBase/23.-Reporte Analisis de Datos 2.xlsx"
# Ancho máximo de las celdas (en caracteres)
ancho_maximo = 40
# Altura máxima de las celdas (en píxeles)
altura_maxima = 20
# Llamar a la función para ajustar las celdas del archivo Excel
ajustar_celdas_excel(excelFilePath2, ancho_maximo, altura_maxima)