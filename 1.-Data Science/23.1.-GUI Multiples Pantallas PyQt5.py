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
#matplotlib - Figure: La clase Figure es la base para crear y organizar los elementos gráficos en Matplotlib, 
#que es una librería de graficación matemática.
#PyQt5 - QtGui: Clase que incluye clases y métodos para trabajar con gráficos, fuentes, colores, imágenes, 
#íconos y otros elementos visuales utilizados en una interfaz gráfica (GUI) de PyQt5.
from PyQt5 import QtGui
import sys #sys: Librería que permite interactuar directamente con el sistema operativo y consola del ordenador.

#MainWindow: La clase hereda de la clase QMainWindow, que a su vez hereda de la clase QtWidgets y ambas 
#pertenecen a la librería PyQt5. El elemento representa la ventana del GUI y crea una instancia de la clase 
#GraficaPyQt5 para agregar dentro de la ventana una gráfica.
class MainWindow(QtWidgets.QMainWindow):
    #def __init__(self): Es el constructor o inicializador de la clase, este se llama automáticamente cuando se 
    #crea un objeto que instancee la clase y en él se declaran los atributos que se reutilizarán en los demás 
    #métodos. En Python, el primer parámetro de cualquier método constructor debe ser self, los demás pueden 
    #servir para cualquier cosa, pero si se declaran en el constructor, estos a fuerza deben tener un valor.
    #self: Se refiere al objeto futuro que se cree a partir de esta clase, es similar al concepto de this en 
    #otros lenguajes de programación.
    def __init__(self):
        #super(): Método para importar métodos específicos de una clase base (superclase) desde una subclase, 
        #osea desde una clase que quiere heredar métodos de otra. En este caso se utiliza para importar el 
        #constructor de la clase que estamos heredando.
        super().__init__()
        #PyQt5.QtWidgets.QMainWindow.setWindowTitle(): Método para colocar un título al Window creado con PyQt5.
        self.setWindowTitle("Time Zone Selector")
        #PyQt5.QtWidgets.QMainWindow.setGeometry(): Método para indicar la posición y dimensiones de una ventana,
        #para ello el primer parámetro representa la posición de la esquina superior izquierda medida desde la 
        #esquina superior izquierda de la pantalla (pos_x), la segunda representa la distancia de separación 
        #vertical medida desde el mismo punto (pos_y) y las últimas dos representan el ancho y alto de la ventana 
        #en pixeles:
        #   - setGeometry(pos_x, pos_y, width, height).
        self.setGeometry(100, 100, 900, 500)
        self.open_windows = []  # List to hold references to opened windows
        
        #CREACIÓN DE LOS WIDGETS: Imágen, clase QLabel
        #Las clases PyQt5.QtGui.QPixmap y PyQt5.QtWidgets.QLabel están relacionadas y se utilizan en conjunto 
        #para trabajar con imágenes en la interfaz gráfica.
        #   PyQt5.QtGui.QPixmap: Representa una imagen en memoria creada con datos en bruto, osea un formato 
        #   matricial 3D conformado 3 capas o dimensiones RGB que contienen valores de 0 a 255. Esta clase 
        #   proporciona métodos para cargar, manipular y transformar imágenes.
        #  
        #   PyQt5.QtWidgets.QLabel: Es una representación de imagen que puede ser utilizada directamente en los 
        #   controles y widgets de la interfaz gráfica de PyQt5.
        iconPath = "C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/1.-Data Science/0.-Archivos_Ejercicios_Python/Img/logoDi_cer0MarkIII.png"
        #Cargar una Imagen: Se crea una instancia de la librería PyQt5 por medio del constructor de la clase 
        #QPixmap para cargar una imagen en memoria con datos en bruto.
        # - filepath: En este atributo se indica el nombre de archivo junto con la ruta completa de donde se 
        #   encuentra la imagen que se va a cargar, la cual debe estar indicada en forma de string, con este 
        #   atributo no se sigue la nomenclatura de poner el nombre del atributo seguido de su valor 
        #   (filepath = valor), solamente se pone el path entre comillas.
        # - format: El formato de imagen deseado. Puede ser una cadena como "PNG", "JPEG", "BMP", etc. Si no se 
        #   especifica, se intentará detectar automáticamente el formato.
        pixmap = QtGui.QPixmap(iconPath)
        #PyQt5.QtGui.QPixmap.scaled(): Método utilizado para redimensionar una imagen conformada por datos 
        #brutos, representada por un objeto QPixmap, se realiza a través de la siguiente sintaxis:
        #scaledImage = originalImage.scaled(width, height, aspectRatioMode)
        # - originalImage: Es el objeto QPixmap original que se desea redimensionar.
        # - width: Es el nuevo ancho de la imagen redimensionada.
        # - height: Es la nueva altura de la imagen redimensionada.
        # - aspectRatioMode: Es una constante de la clase QtCore.Qt.AspectRatioMode que especifica cómo se debe 
        #   ajustar la imagen para mantener la proporción.
        #           - QtCore.Qt.AspectRatioMode.IgnoreAspectRatio: La imagen se ajusta exactamente al tamaño 
        #             especificado, sin mantener la proporción original. Esto puede dar lugar a una distorsión 
        #             de la imagen.
        #           - QtCore.Qt.AspectRatioMode.KeepAspectRatio: La imagen se redimensiona manteniendo la 
        #             proporción original y ajustándose dentro del tamaño especificado para que quepa 
        #             completamente sin recortarla. Esto puede generar márgenes en blanco si la relación de 
        #             aspecto difiere del tamaño especificado.
        #           - QtCore.Qt.AspectRatioMode.KeepAspectRatioByExpanding: La imagen se redimensiona 
        #             manteniendo la proporción original y ocupando todo el tamaño especificado. Esto puede 
        #             provocar que parte de la imagen quede fuera de los límites del tamaño especificado.
        # - SmoothTransformation: Es una constante de la clase QtCore.Qt que se utiliza para suavizar la imagen 
        #   al realizar la transformación, es de mucha utilidad para mejorar la calidad de la imagen escalada.
        #En todos los parámetos mencionados para este método, no se indica explícitamente su nombre, solo se 
        #asigna un valor y el método identifica cuál es por su orden.
        #Todas las operaciones donde se afecta a una imagen se deben realizar a la imagen representada en 
        #datos brutos, para luego asignarse al widget de la GUI.
        scaledImage = pixmap.scaled(200, 200, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        #Mostrar la imagen en un widget: Para mostrar la imagen de tipo Bitmap en un widget gráfico de se usa 
        #una instancia de la clase PyQt5.QtWidgets.QLabel, que es parte de la biblioteca PyQt5 y se utiliza para 
        #crear un widget que muestre un texto estático o una imagen en una interfaz gráfica, se le deben indicar 
        #los siguientes parámetros cuando se usa para crear una imagen estática:
        # - parent: Este parámetro es opcional y especifica el widget padre del QLabel. Indica a qué widget 
        #   pertenece el QLabel.
        # - pixmap (QPixmap): La imagen que se mostrará en la etiqueta.
        #Para dar estilo al QLabel cuando se utiliza para mostrar texto estático es mejor utilizar etiquetas 
        #HTML que contengan un style que les dé estilo por medio de instrucciones CSS, además es importante 
        #mencionar que para el style se deben usar comillas simples ('') para que no tenga conlficto con las 
        #comillas dobles del parámetro text = "". PyQt5 acepta algunas instrucciones CSS pero no todas.
        logo_label = QtWidgets.QLabel(pixmap = scaledImage)    #Imagen redimensionada.

        #CREACIÓN DE LOS WIDGETS: Texto Estático, clase QLabel
        #Instancia de la librería PyQt5 por medio del constructor de la clase QLabel que hereda de la clase 
        #QtWidgets y sirve para crear un widget que muestre un texto estático o una imagen en una interfaz 
        #gráfica, se le deben indicar los siguientes parámetros cuando se usa para crear texto estático:
        # - parent: Especifica el widget padre del QLabel. Si se proporciona, el texto estático se colocará 
        #   dentro del widget padre.
        # - text: Permite especificar el texto que se mostrará en el widget. Puede ser una cadena de texto en 
        #   formato plano o enriquecido con etiquetas HTML.
        #Para dar estilo al QLabel cuando se utiliza para mostrar texto estático es mejor utilizar etiquetas 
        #HTML que contengan un style que les dé estilo por medio de instrucciones CSS, además es importante 
        #mencionar que para el style se deben usar comillas simples ('') para que no tenga conlficto con las 
        #comillas dobles del parámetro text = "". PyQt5 acepta algunas instrucciones CSS pero no todas.
        text_label = QtWidgets.QLabel(text ="<p style = 'font-size: 30px; font-family: Consolas, monospace; color: white; font-weight: bold;'>" +
                                                "GUI MultiPantalla"
                                            "</p>")
        
        #CREACIÓN DE LOS WIDGETS: Combo Box, Lista Desplegable
        #Instancia de la librería PyQt5 por medio del constructor de la clase QComboBox que hereda de la clase 
        #QtWidgets y sirve para crear un widget que muestre una lista desplegable de elementos seleccionables 
        #en una ventana o layout.
        self.timezones_combo = QtWidgets.QComboBox()
        #widget.setStyleSheet(): Método que permite aplicar código CSS (la mayoría de métodos, no todos) a los 
        #widgets de una interfaz gráfica de usuario (GUI).
        # - La siguiente línea de código es un método alternativo a usar la herramienta linear-gradient, ya que 
        #   esta no es admitida por PyQt5:
        #   background: qlineargradient(x1:punto_inicial, y1:punto_inicial, x2:punto_final, y2:punto_final, stop:0 rgb(R_inicial,G_inicial,B_inicial), stop:1 rgb(R_final,G_final,B_final));
        self.timezones_combo.setStyleSheet("font-size: 15px; font-family: Consolas, monospace; color: #002550; font-weight: bold; background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 rgb(255, 255, 255), stop:1 rgb(179, 185, 188))")
        #QtWidgets.QComboBox.addItems(): Método que se utiliza para agregar una lista de elementos al combo box. 
        #Este puede recibir como parámetro directamente una lista, tupla o diccionario que representen los 
        #elementos que se agregarán al combo box o puede recibir una función propia que cree dicha lista, para 
        #luego añadir dichos elementos creados por la función al QComboBox.
        self.timezones_combo.addItems(["GMT", "UTC", "CET", "PST", "EST"])
        
        
        #CONTENEDORES DE ELEMENTOS: La biblioteca PyQt5 ofrece varios tipos de contenedores que se pueden 
        #utilizar para organizar los widgets en una interfaz gráfica. Los más comunes son:
        # - QVBoxLayout: Organiza los widgets en una disposición vertical, uno debajo del otro.
        # - QHBoxLayout: Organiza los widgets en una disposición horizontal, uno al lado del otro.
        # - QGridLayout: Organiza los widgets en una cuadrícula bidimensional de filas y columnas.
        # - QFormLayout: Diseñado específicamente para crear formularios, donde los widgets se colocan en pares 
        #   de etiqueta y campo de entrada.
        # - QStackedLayout: Permite apilar varios widgets uno encima del otro y mostrar uno a la vez.
        # - QTabWidget: Permite crear pestañas donde se pueden colocar diferentes conjuntos de widgets en cada 
        #   pestaña.
        # - QScrollArea: Proporciona una vista desplazable para un contenido que puede ser mayor que el área 
        #   visible.
        # - QGroupBox: Crea un grupo que puede contener y organizar otros widgets.
        # - QSplitter: Permite dividir el área de visualización en secciones redimensionables que contienen 
        #   widgets diferentes.
        # - QWidget: Proporciona una ventana o área rectangular en la que se pueden colocar otros widgets para 
        #   crear una interfaz gráfica, un QWidget puede contener otros widgets o contenedores dentro.
        #Cuando se desee ordenar un contenedor de una forma específica dentro de un diseño o establecer ciertas 
        #características como altura, ancho, etc. Es necesario crear un widget que lo contenga, para ello se le 
        #debe pasar dicho widget como parámetro al contenedor, logrando así que el widget se convierta en el 
        #elemento padre del layout.
        # - parent: Si el constructor de esta clase recibe como parámetro un objeto QWidget, ese será el 
        #   contenedor principal del objeto QVBoxLayout que organiza sus elementos verticalmente.
        # - Si no recibe ningún parámetro, este es un contenedor vacío sin widget principal que aceptará 
        #   varios elementos o contenedores y los irá colocando verticalmente, horizontalmente, en forma de 
        #   matriz, o de varias otras formas, uno después del otro.
        main_layout = QtWidgets.QVBoxLayout()               #Contenedor principal.
        #EL MENÚ SUPERIOR DEBE TENER UNA ALTURA EN ESPECÍFICO, POR LO TANTO SE CREA UN WIDGET QUE LO CONTENGA: 
        #Aunque cabe mencionar que las características del widget se pueden específicar antes o después de 
        #introducir los elementos deseados en el contenedor.
        menu_widget = QtWidgets.QWidget()                   #Widget que contiene al Layout del menú superior.
        menu_widget.setFixedHeight(100)                     #setFixedHeight(): Altura fija para un Widget.
        #En este caso el height de CSS lo que hace es modificar el tamaño de los widgets, no del contenedor.
        menu_widget.setStyleSheet("background-color: #002550; height: 20px;")
        menu_layout = QtWidgets.QHBoxLayout(menu_widget)    #Contenedor del menú superior.
        self.container_layout = QtWidgets.QHBoxLayout()     #Contenedor intermedio.
        
        #PyQt5.QtWidgets.QVBoxLayout.addWidget(): Método usado para añadir un widget (elemento) de forma 
        #secuencial dentro de un Layout, estos se ordenarán de una forma u otra dependiendo de qué tipo de Layout 
        #sea, y los widgets pueden ser botones, listas desplegables, textos, imagenes, etc. Se indica el órden en 
        #el que se colocarán los elementos dependiendo de cual fue añadido primero y cual después en el código.
        #Además, cabe mencionar que si se quiere añadir un Layout dentro de otro, se usa el método .addLayout() 
        #de la misma forma. 
        #AÑADIENDO WIDGETS AL CONTENEDOR DEL MENÚ SUPERIOR:
        menu_layout.addWidget(logo_label)                   #Logo del contenedor del menú superior.
        menu_layout.addWidget(text_label)                   #Texto del contenedor del menú superior.
        menu_layout.addWidget(self.timezones_combo)         #Combo box del contenedor del menú superior.
        #AÑADIENDO WIDGETS AL CONTENEDOR INTERMEDIO:
        self.container_layout.addWidget(self.create_square("Square 1", "This is square 1", "Create 1", 1))
        self.container_layout.addWidget(self.create_square("Square 2", "This is square 2", "Create 2", 2))
        
        #AÑADIENDO CONTENEDORES AL CONTENEDOR PRINCIPAL, QUE LOS ORDENA HORIZONTALMENTE DE ARRIBA A ABAJO: 
        main_layout.addWidget(menu_widget)                  #Se agrega el Widget menú al contenedor principal.
        #PyQt5.QtWidgets.QVBoxLayout.addStretch(): Este método agrega un espacio elástico al layout que se 
        #expandirá para ocupar cualquier espacio adicional disponible dentro del contenedor.
        main_layout.addStretch()                            #Se agrega un espaciado stretch después.
        main_layout.addLayout(self.container_layout)        #Se agrega el Layout medio al contenedor principal.
        main_layout.addStretch()                            #Se agrega un espaciado stretch después.
        
        #Creación de un objeto QWidget para acomodar el contenedor principal dentro del frame.
        centralWidget = QtWidgets.QWidget()
        #PyQt5.QtWidgets.QVBoxLayout.setLayout(): Método usado para añadir un layout (que es un contenedor más 
        #complejo) a un widget (que es un contenedor más sencillo), esto es útil hacerlo cuando se quiere 
        #colocar el contenedor en una cierta posición (central, arriba, abajo, a la derecha o a la izquierda) 
        #dentro de la ventana de la GUI.
        centralWidget.setLayout(main_layout)
        #ALINEACIÓN DE CONTENIDO EN UN WIDGET O LAYOUT:
        #PyQt5.QtWidgets.QMainWindow.setCentralWidget() = self.setCentralWidget(): Método aplicado al objeto de 
        #la clase QMainWindow, del que hereda esta clase para establecer el widget central de la ventana 
        #principal, ya que en PyQt5 las ventanas generalmente se dividen en diferentes áreas:
        # - Una barra de menú en la parte superior, para ello se debe indicar que objeto es el menu bar.
        #       - widget.setMenuBar(widget, QMenuBar)
        # - Una barra de herramientas opcional en la parte superior o inferior.
        #       - widget.setStatusBar(widget, QStatusBar)
        # - Un área central donde se coloca el contenido principal de la ventana. 
        #       - widget.setCentralWidget(widget)
        #El método setCentralWidget() se utiliza para especificar qué widget se debe colocar en el área central
        #de la ventana creada con esta clase propia.
        self.setCentralWidget(centralWidget)            #Contenedor colocado en el área central de la GUI.
        
    def create_square(self, name, text, button_text, window_number):
        square = QtWidgets.QFrame()
        square.setFrameShape(QtWidgets.QFrame.StyledPanel)
        square.setFixedSize(200, 200)
        square.setStyleSheet("background-color: white;")
        square.mousePressEvent = lambda event, n=name, w=window_number: self.open_window(n, w)
        
        # Add layout to square
        layout = QtWidgets.QVBoxLayout()
        square.setLayout(layout)
        
        # Text label
        text_label = QtWidgets.QLabel(text)
        layout.addWidget(text_label)
        
        # Button
        create_button = QtWidgets.QPushButton(button_text)
        create_button.clicked.connect(lambda: self.open_window(f"{name} Window", window_number))
        layout.addWidget(create_button)
        
        return square
    
    def open_window(self, name, window_number):
        window = QtWidgets.QWidget()
        window.setWindowTitle(name)
        window.setGeometry(200, 200, 400, 300)
        
        # Top container with blue background color
        top_container = QtWidgets.QWidget()
        top_container.setStyleSheet("background-color: #002550;")
        
        # Below container with gray background color
        below_container = QtWidgets.QWidget()
        below_container.setStyleSheet("background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 rgb(255, 255, 255), stop:1 rgb(179, 185, 188));")
        
        # Add text labels and buttons to the below container
        text_label1 = QtWidgets.QLabel("This is line 1.")
        text_label2 = QtWidgets.QLabel("This is line 2.")
        
        confirm_button = QtWidgets.QPushButton("Confirm")
        return_button = QtWidgets.QPushButton("Return")
        
        button_layout = QtWidgets.QHBoxLayout()
        button_layout.addWidget(confirm_button)
        button_layout.addWidget(return_button)
        
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(text_label1)
        layout.addWidget(text_label2)
        layout.addLayout(button_layout)
        below_container.setLayout(layout)
        
        # Add top and below containers to the window
        window_layout = QtWidgets.QVBoxLayout()
        window_layout.addWidget(top_container)
        window_layout.addWidget(below_container)
        
        window.setLayout(window_layout)
        
        confirm_button.clicked.connect(lambda: print(f"Confirm button clicked in Window {window_number}"))
        return_button.clicked.connect(window.close)
        
        window.show()
        
        # Keep a reference to the opened window
        self.open_windows.append(window)
        
    def timezone_changed(self, index):
        timezone = self.timezones_combo.currentText()
        print("Selected Time Zone:", timezone)
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setStyleSheet("background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 rgb(255, 255, 255), stop:1 rgb(179, 185, 188));")
    window.show()
    sys.exit(app.exec_())