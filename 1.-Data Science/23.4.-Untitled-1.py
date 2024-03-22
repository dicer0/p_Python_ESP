from PyQt5 import QtWidgets, QtGui, QtCore
import sys
from Clases_Personalizadas.POO_23_3_DataBaseExcel.POO_DB_ExcelReport import DatabaseExcelHandler

class SecondaryWindow(QtWidgets.QMainWindow):
    def __init__(self, title, showTable=False):
        super().__init__() 
        self.setWindowTitle(title)
        self.__createWidgets()
        
        if showTable:
            try:
                self.__createTable()
            except Exception as e:
                self.__showErrorMessageBox(str(e))
                print("Error: ", e)
        else:
            self.__createEmptyTable()
        
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
        self.mainLayout = QtWidgets.QGridLayout()

        # AÑADIR WIDGETS A LOS CONTENEDORES:
        contenedorMatricial.addWidget(texto_1, 0, 0)
        contenedorMatricial.addWidget(texto_2, 1, 0)
        contenedorMatricial.addWidget(confirmButton, 1, 2)
        
        # UNIR LOS CONTENEDORES EN UN SOLO WIDGET Y CENTRAR EL CONTENEDOR PRINCIPAL:
        self.mainLayout.addWidget(widgetContenedor, 1, 0)
        centralWidget = QtWidgets.QWidget()
        centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(centralWidget)
        
    def __createTable(self):
        connectionString = 'DRIVER={MySQL ODBC 8.3 Unicode Driver};SERVER=localhost;PORT=3306;DATABASE=1_platziblog_db;USER=root;PASSWORD=PincheTonto!123;'
        db_handler = DatabaseExcelHandler(connectionString)
        
        try:
            resultDataFrame = db_handler.process_data_and_save_to_excel("C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/1.-Data Science/0.-Archivos_Ejercicios_Python/23.-GUI PyQt5 Conexion DataBase/23.-Reporte Analisis de Datos 1.xlsx")
            if (type(resultDataFrame) == str):
                self.__showErrorMessageBox(resultDataFrame)
            else:
                staticDataAbove_1 = [
                    ['Title A1.1', 'Title A1.2', 'Title A1.3'],
                    ['Static Row 1', '', ''],
                    ['Static Row 2', '', ''],
                    ['Static Row 3', '', ''],
                    ['Static Row 4', '', ''],
                    ['Static Row 5', '', ''],
                    ['Static Row 6', '', '']
                ]
                staticDataAbove_2 = [
                    ['Title A2', '', '', '', '', '', ''],
                    ['Subtitle A2.1', '', '', '', '', '', ''],
                    ['Static Row 1', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', ''],
                    ['Subtitle A2.2', '', '', '', '', '', ''],
                    ['Static Row 2', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', ''],
                    ['Subtitle A2.3', '', '', '', '', '', ''],
                    ['Static Row 3', '', '', '', '', '', ''],
                    ['', '', '', '', '', '', ''],
                    ['Static Text: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque non laoreet mauris. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Curabitur vulputate bibendum nibh elementum pulvinar. Integer a leo in orci ultricies fermentum. Ut vitae velit et sapien congue accumsan sed tincidunt dui. Ut elementum imperdiet nunc, non hendrerit enim ultrices at. Sed rhoncus vehicula.', '', '', '', '', '', '']
                ]
                staticDataBelow_1 = [
                    ['Title B1', '', '', '', '', '', ''],
                    ['Title B1.1', 'Title B1.2', 'Title B1.3', 'Title B1.4', 'Title B1.5', 'Title B1.6', 'Title B1.7'],
                    ['Subtitle 1', '', '', '', '', '', ''],
                    ['Static Row 1', '', '', '', '', '', ''],
                    ['Static Row 2', '', '', '', '', '', ''],
                    ['Static Row 3', '', '', '', '', '', ''],
                    ['Static Row 4', '', '', '', '', '', ''],
                    ['Static Row 5', '', '', '', '', '', ''],
                    ['Static Row 6', '', '', '', '', '', ''],
                    ['Static Row 7', '', '', '', '', '', ''],
                    ['Subtitle 2', '', '', '', '', '', ''],
                    ['Static Row 1', '', '', '', '', '', '']
                ]
                (db_numRows, db_numCols) = resultDataFrame.shape
                totalRows = len(staticDataAbove_1) + len(staticDataAbove_2) + db_numRows + len(staticDataBelow_1)
                staticDataAbove_1_Rows = len(staticDataAbove_1)
                staticDataAbove_2_Rows = len(staticDataAbove_2)
                totalCols = max(7, db_numCols)
                staticDataAbove_1_Cols = len(staticDataAbove_1[0]) 
                staticDataAbove_2_Cols = len(staticDataAbove_2[0]) 
                staticDataBelow_1_Cols = len(staticDataBelow_1[0]) 
                table = QtWidgets.QTableWidget()
                table.setRowCount(totalRows)
                table.setColumnCount(totalCols)

                for (i, row_data) in (enumerate(staticDataAbove_1)):
                    for (j, value) in (enumerate(row_data)): 
                        itemAbove1 = QtWidgets.QTableWidgetItem(str(value)) 
                        itemAbove1.setTextAlignment(QtCore.Qt.AlignCenter)
                        if i == 0:
                            itemAbove1.setBackground(QtGui.QColor('#4f81bd'))
                            font = QtGui.QFont()
                            font.setBold(True)
                            itemAbove1.setFont(font)
                            itemAbove1.setForeground(QtGui.QColor('white'))
                            table.setSpan(i, 1, 1, staticDataAbove_1_Cols)
                        elif (i != 0 and j == 1):
                            itemAbove1.setBackground(QtGui.QColor('#0070c0'))
                        else:                          
                            itemAbove1.setBackground(QtGui.QColor('#d3dfee'))   
                            font = QtGui.QFont() 
                            font.setBold(True)
                            itemAbove1.setFont(font)
                        table.setItem(i, (j + 1), itemAbove1)
                for (i, row_data) in (enumerate(staticDataAbove_2)): 
                    for (j, value) in (enumerate(row_data)): 
                        itemAbove2 = QtWidgets.QTableWidgetItem(str(value)) 
                        itemAbove2.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                        font = QtGui.QFont() 
                        font.setBold(True)
                        table.setSpan((i + staticDataAbove_1_Rows + 1), 0, 1, staticDataAbove_2_Cols)
                        if i == 0:
                            itemAbove2.setBackground(QtGui.QColor('#4f81bd'))
                            itemAbove2.setFont(font)
                        elif (i == 1 or i == 4 or i == 7):
                            itemAbove2.setBackground(QtGui.QColor('white'))  
                            font.setUnderline(True)
                            itemAbove2.setFont(font)
                        else:
                            itemAbove2.setBackground(QtGui.QColor('white'))  
                        table.setItem((i + staticDataAbove_1_Rows + 1), j, itemAbove2)

                for i in range(db_numRows): 
                    for j in range(db_numCols): 
                        celda_Db = QtWidgets.QTableWidgetItem(str(resultDataFrame.iloc[i, j]))
                        celda_Db.setTextAlignment(QtCore.Qt.AlignCenter)
                        font = QtGui.QFont() 
                        font.setBold(True)
                        if (i == 0): 
                            celda_Db.setBackground(QtGui.QColor('blue'))     
                            celda_Db.setFont(font)
                        elif (i != 0 and j == 0): 
                            celda_Db.setBackground(QtGui.QColor('green'))
                            celda_Db.setFont(font)
                        elif (i != 0 and j == 1): 
                            celda_Db.setBackground(QtGui.QColor('gray'))
                        else:
                            celda_Db.setBackground(QtGui.QColor('yellow'))
                        table.setItem((i + staticDataAbove_1_Rows + staticDataAbove_2_Rows + 1 + 1), j, celda_Db)
                
                for i, row_data in enumerate(staticDataBelow_1): 
                    for j, value in enumerate(row_data): 
                        itemBelow1 = QtWidgets.QTableWidgetItem(str(value)) 
                        itemBelow1.setTextAlignment(QtCore.Qt.AlignCenter)
                        font = QtGui.QFont() 
                        font.setBold(True)
                        if i == 0:
                            itemBelow1.setBackground(QtGui.QColor('white'))
                            font.setUnderline(True)
                            itemBelow1.setFont(font)
                            itemBelow1.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                            table.setSpan((i + staticDataAbove_1_Rows + staticDataAbove_2_Rows + db_numRows + 1 + 1 + 1), 0, 1, staticDataBelow_1_Cols)
                        elif i == 1:
                            itemBelow1.setBackground(QtGui.QColor('#4472c4'))
                            itemBelow1.setFont(font)
                        elif i == 2:
                            itemBelow1.setBackground(QtGui.QColor('#A7BFDE'))
                            itemBelow1.setFont(font)
                            table.setSpan((i + staticDataAbove_1_Rows + staticDataAbove_2_Rows + db_numRows + 1 + 1 + 1), 0, 1, staticDataBelow_1_Cols)
                        elif (i != (0 & 1 & 2) and j == 0):
                            itemBelow1.setBackground(QtGui.QColor('#5EC268'))
                            itemBelow1.setFont(font)
                        elif (i != (0 & 1 & 2) and j == 1):
                            itemBelow1.setBackground(QtGui.QColor('gray'))
                        else:
                            itemBelow1.setBackground(QtGui.QColor('#FFF2CC'))
                        table.setItem((i + staticDataAbove_1_Rows + staticDataAbove_2_Rows + db_numRows + 1 + 1 + 1), j, itemBelow1)
                
                # #REDIMENSIONAR EL ANCHO DE LAS CELDAS DE LAS COLUMNAS PARA MOSTRAR SU CONTENIDO COMPLETO:
                # #QtWidgets.QTableWidget().columnCount(): El método columnCount() devuelve un número entero que 
                # #representa el número de columnas de un objeto QtWidgets.QTableWidget().
                # for column in range(table.columnCount()):
                #     #QtWidgets.QTableWidget().resizeColumnToContents(): Este método se utiliza para ajustar 
                #     #automáticamente el ancho de la columna de una tabla QtWidgets.QTableWidget().  
                #     table.resizeColumnToContents(column)
                #     #QtWidgets.QTableWidget().setColumnWidth(): Cuando el método resizeColumnToContents() por 
                #     #alguna razón no haya redimensionado automáticamente de forma correcta el ancho de una 
                #     #columna, esto se puede forzar a través del método setColumnWidth(), en el cual se indica
                #     #el índice de la columna contando desde cero en su primer parámetro y el ancho en pixeles 
                #     #en su segundo parámetro.
                #     table.setColumnWidth(3, 400)
                
                self.mainLayout.addWidget(table, 0, 0)
        except Exception as errorDatabaseExcelHandler:
            self.__showErrorMessageBox(str(errorDatabaseExcelHandler))
    
    def __createEmptyTable(self):
        table = QtWidgets.QTableWidget()
        table.setRowCount(5)
        table.setColumnCount(5)
        self.contenedorVertical.addWidget(table, 0, 0)
        
    def __showErrorMessageBox(self, message):
        reply = QtWidgets.QMessageBox.critical(self, "Error", message, QtWidgets.QMessageBox.Ok)
        if reply == QtWidgets.QMessageBox.Ok:
            self.__createEmptyTable()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SecondaryWindow("Ventana 2", showTable=True)
    window.setStyleSheet("background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 rgb(255, 255, 255), stop:1 rgb(179, 185, 188));")
    window.showMaximized()
    sys.exit(app.exec_())
