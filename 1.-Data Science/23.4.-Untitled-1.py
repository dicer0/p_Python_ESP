from PyQt5 import QtWidgets, QtGui
import sys
from Clases_Personalizadas.POO_23_3_DataBaseExcel.POO_DB_ExcelReport import DatabaseExcelHandler

class SecondaryWindow(QtWidgets.QMainWindow):
    def __init__(self, title, showTable=False):
        super().__init__() 
        self.setWindowTitle(title)
        self.__createWidgets()  # Crea los widgets constantes
        
        if showTable:
            try:
                self.__createTable()  # Crea y muestra la tabla si showTable es True
            except Exception as e:
                self.__showErrorMessageBox(str(e))  # Muestra un cuadro de diálogo con el mensaje de error
        else:
            self.__createEmptyTable()  # Crea una tabla vacía si showTable es False
        
    def __createWidgets(self):
        confirmButton = QtWidgets.QPushButton("Texto del botón")
        createButtonStyle = "max-width: 250px; height: 50px; font-size: 17px; font-weight: bold; font-family: Consolas, monospace; color: white; border-radius: 25px; background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(0,187,255), stop:1 rgb(0,125,173));"
        confirmButton.setStyleSheet(createButtonStyle)
        text_content1 =  """<p style = 'font-size: 25px; font-family: Consolas, monospace; color: white; font-weight: bold;'> 
                                Título ventana adicional 
                            </p>"""
        texto_1 = QtWidgets.QLabel(text_content1)
        text_content2 =   """<p style = 'font-size: 20px; font-family: Consolas, monospace; color: darkgray; font-weight: bold;'> 
                                Texto del botón
                            </p>"""
        texto_2 = QtWidgets.QLabel(text_content2)

        # CONTENEDORES:
        widgetContenedor = QtWidgets.QWidget()
        widgetContenedor.setFixedHeight(100)
        widgetContenedor.setStyleSheet("background-color: #002550; padding: 5px;")
        contenedorMatricial = QtWidgets.QGridLayout(widgetContenedor)   
        self.mainLayout = QtWidgets.QGridLayout()  # Usamos un QGridLayout para organizar los elementos

        # AÑADIR WIDGETS A LOS CONTENEDORES:
        contenedorMatricial.addWidget(texto_1, 0, 0)
        contenedorMatricial.addWidget(texto_2, 1, 0)
        contenedorMatricial.addWidget(confirmButton, 1, 2)
        
        # UNIR LOS CONTENEDORES EN UN SOLO WIDGET Y CENTRAR EL CONTENEDOR PRINCIPAL:
        self.mainLayout.addWidget(widgetContenedor, 1, 0)  # Agregamos el contenedor de labels y botones en la fila 1
        self.setCentralWidget(QtWidgets.QWidget())  # Creamos un widget central para el QGridLayout principal
        self.centralWidget().setLayout(self.mainLayout)
        
    def __createTable(self):
        connectionString = 'DRIVER={MySQL ODBC 8.3 Unicode Driver};SERVER=localhost;PORT=3306;DATABASE=1_platziblog_db;USER=root;PASSWORD=PincheTonto!123;'
        db_handler = DatabaseExcelHandler(connectionString)
        
        try:
            resultDataFrame = db_handler.process_data_and_save_to_excel("C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/1.-Data Science/0.-Archivos_Ejercicios_Python/23.-GUI PyQt5 Conexion DataBase/23.-Reporte Analisis de Datos.xlsx")
            if (type(resultDataFrame) == str):
                # Si hay un error al procesar los datos, mostrar un cuadro de diálogo con el mensaje de error
                self.__showErrorMessageBox(resultDataFrame)
            else:
                # Static data indicating the names of the first row of columns and the first column of rows
                static_data_above = [
                    ['Static Data Above', '', '', '', ''],  # Empty cells for spacing
                    ['', 'Static Col 1', 'Static Col 2', 'Static Col 3', ''],
                    ['Static Row 1', '', '', '', ''],
                    ['Static Row 2', '', '', '', ''],
                    ['Static Row 3', '', '', '', ''],
                    ['', '', '', '', ''],  # Empty cells for spacing
                ]
                
                static_data_below = [
                    ['', '', '', '', ''],  # Empty cells for spacing
                    ['Static Data Below', '', '', '', ''],  # Empty cells for spacing
                    ['', 'Static Col A', 'Static Col B', 'Static Col C', ''],
                    ['Static Row X', '', '', '', ''],
                    ['Static Row Y', '', '', '', ''],
                    ['Static Row Z', '', '', '', '']
                ]
                
                # Convert resultDataFrame to a list
                db_data = resultDataFrame.values.tolist()

                # Determine the number of rows and columns for the database data
                db_num_rows = len(db_data)
                db_num_cols = len(resultDataFrame.columns)

                # Create the combined data list
                combined_data = static_data_above + [['']*5] + db_data + [['']*5] + static_data_below

                # Determine the total number of rows and columns
                total_num_rows = len(combined_data)
                total_num_cols = max(5, db_num_cols)

                # Create the table
                table = QtWidgets.QTableWidget()
                table.setRowCount(total_num_rows)
                table.setColumnCount(total_num_cols)
                
                # Populate the table with database data
                for i, row_data in enumerate(db_data):
                    for j, value in enumerate(row_data):
                        item = QtWidgets.QTableWidgetItem(str(value))
                        if i == 0:
                            item.setBackground(QtGui.QColor('blue'))
                        elif j == 0 and i != 0:
                            item.setBackground(QtGui.QColor('green'))
                        elif j == 1 and i != 0:
                            item.setBackground(QtGui.QColor('gray'))
                        elif i == 0 and j == 1:
                            item.setBackground(QtGui.QColor('blue'))
                        elif i == 0 and j != 0:
                            item.setBackground(QtGui.QColor('blue'))
                        elif i != 0 and j == 0:
                            item.setBackground(QtGui.QColor('green'))
                        else:
                            item.setBackground(QtGui.QColor('yellow'))
                        table.setItem(i + len(static_data_above), j, item)  # Adjust row index to accommodate static data
                
                # Populate the table with static data above
                for i, row_data in enumerate(static_data_above):
                    for j, value in enumerate(row_data):
                        item = QtWidgets.QTableWidgetItem(str(value))
                        if value.startswith('Static Data') or value.startswith('Static Col') or value.startswith('Static Row'):
                            item.setBackground(QtGui.QColor('lightgray'))  # Color for static data
                        else:
                            item.setBackground(QtGui.QColor('white'))  # Color for empty cells
                        table.setItem(i, j, item)
                
                # Populate the table with static data below
                for i, row_data in enumerate(static_data_below):
                    for j, value in enumerate(row_data):
                        item = QtWidgets.QTableWidgetItem(str(value))
                        if value.startswith('Static Data') or value.startswith('Static Col') or value.startswith('Static Row'):
                            item.setBackground(QtGui.QColor('lightgray'))  # Color for static data
                        else:
                            item.setBackground(QtGui.QColor('white'))  # Color for empty cells
                        table.setItem(i + len(static_data_above) + db_num_rows + 1, j, item)  # Adjust row index to accommodate database data and empty row
                
                self.mainLayout.addWidget(table, 0, 0)  # Add the table to the layout
                
        except Exception as e:
            #Si ocurre un error al conectar a la base de datos o procesar los datos, mostrar un cuadro de diálogo con el mensaje de error
            self.__showErrorMessageBox(str(e))


    def __createEmptyTable(self):
        table = QtWidgets.QTableWidget()
        table.setRowCount(5)  # Definimos un número de filas arbitrario
        table.setColumnCount(5)  # Definimos un número de columnas arbitrario
        self.mainLayout.addWidget(table, 0, 0)  # Agregamos la tabla en la fila 0

    def __showErrorMessageBox(self, message):
        reply = QtWidgets.QMessageBox.critical(self, "Error", message, QtWidgets.QMessageBox.Ok)
        if reply == QtWidgets.QMessageBox.Ok:
            self.__createEmptyTable()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SecondaryWindow("Ventana 2", showTable = True)  # Puedes establecer showTable a True o False según lo necesites
    window.setStyleSheet("background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 rgb(255, 255, 255), stop:1 rgb(179, 185, 188));")
    window.showMaximized()
    app.exec_()