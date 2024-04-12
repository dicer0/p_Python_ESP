# -*- coding: utf-8 -*-

#pyinstaller nombreArchivo.py --onefile --windowed --icon=path/icono.ico
#pyinstaller: Es una librería que se utiliza para convertir un programa de Python a un archivo .exe.
#--onefile: Sirve para que cuando se ejecute el comando de pyinstaller, se cree un solo archivo ejecutable.
#--windowed: Sirve para que cuando se ejecute el ejecutable, no se abra la consola.
#--icon=path/icono.ico: Sirve para asignar un ícono al .exe, pero para ello el archivo debe tener extensión .ico.

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
        #------------------------------------------CONTENEDOR MATRICIAL-------------------------------------------
        contenedorMatricial.addWidget(texto_1, 0, 0)        #Añadir texto a la posición matricial (0,0).
        contenedorMatricial.addWidget(texto_2, 1, 0)        #Añadir texto a la posición matricial (1,0).
        contenedorMatricial.addWidget(confirmButton, 1, 2)  #Añadir botón a la posición matricial (1,2).
        #------------------------------------------CONTENEDOR MATRICIAL-------------------------------------------
        #-------------------------------------------CONTENEDOR VERTICAL-------------------------------------------
        self.contenedorVertical.addWidget(widgetContenedor, 1, 0)   #Añadir el contenedor a la posición (1,0).
        #-------------------------------------------CONTENEDOR VERTICAL-------------------------------------------
        
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
                STATICDATA_ABOVE_1 = [
                    ['Title A1.1', 'Title A1.2', 'Title A1.3'],
                    ['Static Row 1', '', ''],
                    ['Static Row 2', '', ''],
                    ['Static Row 3', '', ''],
                    ['Static Row 4', '', ''],
                    ['Static Row 5', '', ''],
                    ['Static Row 6', '', '']
                ]
                STATICDATA_ABOVE_2 = [
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
                STATICDATA_BELOW_1 = [
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
                #TAMAÑO DE LA TABLA QUE CONTIENE TODAS LAS AGRUPACIONES DE DATOS:
                #pandas.DataFrame().columns: El atributo .columns devuelve un objeto de tipo Index que representa 
                #los nombres de las columnas de un DataFrame. Los objetos Index de igual manera se pueden utilizar
                #de forma opcional para nombrar las filas, no solo las columnas. 
                headers = resultDataFrame.columns       #Extraer objetos Index que dicen el nombre de las columnas.
                #pandas.DataFrame().loc[]: El método .loc[] sirve para extraer o seleccionar datos dentro de un 
                #DataFrame de las siguientes distintas formas:
                # - Selección de filas y columnas por etiqueta (objeto Index): El método .loc[] se puede utilizar 
                #   para seleccionar un subconjunto de filas y columnas de un DataFrame, esto se puede realizar 
                #   indicando sus etiquetas de fila y columna o su número de fila y nombre de columna.
                #       - subConjunto = pandas.DataFrame().loc['etiqueta_fila', 'etiqueta_columna']
                #       - subConjunto = pandas.DataFrame().loc[numero_fila,     'etiqueta_columna']
                # - Selección de una sola columna: Se puede utilizar la nomenclatura de dos puntos (:) para 
                #   extraer todos los datos de una columna.
                #       - columna = pandas.DataFrame().loc[:, 'etiqueta_columna']
                # - Selección de múltiples filas y columnas: También se pueden seleccionar múltiples filas y 
                #   columnas especificando de igual forma sus etiquetas o números.
                #       - subConjunto = pandas.DataFrame().loc[['fila_1', 'fila_2'], ['columna_1', 'columna_2']]
                # - Selección condicional de filas: Se puede seleccionar filas o columnas que cumplan con ciertas 
                #   condiciones lógicas.
                #       - subConjunto = pandas.DataFrame().loc[df['columna'] > 5]
                # - Actualizar una fila existente: Se puede usar para actualizar valores en una fila existente.
                #       - pandas.DataFrame().loc['etiqueta_fila'] = ['nuevo_valor1', 'nuevo_valor2']
                # - Eliminar una fila: Si se pasa un valor None a una fila existente con el método loc[], se 
                #   elimina esa fila del DataFrame.
                #       - pandas.DataFrame().loc['etiqueta_fila'] = None
                # - Añadir una nueva fila: Al pasar -1 como índice de fila, se añadirá una nueva fila al final del 
                #   DataFrame.
                #       - pandas.DataFrame().loc[-1] = ['nuevo_valor1', 'nuevo_valor2']
                resultDataFrame.loc[-1] = headers       #Agregar los nombres de columnas al final del DataFrame.
                #pandas.DataFrame().index: El atributo .index devuelve un objeto que indica los índices de las 
                #filas de un DataFrame. Si los índices de las filas del dataframe son numéricos devuelve un 
                #objeto RangeIndex y si son strings que nombran las filas devuelve un objeto Index. Pero el 
                #chiste de este atributo es poder acceder y modificar los índices de un DataFrame, para así 
                #manipular la posición existente de las filas, si se pone +1 se desplazan hacia abajo y si se 
                #usa la operación -1 se desplazan hacia arriba 1 posición, pero al hacer esto, las filas se 
                #reordenan por sí solas, donde la que estaba hasta abajo se coloca hasta arriba o viceversa.
                resultDataFrame.index = resultDataFrame.index + 1   #Desplazar las filas 1 posición hacia abajo.
                #pandas.DataFrame().sort_index(): El método .sort_index() se utiliza para ordenar o actualizar el 
                #índice asignado a cada fila de un DataFrame. 
                resultDataFrame = resultDataFrame.sort_index()      #Actualizar los índices asignados a las filas.
                #pandas.DataFrame().shape: Para extraer el tamaño de un DataFrame se puede utilizar el atributo 
                #shape de la clase DataFrame, el cual devuelve una tupla que indica su número de filas y 
                #columnas: (filas, columnas) = pandas.DataFrame().shape
                (db_numRows, db_numCols) = resultDataFrame.shape
                #Para obtener el tamaño total de la tabla, se considera el tamaño de la lista de listas que 
                #indican los datos estáticos y el número de filas del DataFrame.
                #NÚMERO DE FILAS DE LA TABLA QUE GUARDA TODOS LOS DATOS.
                numberOfDataSets = 4
                numberOfSpaces = numberOfDataSets - 1
                totalRows = len(STATICDATA_ABOVE_1) + len(STATICDATA_ABOVE_2) + db_numRows + len(STATICDATA_BELOW_1) + numberOfSpaces
                staticDataAbove_1_Rows = len(STATICDATA_ABOVE_1)                 #Filas staticDataAbove_1.
                staticDataAbove_2_Rows = len(STATICDATA_ABOVE_2)                 #Filas staticDataAbove_1.
                #max(num1, num2, num_n): Método que retorna el valor máximo al comparar varios números.
                totalCols = max(7, db_numCols)                                              #Columnas tabla.
                staticDataAbove_2_Cols = len(STATICDATA_ABOVE_2[0])              #Columnas staticDataAbove_2.
                staticDataBelow_1_Cols = len(STATICDATA_BELOW_1[0])              #Columnas staticDataBelow_1.
                #QtWidgets.QTableWidget(): Widget que proporciona una funcionalidad de hoja de cálculo o tabla 
                #editable para mostrar filas y columnas de información en una GUI de PyQt5, las cuales pueden 
                #contener texto, números, imágenes u otros widgets.
                table = QtWidgets.QTableWidget()
                #QtWidgets.QTableWidget().setRowCount() y setColumnCount(): Métodos que sirven para indicar el 
                #número de filas y columnas de un objeto QTableWidget() en una GUI, en sus parámetros reciben 
                #dicho tamaño.
                table.setRowCount(totalRows)
                table.setColumnCount(totalCols)

                #AGREGACIÓN DE DATOS ESTÁTICOS SUPERIORES EN LA TABLA:
                #Establecer colores para filas y columnas de la tabla con datos estáticos que se encuentren 
                #arriba de los datos extraídos por la database.
                #enumerate(): Es un método que devuelve tanto el índice como el valor de los elementos de una 
                #lista, tupla, diccionario, etc. en forma de una tupla de dos valores (indice, valor).
                for (i, row_data) in (enumerate(STATICDATA_ABOVE_1)): #Bucle que recorre las filas de la tabla.
                    for (j, value) in (enumerate(row_data)):         #Bucle que recorre las columnas de la tabla.
                        #QtWidgets.QTableWidgetItem(): Es una clase de PyQt5 que representa una celda individual 
                        #dentro de una tabla QTableWidget. Este elemento puede contener datos y proporcionar 
                        #funcionalidades para editar su formato (color, letra, etc.) dentro de una tabla en la 
                        #interfaz de usuario. En su constructor debe recibir el dato que mostrará cada celda en 
                        #forma de string.
                        itemAbove1 = QtWidgets.QTableWidgetItem(str(value))   #Celdas individuales de la tabla.
                        #QtWidgets.QTableWidgetItem().setTextAlignment(): Este método se utiliza para indicar el
                        #la alineación de un texto dentro de un objeto QTableWidgetItem(), que representa la 
                        #celda de una tabla QTableWidget(), este siempre recibe como parámetro un el atributo de 
                        #un objeto QtCore.Qt, el cual puede ser alguno de los siguientes:
                        # - QtCore.Qt.AlignLeft: Alinea el texto a la izquierda.
                        # - QtCore.Qt.AlignRight: Alinea el texto a la derecha.
                        # - QtCore.Qt.AlignHCenter: Alinea el texto horizontalmente en el centro.
                        # - QtCore.Qt.AlignJustify: Justifica el texto, extendiéndolo para que llene 
                        #   completamente el espacio disponible.
                        # - QtCore.Qt.AlignTop: Alinea el texto en la parte superior.
                        # - QtCore.Qt.AlignBottom: Alinea el texto en la parte inferior.
                        # - QtCore.Qt.AlignVCenter: Alinea el texto verticalmente en el centro.
                        # - QtCore.Qt.AlignCenter: Alinea el texto tanto horizontal como verticalmente en el 
                        #   centro.
                        # - QtCore.Qt.AlignBaseline: Alinea el texto en la línea base de los caracteres.
                        #Estos atributos se pueden combinar utilizando el operador OR (|) si deseas alinear en 
                        #múltiples direcciones simultáneamente.
                        itemAbove1.setTextAlignment(QtCore.Qt.AlignCenter)    #Texto alineado en medio.
                        if i == 0:                      #Color azul:    Fila 1 = (0, Ninguna Columna)
                            #QtWidgets.QTableWidgetItem().setBackground(): Este método se utiliza para indicar el
                            #color de fondo de un objeto QTableWidgetItem(), que representa una celda de una 
                            #tabla QTableWidget(), este siempre recibe como parámetro un objeto QtGui.QColor(), 
                            #el cual a su vez recibe como parámetro el color de fondo en formato rgb, hexadecimal
                            #o string.
                            itemAbove1.setBackground(QtGui.QColor('#4f81bd'))   #Color de celdas.
                            #QtWidgets.QTableWidgetItem().setFont(): Este método sirve para indicar el estilo de 
                            #letra que se usará en el texto de la celda, para ello recibe como parámetro un 
                            #objeto QtGui.QFont(), el cual a su vez puede indicar su tipo de letra y tamaño. Si 
                            #no se indica un tipo de letra y tamaño, se elegirá la predeterminada del sistema 
                            #operativo, o se puede elegir una de las siguientes:
                            # - "Arial"
                            # - "Times New Roman"
                            # - "Courier New"
                            # - "Verdana"
                            # - "Tahoma"
                            # - "Helvetica"
                            # - "Comic Sans MS"
                            # - "Georgia"
                            # - "Trebuchet MS"
                            # - "Palatino"
                            # - "Century Gothic"
                            # - "Lucida Sans Unicode"
                            # - "Segoe UI" (Muy común en Windows)
                            font = QtGui.QFont()
                            #A los objetos QtGui.QFont() se les pueden aplicar los siguientes métodos, pero es 
                            #muy importante que para que esto funcione, primero se cree el objeto, luego se 
                            #aplique el método y finalmente esa variable se asigne al método .setFont():
                            # - setFamily(family): Establece la familia de fuentes para la fuente.
                            # - setPointSize(size): Establece el tamaño del punto de la fuente.
                            # - setPointSizeF(size): Establece el tamaño de punto flotante de la fuente.
                            # - setBold(bold): Establece si la fuente es negrita.
                            # - setItalic(italic): Establece si la fuente es cursiva.
                            # - setUnderline(underline): Establece si la fuente está subrayada.
                            # - setStrikeOut(strikeOut): Establece si la fuente está tachada.
                            # - setWeight(weight): Establece el peso de la fuente.
                            # - setStyle(style): Establece el estilo de la fuente.
                            # - setPixelSize(pixelSize): Establece el tamaño de píxel de la fuente.
                            # - setStretch(stretch): Establece la expansión de la fuente.
                            # - setLetterSpacing(type, spacing): Establece el espaciado entre letras.
                            # - setCapitalization(capitalization): Establece la capitalización de la fuente.
                            # - setHintingPreference(hintingPreference): Establece la preferencia de ajuste de la 
                            #   fuente.
                            # - setFixedPitch(fixedPitch): Establece si la fuente es de espaciado fijo.
                            # - setRawMode(rawMode): Establece el modo bruto de la fuente.
                            # - setStyleHint(styleHint, strategy=None): Establece una pista de estilo para la 
                            #   fuente.
                            # - setStyleStrategy(styleStrategy): Establece la estrategia de estilo de la fuente.
                            # - setKerning(kerning): Establece si la fuente realiza el kerning.
                            # - setOverline(overline): Establece si la fuente tiene una línea superior.
                            font.setBold(True)
                            itemAbove1.setFont(font)
                            #QtWidgets.QTableWidgetItem().setForeground(): Este método se utiliza para indicar el
                            #color del texto de una celda de una tabla, este siempre recibe como parámetro un 
                            #objeto QtGui.QColor(), el cual a su vez recibe como parámetro el color de texto en 
                            #formato rgb, hexadecimal o string.
                            itemAbove1.setForeground(QtGui.QColor('white'))     #Color de letra blanco.
                        elif (i != 0 and j == 1):       #Azul obscuro:  Columna 2 = (Todas las filas menos la primera, 1)
                            itemAbove1.setBackground(QtGui.QColor('#0070c0'))
                        else:                           #Gris azulado:  Todas las demás celdas.
                            itemAbove1.setBackground(QtGui.QColor('#d3dfee'))   #Color de celdas.
                            font = QtGui.QFont()                                #Tipo de letra en negritas.
                            font.setBold(True)
                            itemAbove1.setFont(font)
                        #QtWidgets.QTableWidget().setItem(): El método setItem() se aplica a un objeto 
                        #QTableWidget() y se utiliza para establecer un objeto QTableWidgetItem() en una posición 
                        #específica dentro de una tabla.
                        table.setItem(i, (j + 1), itemAbove1)
                #STATIC DATA ABOVE 2:
                for (i, row_data) in (enumerate(STATICDATA_ABOVE_2)):#Bucle que recorre las filas de la tabla.
                    for (j, value) in (enumerate(row_data)):         #Bucle que recorre las columnas de la tabla.
                        itemAbove2 = QtWidgets.QTableWidgetItem(str(value))     #Celdas individuales de la tabla.
                        #Texto alineado a la izquierda horizontalmente y en medio de la celda verticalmente.
                        itemAbove2.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                        font = QtGui.QFont()                                    #Tipo de letra en negritas.
                        font.setBold(True)                                      #Tipo de letra en negritas.
                        #QtWidgets.QTableWidget().setSpan(): El método .setSpan() permite fusionar un 
                            #conjunto de celdas que se encuentren una alado de la otra (adyacentes) en una sola 
                            #celda más grande dentro de una tabla, osea un objeto QtWidgets.QTableWidget(), para 
                            #ello se deben indicar lo siguiente: setSpan(inicio_y, inicio_x, alto, ancho).
                            # - inicio_y: Índice de fila ("y" o vertical) de la tabla desde donde se quiere 
                            #   empezar a fusionar las celdas.
                            # - inicio_x: Índice de columna ("x" u horizontal) de la tabla desde donde se quiere 
                            #   empezar a fusionar las celdas.
                            # - alto: Número de filas que se fusionarán a partir de la celda especificada por 
                            #   inicio_y e inicio_x.
                            # - ancho: Número de columnas que se fusionarán a partir de la celda especificada por 
                            #   inicio_y e inicio_x.
                            #A continuación, se fusionarán todas las celdas de la 1era fila de la tabla.
                        table.setSpan((i + staticDataAbove_1_Rows + 1), 0, 1, staticDataAbove_2_Cols)
                        if i == 0:                      #Color azul:    Fila 1 = (0, Ninguna Columna)
                            itemAbove2.setBackground(QtGui.QColor('#4f81bd'))   #Color de celdas.
                            itemAbove2.setFont(font)                            #Tipo de letra en negritas.
                        elif (i == 1 or i == 4 or i == 7):#Letra subrayada y en negritas: Filas 2, 5 y 8.
                            itemAbove2.setBackground(QtGui.QColor('white'))     #Color de celdas.
                            font.setUnderline(True)                             #Letra subrayada.
                            itemAbove2.setFont(font)                            #Letra subrayada y en negritas.
                        else:                           #Color blanco:  Todas las demás celdas.
                            itemAbove2.setBackground(QtGui.QColor('white'))     #Color de celdas.
                        #Colocar agrupación de datos.
                        table.setItem((i + staticDataAbove_1_Rows + 1), j, itemAbove2)

                #AGREGACIÓN DE DATOS EXTRAÍDOS DE UNA DATABASE DENTRO DE UNA TABLA:
                #Establecer colores para filas y columnas de la tabla con datos extraídos del database. 
                #Para ello se debe hacer uso del objeto QTableWidgetItem que accede a cada celda de la tabla de 
                #forma individual y además se debe obtener todos los valores del DataFrame que contiene los datos 
                #del database para que estos se puedan colocar en la tabla y además darles color.
                for i in range(db_numRows):       #Bucle for que recorre las filas = i.
                    for j in range(db_numCols):   #Bucle for que recorre las columnas = j.
                        #pandas.DataFrame.iloc[filas, columnas]: El método iloc sirve para acceder a uno o varios 
                        #de los valores de un DataFrame a través de sus filas y/o columnas contando desde 0. 
                        #Por ejemplo:
                        # - DataFrame.iloc[0]: Selecciona la primera fila del DataFrame.
                        # - DataFrame.iloc[:, 0]: Selecciona la primera columna del DataFrame.
                        # - DataFrame.iloc[0:5, :]: Selecciona las primeras cinco filas del DataFrame.
                        # - DataFrame.iloc[:, 0:2]: Selecciona las dos primeras columnas del DataFrame.
                        celda_Db = QtWidgets.QTableWidgetItem(str(resultDataFrame.iloc[i, j]))
                        celda_Db.setTextAlignment(QtCore.Qt.AlignCenter)    #Texto alineado en medio.
                        font = QtGui.QFont()                                #Tipo de letra en negritas.
                        font.setBold(True)                                  #Tipo de letra en negritas.
                        if (i == 0):                    #Color azul:    Fila 1 = (0, Ninguna Columna)
                            #QtWidgets.QTableWidgetItem().setBackground(): Este método se utiliza para indicar el
                            #color de fondo de un objeto QTableWidgetItem(), que representa una celda de una 
                            #tabla QTableWidget(), este siempre recibe como parámetro un objeto QtGui.QColor(), 
                            #el cual a su vez recibe como parámetro el color de fondo en formato rgb, hexadecimal
                            #o string.
                            celda_Db.setBackground(QtGui.QColor('blue'))        #Color de celdas.
                            celda_Db.setFont(font)                              #Letra en negritas.
                        elif (i != 0 and j == 0):       #Color verde:   Columna 1 = (Todas las filas menos la primera, 0)
                            celda_Db.setBackground(QtGui.QColor('green'))
                            celda_Db.setFont(font)                              #Letra en negritas.
                        elif (i != 0 and j == 1):       #Color gris:    Columna 2 = (Todas las filas menos la primera, 1)
                            celda_Db.setBackground(QtGui.QColor('gray'))
                            #De igual manera, se puede analizar el contenido de las celdas y/o columnas para asignar un 
                            #color condicional a sus celdas, para ello se hará uso de un if anidado, recordando que la 
                            #variable "j" accede a las columnas de la tabla, la "i" a sus filas y el método iloc accede 
                            #a un valor en específico dadas la coordenada de su [fila, columna]:
                            if ((resultDataFrame.columns[j] == "Content Status") and (resultDataFrame.iloc[i, j] == "standard")):
                                celda_Db.setBackground(QtGui.QColor('#00f1ba')) #Color condicional.
                        else:                           #Color amarillo: Todas las demás celdas.
                            celda_Db.setBackground(QtGui.QColor('yellow'))
                        #QtWidgets.QTableWidget().setItem(): El método setItem() se aplica a un objeto 
                        #QTableWidget() y se utiliza para establecer un objeto QTableWidgetItem() en una posición 
                        #específica dentro de una tabla. Pero en este caso es importante ajustar el índice de 
                        #fila (i) para acomodar esta nueva tabla debajo de los datos estáticos superiores, además 
                        #de dejar un espacio entre ellos, por eso es que se debe sumar un 1 al número de filas 
                        #más el número de filas de la tabla o tablas superiores, pero para dejar un espacio entre 
                        #ellas los datos inferiores deberán aumentar en 1 el espacio.
                        table.setItem((i + staticDataAbove_1_Rows + staticDataAbove_2_Rows + 1 + 1), j, celda_Db)
                
                #AGREGACIÓN DE DATOS ESTÁTICOS INFERIORES EN LA TABLA:
                #Establecer colores para filas y columnas de la tabla con datos estáticos que se encuentren 
                #arriba de los datos extraídos por la database.
                for i, row_data in enumerate(STATICDATA_BELOW_1):    #Bucle que recorre las filas de la tabla.
                    for j, value in enumerate(row_data):            #Bucle que recorre las columnas de la tabla.
                        itemBelow1 = QtWidgets.QTableWidgetItem(str(value))   #Objeto que representa cada celda.
                        itemBelow1.setTextAlignment(QtCore.Qt.AlignCenter)    #Alineación del texto en medio.
                        font = QtGui.QFont()                                #Tipo de letra en negritas.
                        font.setBold(True)                                  #Tipo de letra en negritas.
                        if i == 0:
                            itemBelow1.setBackground(QtGui.QColor('white')) #Color de celdas.
                            font.setUnderline(True)                         #Letra subrayada.
                            itemBelow1.setFont(font)                        #Letra subrayada y en negritas.
                            #Texto alineado a la izquierda horizontalmente y en medio de la celda verticalmente.
                            itemBelow1.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
                            #QtWidgets.QTableWidget().setSpan(): El método .setSpan() permite fusionar un 
                            #conjunto de celdas que se encuentren una alado de la otra (adyacentes) en una sola 
                            #celda más grande dentro de una tabla, osea un objeto QtWidgets.QTableWidget(), para 
                            #ello se deben indicar lo siguiente: setSpan(inicio_y, inicio_x, alto, ancho).
                            #Cabe mencionar que como entre las agrupaciones de datos dentro de la tabla se está 
                            #considerando un espacio de separación, se debe sumar + 1 cada que se agrega una 
                            #nueva agrupación de datos, además de que se debe considerar específicamente la 
                            #posición de la fila donde se quiere fusionar las celdas.
                            table.setSpan((i + staticDataAbove_1_Rows + staticDataAbove_2_Rows + db_numRows + 1 + 1 + 1), 0, 1, staticDataBelow_1_Cols)
                        elif i == 1:                    #Color azul:    Fila 1 = (0, Ninguna Columna)
                            itemBelow1.setBackground(QtGui.QColor('#4472c4'))   #Color de celdas.
                            itemBelow1.setFont(font)                            #Letra en negritas.
                        elif (i == 2 or i == 10):                       #Gris azulado:  Fila 2 = (1, Ninguna Columna)
                            itemBelow1.setBackground(QtGui.QColor('#A7BFDE'))   #Color de celdas.
                            itemBelow1.setFont(font)                            #Letra en negritas.
                            #QtWidgets.QTableWidget().setSpan(): El método .setSpan() permite fusionar un 
                            #conjunto de celdas que se encuentren una alado de la otra (adyacentes) en una sola 
                            #celda más grande dentro de una tabla, osea un objeto QtWidgets.QTableWidget(), para 
                            #ello se deben indicar lo siguiente: setSpan(inicio_y, inicio_x, alto, ancho).
                            #Se debe considerar específicamente la posición de la fila donde se quiere fusionar 
                            #las celdas.
                            table.setSpan((i + staticDataAbove_1_Rows + staticDataAbove_2_Rows + db_numRows + 1 + 1 + 1), 0, 1, staticDataBelow_1_Cols)
                        elif (i != (0 & 1 & 2) and j == 0): #Color verde:   Columna 1 = (Todas las filas menos las primeras 2, 0)
                            itemBelow1.setBackground(QtGui.QColor('#5EC268'))   #Color de celdas.
                            itemBelow1.setFont(font)                            #Letra en negritas.
                        elif (i != (0 & 1 & 2) and j == 1): #Color gris:    Columna 2 = (Todas las filas menos las primeras 2, 0)
                            itemBelow1.setBackground(QtGui.QColor('gray'))
                        else:                           #Color amarillo: Todas las demás celdas.
                            itemBelow1.setBackground(QtGui.QColor('#FFF2CC'))
                        #QtWidgets.QTableWidget().setItem(): Método para establecer cada celda en una posición 
                        #específica dentro de una tabla. Es importante tomar en cuenta los espacios entre las
                        #agrupaciones de datos que se incluyen en la tabla, además de las filas de todas las 
                        #agrupaciones de datos anteriores.
                        table.setItem((i + staticDataAbove_1_Rows + staticDataAbove_2_Rows + db_numRows + 1 + 1 + 1), j, itemBelow1)
                
                #REDIMENSIONAR EL ANCHO DE LAS CELDAS DE LAS COLUMNAS PARA MOSTRAR SU CONTENIDO COMPLETO:
                #QtWidgets.QTableWidget().columnCount(): El método columnCount() devuelve un número entero que 
                #representa el número de columnas de un objeto QtWidgets.QTableWidget().
                for column in range(table.columnCount()):
                    #QtWidgets.QTableWidget().resizeColumnToContents(): Este método se utiliza para ajustar 
                    #automáticamente el ancho de la columna de una tabla QtWidgets.QTableWidget().  
                    table.resizeColumnToContents(column)
                    #QtWidgets.QTableWidget().columnWidth(): Este método sirve para obtener el ancho actual 
                    #de algunas de las columnas pertenecientes a una tabla QTableWidget, para ello recibe en su 
                    #único parámetro la posición de la columna enumarada desde 0.  
                    anchoColumnas = table.columnWidth(column)
                    #min(num1, num2, num_n): Método que retorna el valor mínimo al comparar varios números. De 
                    #esta forma es como se limita el ancho máximo que puede adoptar una columna en pixeles.
                    limiteAncho = 200           #Anchura máxima de las celdas.
                    anchoMaxColumnas = min(anchoColumnas, limiteAncho)
                    #QtWidgets.QTableWidget().setColumnWidth(): Cuando el método resizeColumnToContents() por 
                    #alguna razón no haya redimensionado automáticamente de forma correcta el ancho de una 
                    #columna, esto se puede forzar a través del método setColumnWidth(), en el cual se indica
                    #el índice de la columna contando desde 0 en su primer parámetro y el ancho en pixeles en su 
                    #segundo parámetro: 
                    table.setColumnWidth(column, anchoMaxColumnas)
                    #ANALIZAR LA ALTURA DE LAS FILAS: Se repetirá el mismo proceso pero ahora con la altura de 
                    #las filas para mostrar todo el contenido de la celda.
                    #QtWidgets.QTableWidget().rowCount(): Método que devuelve el número de filas de una tabla.
                    for row in range(table.rowCount()):
                        #QtWidgets.QTableWidget().sizeHintForRow(): Este método se utiliza para obtener la altura 
                        #recomendada de una fila en un QTableWidget en función del contenido de sus celdas.
                        alturaCelda = table.sizeHintForRow(row)
                        limiteAltura = 100      #Altura máxima de las celdas.
                        alturaMaxCelda = min(alturaCelda, limiteAltura)
                        #QtWidgets.QTableWidget().setRowHeight(): Método utilizado para indicar la altura de 
                        #la fila de una tabla, para ello se debe indicar su índice contando desde 0 y su altura
                        #en pixeles.
                        table.setRowHeight(row, alturaMaxCelda)

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