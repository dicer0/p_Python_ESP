# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5 import QtGui
import sys #sys: Librería que permite interactuar directamente con el sistema operativo y consola del ordenador.

#SecondaryWindow: Clase que representa las ventanas adicionales abiertas en la GUI, a través de ella se 
#pueden crear instancias que abran ventanas distintas, esta recibe un parámetro que nombra cada ventana.
class SecondaryWindow(QtWidgets.QMainWindow):
    #__init__(): Constructor de la clase SecondaryWindow.
    def __init__(self, title, db_handler, excelFilePath, showTable = False):
        super().__init__()                          #super(): Herencia de la clase QtWidgets.QMainWindow.
        #ATRIBUTOS PRIVADOS DEL CONSTRUCTOR:
        #Los métodos o atributos cuyo nombre empieza con dos guiones bajos __, indican que son métodos privados, 
        #osea que solo pueden ser accedidos desde dentro de la clase, pero no desde fuera.
        #Inyección de dependencias: Este es un concepto utilizado cuando una clase para funcionar necesita el 
        #objeto de otra clase, en este caso para que la clase SecondaryWindow funcione, necesita de un objeto 
        #DatabaseExcelHandler, a esto se le llama inyección de dependencias.
        self.__db_handler = db_handler       #self.__db_handler: Atributo que recibe un objeto DatabaseExcelHandler.
        self.__excelFilePath = excelFilePath #self.__excelFilePath: Atributo que indica el directorio del Excel.
        #MÉTODOS EJECUTADOS POR DEFECTO EN EL CONSTRUCTOR:
        self.setWindowTitle(title)                  #Título de la ventana, que recibe la clase como parámetro.
        self.__createWidgets()                      #__createWidgets(): Método que crea los widgets constantes.
        #Condicional que evalúa si se desea mostrar la tabla con datos llenados por default o no.
        if showTable == True:
            #MANEJO DE EXCEPCIONES: Es una parte de código que se conforma de 2 o3 partes, try, except y finally: 
            # - Primero se ejecuta el código que haya dentro del try, y si es que llegara a ocurrir una excepción 
            #   durante su ejecución, el programa brinca al código del except.
            # - En la parte de código donde se encuentra la palabra reservada except, se ejecuta cierta acción 
            #   cuando ocurra el error esperado.
            # - Por último, cuando no ocurra una excepción durante la ejecución del gestor de excepciones, se 
            #   ejecutará el código que esté incluido dentro del finally después de haber terminado de ejecutar 
            #   lo que haya en el try, pero si ocurre una excepción, la ejecución terminará cuando se llegue al 
            #   except.
            try:
                #__createTable(): Método que crea la tabla rellena de datos cuando el parámetro showTable = True
                self.__createTable()
            #Si ocurre un error al abrir la base de datos o procesar los datos, se mostrará un mensaje de error.
            except Exception as errorDatabaseExcelHandler:
                #__showErrorMessageBox(): Método que muestra un cuadro de diálogo con el mensaje de error en 
                #forma de string, devuelto por el constructor de la clase propia DatabaseExcelHandler cuando el 
                #programa no se pudo conectar con la base de datos o cuando no pudo procesar o guardar dichos 
                #datos.
                self.__showErrorMessageBox(str(errorDatabaseExcelHandler))
        else:
            #__createEmptyTable(): Método de esta clase que crea una tabla vacía cuando ocurre un error o 
            #simplemente cuando no se quiere mostrar la tabla que incluye los datos.
            self.__createEmptyTable()

    def __createWidgets(self):
        #CREACIÓN DE WIDGETS DE LAS VENTANAS ADICIONALES, QUE NO SON LA TABLA:
        confirmButton = QtWidgets.QPushButton("Texto del botón")    #Botón.
        createButtonStyle = "max-width: 250px; height: 50px; font-size: 17px; font-weight: bold; font-family: Consolas, monospace; color: white; border-radius: 25px; background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(0,187,255), stop:1 rgb(0,125,173));"
        confirmButton.setStyleSheet(createButtonStyle)              #Estilo del botón.
        text_content1 =  """<p style = 'font-size: 25px; font-family: Consolas, monospace; color: white; font-weight: bold;'> 
                                Título ventana adicional 
                            </p>"""
        texto_1 = QtWidgets.QLabel(text_content1)                   #Texto indicativo.
        text_content2 =   """<p style = 'font-size: 20px; font-family: Consolas, monospace; color: darkgray; font-weight: bold;'> 
                                Texto del botón
                            </p>"""
        texto_2 = QtWidgets.QLabel(text_content2)                   #Texto indicativo.

        #CONTENEDORES:
        widgetContenedor = QtWidgets.QWidget()              #Widget que contiene al Layout inferior.
        widgetContenedor.setFixedHeight(100)                #setFixedHeight(): Altura fija para un Widget.
        widgetContenedor.setStyleSheet("background-color: #002550; padding: 5px;")
        #Contenedor con organización matricial (fila, col).
        contenedorMatricial = QtWidgets.QGridLayout(widgetContenedor)   
        self.contenedorVertical = QtWidgets.QGridLayout()

        #AÑADIR WIDGETS A LOS CONTENEDORES:
        #------------------------------------------CONTENEDOR MATRICIAL------------------------------------------
        contenedorMatricial.addWidget(texto_1, 0, 0)        #Añadir texto a la posición matricial (0,0).
        contenedorMatricial.addWidget(texto_2, 1, 0)        #Añadir texto a la posición matricial (1,0).
        contenedorMatricial.addWidget(confirmButton, 1, 2)  #Añadir botón a la posición matricial (1,2).
        #------------------------------------------CONTENEDOR MATRICIAL------------------------------------------
        #-------------------------------------------CONTENEDOR VERTICAL------------------------------------------
        self.contenedorVertical.addWidget(widgetContenedor, 1, 0)   #Añadir el contenedor a la posición (1,0).
        #-------------------------------------------CONTENEDOR VERTICAL------------------------------------------
        
        #UNIR LOS CONTENEDORES EN UN SOLO WIDGET Y CENTRAR EL CONTENEDOR PRINCIPAL:
        centralWidget = QtWidgets.QWidget()                 #Widget que incluye todos los contenedores.
        centralWidget.setLayout(self.contenedorVertical)    #Layout principal metido en un widget para centrarlo.
        self.setCentralWidget(centralWidget)                #Centralización del widget principal.
        
    def __createTable(self):
        #EXTRAER DATOS DE LA BASE DE DATOS Y CREAR UN REPORTE EN EXCEL:
        try:
            #DatabaseExcelHandler.process_data_and_save_to_excel(): Método de nuestra clase DatabaseExcelHandler,
            #el cual sirve para procesar los datos recopilados de una base de datos y guardarlos en cierto 
            #directorio en un archivo de Excel.
            resultDataFrame = self.__db_handler.process_data_and_save_to_excel(self.__excelFilePath)
            print(resultDataFrame)
            if (type(resultDataFrame) == str):
                #Si pasa un error al procesar los datos, se mostrará un cuadro de diálogo con un mensaje.
                self.__showErrorMessageBox(resultDataFrame)
            else:
                #QtWidgets.QTableWidget(): Widget que proporciona una funcionalidad de hoja de cálculo o tabla 
                #editable para mostrar filas y columnas de información en una GUI de PyQt5, las cuales pueden 
                #contener texto, números, imágenes u otros widgets.
                table = QtWidgets.QTableWidget()
                headers = resultDataFrame.columns.tolist()
                resultDataFrame.loc[-1] = headers
                resultDataFrame.index = resultDataFrame.index + 1
                resultDataFrame = resultDataFrame.sort_index()
                num_rows, num_cols = resultDataFrame.shape
                table.setRowCount(num_rows)
                table.setColumnCount(num_cols)
                # Establecer colores para las filas y columnas
                for i in range(num_rows):
                    for j in range(num_cols):
                        item = QtWidgets.QTableWidgetItem(str(resultDataFrame.iloc[i, j]))
                        if i == 0:
                            item.setBackground(QtGui.QColor('blue'))
                        elif j == 0 and i != 0:
                            item.setBackground(QtGui.QColor('green'))
                        elif j == 1 and i != 0:  # Solo la segunda columna, excluyendo la primera fila
                            item.setBackground(QtGui.QColor('gray'))
                        elif i == 0 and j == 1:
                            item.setBackground(QtGui.QColor('blue'))  # Para la esquina superior derecha
                        elif i == 0 and j != 0:
                            item.setBackground(QtGui.QColor('blue'))  # Para la primera fila
                        elif i != 0 and j == 0:
                            item.setBackground(QtGui.QColor('green'))  # Para la primera columna
                        else:
                            item.setBackground(QtGui.QColor('yellow'))
                        table.setItem(i, j, item)
                self.contenedorVertical.addWidget(table, 0, 0)  #Añadir la tabla a la posición (0,0).
        #Si ocurre un error al conectar a la base de datos o procesar los datos, se mostrará un cuadro de diálogo 
        #con el mensaje de error.
        except Exception as errorDatabaseExcelHandler:
            self.__showErrorMessageBox(str(errorDatabaseExcelHandler))
    #__createEmptyTable(): Método que crea una tabla vacía cuando showTable = False o cuando ocurra un error al 
    #conectarse a la base de datos o al procesarlos/guardarlos en un Excel.
    def __createEmptyTable(self):
        table = QtWidgets.QTableWidget()
        table.setRowCount(5)        #Número de filas arbitrario.
        table.setColumnCount(5)     #Número de columnas arbitrario.
        self.contenedorVertical.addWidget(table, 0, 0)          #Añadir la tabla vacía a la posición (0,0).
    #__showErrorMessageBox(): Método que se utiliza para mostrar una ventana de diálogo, la cual indica un 
    #mensaje de error.
    def __showErrorMessageBox(self, message):
        reply = QtWidgets.QMessageBox.critical(self, "Error", message, QtWidgets.QMessageBox.Ok)
        if reply == QtWidgets.QMessageBox.Ok:
            self.__createEmptyTable()