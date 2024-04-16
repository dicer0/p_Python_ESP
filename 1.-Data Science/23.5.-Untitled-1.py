import xlwings
import time
from PyQt5 import QtCore
import psutil
import subprocess

class ExcelDataCopier(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)

    def __init__(self, file_path, delay_segs):
        super().__init__()
        self.file_path = file_path
        self.workBook = None
        self.delay = delay_segs
        self.countdown_message = "Bienvenido"

    def check_excel_open(self):
        for proc in psutil.process_iter():
            try:
                if "EXCEL.EXE" in proc.name():
                    for file in proc.open_files():
                        if self.file_path == file.path:
                            return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False

    def close_excel(self):
        try:
            if self.workBook:
                for app in xlwings.apps:
                    app.quit()
                subprocess.Popen('taskkill /f /im EXCEL.EXE', shell=True)
                time.sleep(2)  # Esperar un momento para que Excel se cierre completamente
        except Exception as e:
            print(f"Error al cerrar Excel: {e}")
            self.signal.emit(f"Error al cerrar Excel: {e}")

    def run(self):
        if self.check_excel_open():
            self.countdown_message = "El archivo de Excel está abierto. Cerrándolo..."
            print(self.countdown_message)
            self.signal.emit(self.countdown_message)
            try:
                for proc in psutil.process_iter():
                    if "EXCEL.EXE" in proc.name():
                        for file in proc.open_files():
                            if self.file_path == file.path:
                                proc.terminate()
                                break
            except Exception as e:
                print(f"Error al cerrar el archivo de Excel: {e}")
                self.signal.emit(f"Error al cerrar el archivo de Excel: {e}")

        self.close_excel()

        # Ahora podemos abrir el archivo de Excel
        try:
            self.workBook = xlwings.Book(self.file_path)
            print("Libro de Excel abierto:\t\t", self.workBook.app.books)
            print("Hojas del Excel abierto:\t", self.workBook.sheets)
            self.workBook.app.visible = False
            self.workBook.app.display_alerts = False
            for sheet in self.workBook.sheets:
                sheet.select()
                sheet.api.UsedRange.Copy()
        except Exception as e:
            print(f"Error al abrir el archivo de Excel: {e}")
            self.signal.emit(f"Error al abrir el archivo de Excel: {e}")
            return

        for remaining in range(self.delay, 0, -1):
            self.countdown_message = f"Countdown: {remaining} segundos"
            self.signal.emit(self.countdown_message)
            print(self.countdown_message, end="\r")
            time.sleep(1)
        self.countdown_message = "Countdown finalizado. Cerrando Excel..."
        print(self.countdown_message)
        self.signal.emit(self.countdown_message)

        try:
            if self.workBook:
                self.workBook.close()
        except Exception as e:
            print(f"Error al cerrar el archivo de Excel: {e}")
            self.signal.emit(f"Error al cerrar el archivo de Excel: {e}")

        self.close_excel()

excelFilePath2 = "C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/1.-Data Science/0.-Archivos_Ejercicios_Python/23.-GUI PyQt5 Conexion DataBase/23.-Reporte Analisis de Datos 1.xlsx"
copier = ExcelDataCopier(excelFilePath2, delay_segs=10)
copier.run()