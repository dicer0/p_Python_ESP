# -*- coding: utf-8 -*-

import xlwings
import time
from PyQt5 import QtCore

class ExcelDataCopier(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)

    def __init__(self, file_path, delay):
        super().__init__()
        self.file_path = file_path
        self.workBook = None
        self.delay = delay
        self.countdown_message = None

    def copy_data_to_clipboard(self):
        self.workBook = xlwings.Book(self.file_path)
        print("Libro de Excel abierto:\t\t", self.workBook.app.books)
        print("Hojas del Excel abierto:\t", self.workBook.sheets)
        self.workBook.app.visible = False
        self.workBook.app.display_alerts = False
        for sheet in self.workBook.sheets:
            sheet.select()
            sheet.api.UsedRange.Copy()
        
        for remaining in range(self.delay, 0, -1):
            self.countdown_message = f"Countdown: {remaining} seconds"  # Actualiza el mensaje de conteo
            self.signal.emit(self.countdown_message)
            print(self.countdown_message, end = "\r")
            time.sleep(1)
        self.countdown_message = "Countdown finished. Closing Excel..."
        print(self.countdown_message)
        self.signal.emit(self.countdown_message)
        
        try:
            self.workBook.close()
        except Exception as e:
            print(f"An error occurred while closing the Excel file: {e}")
        
        for app in xlwings.apps:
            app.quit()

excelFilePath2 = "C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/1.-Data Science/0.-Archivos_Ejercicios_Python/23.-GUI PyQt5 Conexion DataBase/23.-Reporte Analisis de Datos 1.xlsx"
copier = ExcelDataCopier(excelFilePath2, delay=10)
copier.copy_data_to_clipboard()