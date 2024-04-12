import xlwings
import time

def copy_excel_data_to_clipboard(file_path, delay=5):
    # Abre el libro de Excel
    workBook = xlwings.Book(file_path)
    
    # Copia cada hoja de cálculo al portapapeles
    for sheet in workBook.sheets:
        sheet.range('A1').select()
        sheet.api.UsedRange.Copy()
    
    # Countdown timer
    for remaining in range(delay, 0, -1):
        print(f"Countdown: {remaining} seconds", end="\r")
        time.sleep(1)
    
    print("Countdown finished. Closing Excel...")
    
    # Try to close the Excel file
    try:
        # Set DisplayAlerts to False to suppress pop-up messages
        workBook.app.display_alerts = False
        workBook.close()
    except Exception as e:
        print(f"An error occurred while closing the Excel file: {e}")
    
    # Quit the Excel application
    for app in xlwings.apps:
        app.quit()

# Ejemplo de uso
excelFilePath2 = "C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/1.-Data Science/0.-Archivos_Ejercicios_Python/23.-GUI PyQt5 Conexion DataBase/23.-Reporte Analisis de Datos 1.xlsx"
copy_excel_data_to_clipboard(excelFilePath2, delay = 10)  # Delay set to 10 seconds