# -*- coding: utf-8 -*-

#PyQt5 - QtWidgets: La clase QtWidgets proporciona todos los elementos que conforman las interfaces gráficas 
#(GUI) hechas con la librería PyQt5, entre dichas herramientas se incluyen: 
# - Widgets: Elementos gráficos básicos de los que se conforma una GUI como lo son botones (QPushButton), cajas 
#   de texto (QLineEdit), texto estático (QLabel), listas desplegables (QComboBox), barras de progreso 
#   (QProgressBar), casillas de verificación (QCheckBox), imágenes (QLabel), etc.
#   - Diálogos: Los diálogos son elementos gráficos que  facilitan la interacción con el usuario, incluyen 
#     widgets como cuadros de diálogo de mensajes (QMessageBox), cuadros de diálogo para seleccionar archivos o 
#     directorios (QFileDialog), cuadros de diálogo de entrada de texto (QInputDialog), etc.
# - Layouts: Es un contenedor de PyQt5 que permite almacenar y organizar varios widgets, es el equivalente al 
#   Panel de la librería PyQt5.
#           - Widget: Es un contenedor que puede almacenar widgets directamente, proporcionando funcionalidades 
#             para mostrar, ocultar, establecer posición, tamaño, manejar eventos, etc. de los diferentes 
#             botones, checkboxes, áreas de texto, comboboxes, radiobuttons, listboxes, etc.
# - Ventana: Es la ventana principal de la GUI, que a su vez contiene todos los contenedores con los widgets que 
#   conforman la GUI, se declara a través de la clase QMainWindow de la librería pyQt5 y es el equivalente al 
#   Frame de PyQt5.
from PyQt5 import QtWidgets
#PyQt5 - QtCore: Clase que incluye métodos para trabajar con temporizadores, tamaño de elementos, fechas, 
#archivos, directorios, señales, hilos, subprocesos, etc.
from PyQt5 import QtCore
#PyQt5 - QtGui: Clase que incluye clases y métodos para trabajar con gráficos, fuentes, colores, imágenes, 
#íconos y otros elementos visuales utilizados en una interfaz gráfica (GUI) de PyQt5.
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
        self.__db_handler = db_handler       #self.__db_handler: Atributo de un objeto DatabaseExcelHandler.
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

    #__createWidgets():Método propio de la clase que sirve para declarar los widgets (botones y textos) que 
    #siempre quiero que aparezcan en la GUI.
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
        
    #__createTable():Método propio de la clase que sirve para crear y mostrar la tabla que contiene los datos 
    #extraídos de la database.
    def __createTable(self):
        #EXTRAER DATOS DE LA BASE DE DATOS Y CREAR UN REPORTE EN EXCEL:
        try:
            #DatabaseExcelHandler.process_data_and_save_to_excel(): Método de nuestra clase DatabaseExcelHandler,
            #el cual sirve para procesar los datos recopilados de una base de datos y guardarlos en cierto 
            #directorio en un archivo de Excel.
            resultDataFrame = self.__db_handler.process_data_and_save_to_excel(self.__excelFilePath)
            print("Tipo de dato database: ", type(resultDataFrame))
            print(resultDataFrame)
            #Se detecta que ha ocurrido un error cuando resultDataFrame es de tipo string, en vez de DataFrame. 
            if (type(resultDataFrame) == str):
                #Si pasa un error al procesar los datos, se mostrará un cuadro de diálogo con un mensaje.
                self.__showErrorMessageBox(resultDataFrame)
            else:
                #DATOS ESTÁTICOS QUE SE VAN A COLOCAR ENCIMA Y DEBAJO DEL REPORTE EXTRAÍDO DEL DATABASE:
                staticDataAbove_1 = [
                    ['Title A1.1', 'Title A1.2', 'Title A1.3'],
                    ['Static Row 1', '', ''],
                    ['Static Row 2', '', ''],
                    ['Static Row 3', '', ''],
                    ['Static Row 4', '', ''],
                    ['Static Row 5', '', ''],
                    ['Static Row 6', '', '']
                ]
                staticDataBelow_1 = [
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
                #TAMAÑO DE LA TABLA QUE CONTIENE TODAS LAS AGRUPACIONES DE DATOS:
                #pandas.DataFrame().shape: Para extraer el tamaño de un DataFrame se puede utilizar el atributo 
                #shape de la clase DataFrame, el cual devuelve una tupla que indica su número de filas y 
                #columnas: (filas, columnas) = pandas.DataFrame().shape
                (db_numRows, db_numCols) = resultDataFrame.shape
                #Para obtener el tamaño total de la tabla, se considera el tamaño de la lista de listas que 
                #indican los datos estáticos y el número de filas del DataFrame.
                totalRows = len(staticDataAbove_1) + db_numRows + len(staticDataBelow_1)   #Filas tabla.
                #max(): Este método retorna el valor que sea mayor al comparar dos números.
                totalCols = max(7, db_numCols)                                             #Columnas tabla.
                #QtWidgets.QTableWidget(): Widget que proporciona una funcionalidad de hoja de cálculo o tabla 
                #editable para mostrar filas y columnas de información en una GUI de PyQt5, las cuales pueden 
                #contener texto, números, imágenes u otros widgets.
                table = QtWidgets.QTableWidget()
                #QtWidgets.QTableWidget().setRowCount() y setColumnCount(): Métodos que sirven para indicar el 
                #número de filas y columnas de un objeto QTableWidget() en una GUI, en sus parámetros reciben 
                #dicho tamaño.
                table.setRowCount(totalRows)
                table.setColumnCount(totalCols)

                #Establecer colores para filas y columnas de la tabla con datos estáticos que se encuentren arriba de 
                #los datos extraídos por la database.
                #enumerate(): Es un método que devuelve tanto el índice como el valor de los elementos de una lista, 
                #tupla u otro iterable.
                for (i, row_data) in (enumerate(staticDataAbove_1)):
                    for j, value in enumerate(row_data):
                        item = QtWidgets.QTableWidgetItem(str(value))
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        if i == 0:
                            item.setBackground(QtGui.QColor('red'))
                            item.setTextAlignment(QtCore.Qt.AlignCenter)
                            table.setSpan(i, 0, 1, 5)
                        elif j == 0:
                            item.setBackground(QtGui.QColor('aqua'))
                        elif j == 1:
                            item.setBackground(QtGui.QColor('darkgray'))
                        else:
                            item.setBackground(QtGui.QColor('white'))
                        table.setItem(i, j, item)

                #Establecer colores para filas y columnas de la tabla con datos extraídos del database. 
                #Para ello se debe hacer uso del objeto QTableWidgetItem que accede a cada celda de la tabla de 
                #forma individual y además se debe obtener todos los valores del DataFrame que contiene los datos 
                #del database para que estos se puedan colocar en la tabla y además darles color.
                for i in range(db_numRows):       #Bucle for que recorre las filas = i.
                    for j in range(db_numCols):   #Bucle for que recorre las columnas = j.
                        #QtWidgets.QTableWidgetItem(): Es una clase de PyQt5 que representa una celda individual 
                        #dentro de una tabla QTableWidget. Este elemento puede contener datos y proporcionar 
                        #funcionalidades para editar su formato (color, letra, etc.) dentro de una tabla en la 
                        #interfaz de usuario. En su constructor debe recibir el dato que mostrará cada celda en 
                        #forma de string.
                        #pandas.DataFrame.iloc[filas, columnas]: El método iloc sirve para acceder a uno o varios 
                        #de los valores de un DataFrame a través de sus filas y/o columnas contando desde 0. 
                        #Por ejemplo:
                        # - DataFrame.iloc[0]: Selecciona la primera fila del DataFrame.
                        # - DataFrame.iloc[:, 0]: Selecciona la primera columna del DataFrame.
                        # - DataFrame.iloc[0:5, :]: Selecciona las primeras cinco filas del DataFrame.
                        # - DataFrame.iloc[:, 0:2]: Selecciona las dos primeras columnas del DataFrame.
                        celdaTabla = QtWidgets.QTableWidgetItem(str(resultDataFrame.iloc[i, j]))
                        if (i == 0):                    #Color azul:    Fila 1 = (0, Ninguna Columna)
                            #QtWidgets.QTableWidgetItem().setBackground(): Este método se utiliza para indicar el
                            #color de fondo de un objeto QTableWidgetItem(), que representa una celda de una 
                            #tabla QTableWidget(), este siempre recibe como parámetro un objeto QtGui.QColor(), 
                            #el cual a su vez recibe como parámetro el color de fondo en formato rgb, hexadecimal
                            #o string.
                            celdaTabla.setBackground(QtGui.QColor('blue'))
                        elif (i != 0 and j == 0):       #Color verde:   Columna 1 = (Todas las filas menos la primera, 0)
                            celdaTabla.setBackground(QtGui.QColor('green'))
                        elif (i != 0 and j == 1):       #Color gris:    Columna 2 = (Todas las filas menos la primera, 1)
                            celdaTabla.setBackground(QtGui.QColor('gray'))
                        else:                           #Color amarillo: Todas las demás celdas.
                            celdaTabla.setBackground(QtGui.QColor('yellow'))
                        #QtWidgets.QTableWidget().setItem(): El método setItem() se aplica a un objeto 
                        #QTableWidget() y se utiliza para establecer un objeto QTableWidgetItem() en una posición 
                        #específica dentro de una tabla.
                        table.setItem(i, j, celdaTabla)
                
                #Establecer colores para filas y columnas de la tabla con datos estáticos que se encuentren arriba de 
                #los datos extraídos por la database.
                
                
                #QtWidgets.QGridLayout(): La variable self.contenedorVertical es un contenedor matricial, y a 
                #través de indicar que la tabla se coloque en la posición (0,0) nos aseguramos que aunque la 
                #tabla se cree después que el contenedor que tiene los demás widgets, esta se coloque hasta 
                #arriba dentro de la GUI. 
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
    #mensaje de error que recibe de la clase DatabaseExcelHandler, ya sea cuando ocurrió un error al 
    #conectarse a la base de datos o cuando ocurrió un error al procesar/guardar los datos en un Excel.
    def __showErrorMessageBox(self, message):
        reply = QtWidgets.QMessageBox.critical(self, "Error", message, QtWidgets.QMessageBox.Ok)
        if reply == QtWidgets.QMessageBox.Ok:
            self.__createEmptyTable()