import xlwings as xw
import time

def copy_excel_data_to_clipboard(file_path, delay=5):
    # Abre el libro de Excel
    wb = xw.Book(file_path)
    
    # Copia cada hoja de cálculo al portapapeles
    for sheet in wb.sheets:
        sheet.range('A1').select()
        sheet.api.UsedRange.Copy()
    
    # Espera un tiempo antes de cerrar el libro de Excel
    time.sleep(delay)
    
    # Cierra el libro de Excel después de copiar los datos
    wb.close()

# Ejemplo de uso
excelFilePath2 = "C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/1.-Data Science/0.-Archivos_Ejercicios_Python/23.-GUI PyQt5 Conexion DataBase/23.-Reporte Analisis de Datos 2.xlsx"
copy_excel_data_to_clipboard(excelFilePath2, delay=10)  # Delay set to 10 seconds