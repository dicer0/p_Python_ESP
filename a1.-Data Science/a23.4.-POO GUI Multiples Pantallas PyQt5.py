# -*- coding: utf-8 -*-

#pyinstaller nombreArchivo.py --onefile --windowed --icon=path/icono.ico
#pyinstaller: Es una librería que se utiliza para convertir un programa de Python a un archivo .exe.
#--onefile: Sirve para que cuando se ejecute el comando de pyinstaller, se cree un solo archivo ejecutable.
#--windowed: Sirve para que cuando se ejecute el ejecutable, no se abra la consola.
#--icon=path/icono.ico: Sirve para asignar un ícono al .exe, pero para ello el archivo debe tener extensión .ico.

#En Python se introducen comentarios de una sola linea con el simbolo #.
#La primera línea de código incluida en este programa se conoce como declaración de codificación o codificación 
#de caracteres. Al especificar utf-8 (caracteres Unicode) como la codificación, nos aseguramos de que el archivo 
#pueda contener caracteres especiales, letras acentuadas y otros caracteres no ASCII sin problemas, garantizando 
#que Python interprete correctamente esos caracteres y evite posibles errores de codificación.
#Se puede detener una ejecución con el comando [CTRL] + C puesto en consola, con el comando "cls" se borra su 
#historial y en Visual Studio Code con el botón superior derecho de Play se corre el programa.
#Para comentar en Visual Studio Code varias líneas de código se debe pulsar:
#[CTRL] + K (VSCode queda a la espera). Después pulsa [CTRL] + C para comentar y [CTRL] + U para descomentar.

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
import webbrowser #webbrowser: Librería que permite abrir y utilizar navegadores web en Python.

#IMPORTACIÓN DE CLASES: Cuando se quiera importar una clase, el nombre de esta no puede empezar con un número, 
#sino cuando la quiera importar obtendré un error y se va accediendo a las carpetas o también llamados paquetes 
#en la programación orientada a objetos (POO), por medio de puntos:
# - Directorio normal:      carpeta1/carpeta2/carpeta3
# - Directorio paquetes:    carpeta1.carpeta2.carpeta3
#La parte del directorio se coloca después de la palabra reservada from y la clase a importar después de import.
from Clases_Personalizadas.POO_23_3_DataBaseExcel.POO_DB_ExcelReport import DatabaseExcelHandler
from Clases_Personalizadas.POO_23_3_DataBaseExcel.POO_AdditionalScreens import SecondaryWindow
from Clases_Personalizadas.POO_23_3_DataBaseExcel.POO_ExcelCellAdjust import ExcelCellAdjuster
from Clases_Personalizadas.POO_23_3_DataBaseExcel.POO_CopyExcelTable import ExcelDataCopier
#AutomationConstants(): Clase propia que hereda de enum.Enum para poder declarar enums en el código para ayudar 
#en la legibilidad del código, además de que de esta manera se pueden separar datos sensibles que necesitan más 
#seguridad como claves, contraseñas, etc. en un archivo por separado. La sintaxis para usar un enum es:
# - Clase donde se declaran los enums dentro de un archivo file_enums.py:
#       class nombreClasePersonalizadaQueHeredaDeEnum(enum.Enum):
#           NOMBRE_CONSTANTE = VALOR
# - Clase donde se importan los enums para utilizarlos:
#       from file_enums import nombreClasePersonalizadaQueHeredaDeEnum
#       constanteEnum = nombreClasePersonalizadaQueHeredaDeEnum.NOMBRE_CONSTANTE.value
from Clases_Personalizadas.POO_23_3_DataBaseExcel.Constants_and_Keys.ENUM_Constants import AutomationConstants

#MainWindow: La clase hereda de la clase QMainWindow, que a su vez hereda de la clase QtWidgets y ambas 
#pertenecen a la librería PyQt5. El elemento representa la ventana del GUI y crea una instancia de la clase 
#GraficaPyQt5 para agregar dentro de la ventana una gráfica.
class MainWindow(QtWidgets.QMainWindow):
    #def __init__(self): Es el constructor o inicializador de la clase, este se llama automáticamente cuando se 
    #crea un objeto que instancíe la clase y en él se declaran los atributos que se reutilizarán en los demás 
    #métodos. En Python, el primer parámetro de cualquier método constructor debe ser self, los demás pueden 
    #servir para cualquier cosa, pero si se declaran en el constructor, estos a fuerza deben tener un valor.
    #self: Se refiere al objeto futuro que se cree a partir de esta clase, es similar al concepto de this en 
    #otros lenguajes de programación.
    def __init__(self):
        #super(): Método para importar métodos de una clase base (superclase) desde una subclase, osea desde una 
        #clase que quiere heredar métodos de otra. En este caso se utiliza para importar el constructor de la 
        #clase que estamos heredando.
        super().__init__()
        #PyQt5.QtWidgets.QMainWindow.setWindowTitle(): Método para colocar un título al Window creado con PyQt5.
        self.setWindowTitle("Time Zone Selector")
        #PyQt5.QtWidgets.QMainWindow.setGeometry(): Método para indicar la posición y dimensiones de una ventana,
        #para ello el primer parámetro representa la posición de la esquina superior izquierda medida desde la 
        #esquina superior izquierda de la pantalla (pos_x), la segunda representa la distancia de separación 
        #vertical medida desde el mismo punto (pos_y) y las últimas dos representan el ancho y alto de la ventana 
        #en pixeles:
        #   - setGeometry(pos_x, pos_y, width, height).
        self.setGeometry(100, 100, 1000, 500)
        #La lista self.open_windows sirve para que las ventanas adicionales del GUI no se cierren.
        self.open_windows = []
        
        #WIDGETS MENU:
        #CREACIÓN DE LOS WIDGETS: Imágen, clase QLabel
        #Las clases PyQt5.QtGui.QPixmap y PyQt5.QtWidgets.QLabel están relacionadas y se utilizan en conjunto 
        #para trabajar con imágenes en la interfaz gráfica.
        #   PyQt5.QtGui.QPixmap: Representa una imagen en memoria creada con datos en bruto, osea un formato 
        #   matricial 3D conformado 3 capas o dimensiones RGB que contienen valores de 0 a 255. Esta clase 
        #   proporciona métodos para cargar, manipular y transformar imágenes.
        #  
        #   PyQt5.QtWidgets.QLabel: Es una representación de imagen que puede ser utilizada directamente en los 
        #   controles y widgets de la interfaz gráfica de PyQt5.
        ICON_PATH = "C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/a1.-Data Science/0.-Archivos_Ejercicios_Python/Img/logoDi_cer0MarkIII.png"
        #Cargar una Imagen: Se crea una instancia de la librería PyQt5 por medio del constructor de la clase 
        #QPixmap para cargar una imagen en memoria con datos en bruto.
        # - filepath: En este atributo se indica el nombre de archivo junto con la ruta completa de donde se 
        #   encuentra la imagen que se va a cargar, la cual debe estar indicada en forma de string, con este 
        #   atributo no se sigue la nomenclatura de poner el nombre del atributo seguido de su valor 
        #   (filepath = valor), solamente se pone el path entre comillas.
        # - format: El formato de imagen deseado. Puede ser una cadena como "PNG", "JPEG", "BMP", etc. Si no se 
        #   especifica, se intentará detectar automáticamente el formato.
        pixmap = QtGui.QPixmap(ICON_PATH)
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
        text_menu =  QtWidgets.QLabel(text ="<p style = 'font-size: 30px; font-family: Consolas, monospace; color: white; font-weight: bold;'>" +
                                                "GUI MultiPantalla"
                                            "</p>")
        #CREACIÓN DE LOS WIDGETS: Combo Box, Lista Desplegable
        #Instancia de la librería PyQt5 por medio del constructor de la clase QComboBox que hereda de la clase 
        #QtWidgets y sirve para crear un widget que muestre una lista desplegable de elementos seleccionables 
        #en una ventana o layout.
        self.timezones_combo = QtWidgets.QComboBox()
        #widget.setStyleSheet(): Método que permite aplicar código CSS (la mayoría de métodos, no todos) a los 
        #widgets de una interfaz gráfica de usuario (GUI). Cabe mencionar que al indicar el objeto del widget 
        #(tipo de elemento), se puede añadir condiciones para que el diseño cambie:
        # - "widget:estado { estilo }": A continuación se muestran algunos ejemplos.
        #       - QPushButton:
        #           - QPushButton:disabled { estilo_condicional }
        #           - QPushButton:checked { estilo_condicional }
        #           - QPushButton:checked:hover { estilo_condicional }
        #           - QPushButton:checked:pressed { estilo_condicional }
        #       - QCheckBox:
        #           - QCheckBox:checked { estilo_condicional }
        #           - QCheckBox:unchecked { estilo_condicional }
        #       - QRadioButton:
        #           - QRadioButton:checked { estilo_condicional }
        #       -    QRadioButton:unchecked { estilo_condicional }
        #       - QLineEdit:
        #           - QLineEdit:read-only { estilo_condicional }
        #           - QLineEdit:focus { estilo_condicional }
        #       - QComboBox:
        #           - QComboBox:editable { estilo_condicional }
        #           - QComboBox:disabled { estilo_condicional }
        #       - QProgressBar:
        #           - QProgressBar::chunk { estilo_condicional }
        #           - QProgressBar::chunk:disabled { estilo_condicional }
        # - La siguiente línea de código es un método alternativo a usar la herramienta linear-gradient, ya que 
        #   esta no es admitida por PyQt5:
        #   background: qlineargradient(x1:punto_inicial, y1:punto_inicial, x2:punto_final, y2:punto_final, stop:0 rgb(R_inicial,G_inicial,B_inicial), stop:1 rgb(R_final,G_final,B_final));
        self.timezones_combo.setStyleSheet("font-size: 15px; font-family: Consolas, monospace; color: #002550; font-weight: bold; background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 rgb(255, 255, 255), stop:1 rgb(179, 185, 188))")
        #QtWidgets.QComboBox.addItems(): Método que se utiliza para agregar una lista de elementos al combo box. 
        #Este puede recibir como parámetro directamente una lista, tupla o diccionario que representen los 
        #elementos que se agregarán al combo box o puede recibir una función propia que cree dicha lista, para 
        #luego añadir dichos elementos creados por la función al QComboBox.
        self.timezones_combo.addItems(["GMT", "UTC", "CET", "PST", "EST"])
        
        #WIDGETS CONTENEDOR INTERMEDIO:
        #QtWidgets.QLabel(): Widget que sirve para crear un texto estático o una imagen en una interfaz gráfica, 
        #se le deben indicar los siguientes parámetros cuando se usa para crear un texto estático:
        # - parent: Especifica el widget padre del QLabel. Si se proporciona, el texto estático se colocará 
        #   dentro del widget padre.
        # - text: Permite especificar el texto que se mostrará en el widget. Puede ser una cadena de texto en 
        #   formato plano o enriquecido con etiquetas HTML. 
        title_content =  """<p style = 'font-size: 30px; font-family: Consolas, monospace; color: black; font-weight: bold;'> 
                                Título Layout 
                            </p>"""
        element_title1 =  QtWidgets.QLabel(text = title_content)
        element_title2 =  QtWidgets.QLabel(text = title_content)
        text_content =   """<p style = 'font-size: 20px; font-family: Consolas, monospace; color: black;'> 
                                Texto del contenedor
                            </p>"""
        element_text1 =  QtWidgets.QLabel(text = text_content)
        element_text2 =  QtWidgets.QLabel(text = text_content)
        buttons_content =   """<p style = 'font-size: 25px; font-family: Consolas, monospace; color: darkgray; font-weight: bold;'> 
                                Texto del botón
                            </p>"""
        buttons_text1 =  QtWidgets.QLabel(text = buttons_content)
        buttons_text2 =  QtWidgets.QLabel(text = buttons_content)
        #CREACIÓN DE LOS WIDGETS: Botón
        #Instancia de la librería PyQt5 por medio del constructor de la clase QPushButton que hereda de la clase 
        #QtWidgets y sirve para crear un widget de tipo botón, en este se deben indicar como parámetros:
        # - parent: Especifica el objeto padre al que se asociará el botón. Si se proporciona, el botón se 
        #   colocará dentro del widget padre.
        # - text: Con este parámetro se indica el texto que aparecerá sobre el botón.
        # - icon: Establece el ícono que se mostrará junto al texto del botón, debe utilizarse un objeto QIcon 
        #   perteneciente a la librería QtGui para que se pueda agregar un ícono.
        # - checkable: Especifica si el botón funciona como un switch (que mantiene su estado) o como un push 
        #   button (que no mantiene su estado a menos que se mantenga presionado).
        #       - checkable = True:     Botón tipo switch.
        #       - checkable = False:    Botón tipo push button.
        # - autoDefault: Indica si el botón es el predeterminado del diálogo. Si se establece en True, el botón 
        #   responderá automáticamente a la tecla "Enter", sino no lo hará.
        # - flat: Con False se indica que el botón se muestre sin un marco, con True aparece el marco.
        # - menu: Especifica el menú desplegable asociado al botón.
        # - iconSize: Establece el tamaño del ícono del botón, para ello recibe un objeto QSize:
        #       - QtCore.QSize(ancho, alto): Objeto que indica el tamaño del ícono.
        #CREACIÓN DE ÍCONO PARA INCLUIR EN EL BOTÓN:
        #Variable que guarda el directorio y el nombre del archivo creado, se reemplazan los guiones \ por / 
        #para poder leer una imagen o cualquier otro archivo, se usa la dirección relativa o absoluta de un 
        #directorio:
        # - Dirección relativa: Es una dirección que busca un archivo desde donde se encuentra la carpeta del 
        #   archivo python actualmente, esta se debe colocar entre comillas simples o dobles.
        # - Dirección absoluta: Es una dirección que coloca toda la ruta desde el disco duro C o cualquier otro 
        #   que se esté usando hasta la ubicación del archivo, la cual se debe colocar entre comillas simples o 
        #   dobles.
        #   ..      : Significa que nos debemos salir de la carpeta donde nos encontramos actualmente.
        #   /       : Sirve para introducirnos a alguna carpeta cuyo nombre se coloca después del slash.
        #   .ext    : Se debe colocar siempre el nombre del archivo + su extensión.
        BUTTON_ICON_PATH = "C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/a1.-Data Science/0.-Archivos_Ejercicios_Python/Img/LogoBlancoDi_cer0.png"
        #PyQt5.QtGui.QIcon(): Constructor de la clase QIcon que hereda de la clase QtGui y perteneciente a la 
        #librería PyQt5, usado para crear un objeto que ícono que pueda ser añadido a cualquier widget como lo 
        #puede ser un botón, un texto estático, etc. El tamaño de dicha imagen será reducido automáticamente.
        logoButton = QtGui.QIcon(BUTTON_ICON_PATH)
        #Se declaran como self.nombreObjeto los widgets a los que se les vaya a extraer o introducir datos en el 
        #transcurso del funcionamiento de la interfaz gráfica, en este caso se aplica al botón porque este va a 
        #cambiar el texto que tiene escrito cuando sea presionado.
        docButton1 = QtWidgets.QPushButton(text = "", icon = logoButton, iconSize = QtCore.QSize(30, 30))
        createButton1 = QtWidgets.QPushButton(text = "Create")
        docButton2 = QtWidgets.QPushButton(text = "", icon = logoButton, iconSize = QtCore.QSize(30, 30))
        createButton2 = QtWidgets.QPushButton(text = "Create")
        #widget.setStyleSheet(): Método que permite aplicar código CSS (la mayoría de métodos, no todos) a los 
        #widgets de una interfaz gráfica de usuario (GUI). Cabe mencionar que al indicar el objeto del widget 
        #(tipo de elemento), se puede añadir condiciones para que el diseño cambie:
        # - "widget:estado { estilo }": A continuación se muestran algunos ejemplos.
        #       - QPushButton:
        #           - QPushButton:disabled { estilo_condicional }
        #           - QPushButton:checked { estilo_condicional }
        #           - QPushButton:hover { estilo_condicional }
        #           - QPushButton:pressed { estilo_condicional }
        doctButtonStyle = "background-color: transparent; max-width: 50px; height: 50px; border: 2px solid #e6ebf3; border-radius: 23px;"
        hoverDoctButtonStyle = "background-color: #eaedef; max-width: 50px; height: 50px; border: 2px solid #e6ebf3; border-radius: 23px;"
        docButton1.setStyleSheet(
            f"QPushButton {{ {doctButtonStyle} }}"
            f"QPushButton:hover {{ {hoverDoctButtonStyle} }}"
        )
        docButton2.setStyleSheet(
            f"QPushButton {{ {doctButtonStyle} }}"
            f"QPushButton:pressed {{ {hoverDoctButtonStyle} }}"
        )
        #widget.setStyleSheet(): Método que permite aplicar código CSS (la mayoría de métodos, no todos) a los 
        #widgets de una interfaz gráfica de usuario (GUI).
        createButtonStyle = "min-width: 100px; height: 50px; font-size: 17px; font-weight: bold; font-family: Consolas, monospace; color: white; background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(0,187,255), stop:1 rgb(0,125,173));"
        hoverCreateButtonStyle = "min-width: 100px; height: 50px; font-size: 17px; font-weight: bold; font-family: Consolas, monospace; color: white; background: #00395D;"
        createButton1.setStyleSheet(
            f"QPushButton {{ {createButtonStyle} }}"
            f"QPushButton:hover {{ {hoverCreateButtonStyle} }}"
        )
        createButton2.setStyleSheet(
            f"QPushButton {{ {createButtonStyle} }}"
            f"QPushButton:pressed {{ {hoverCreateButtonStyle} }}"
        )

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
        #------------------------------------------CONTENEDOR PRINCIPAL------------------------------------------
        main_layout = QtWidgets.QVBoxLayout()               #Contenedor principal.
        #------------------------------------------CONTENEDOR PRINCIPAL------------------------------------------
        #EL MENÚ SUPERIOR DEBE TENER UNA ALTURA EN ESPECÍFICO, POR LO TANTO SE CREA UN WIDGET QUE LO CONTENGA: 
        #Aunque cabe mencionar que las características del widget se pueden específicar antes o después de 
        #introducir los elementos deseados en el contenedor.
        #---------------------------------------------CONTENEDOR MENÚ--------------------------------------------
        menu_widget = QtWidgets.QWidget()                   #Widget que contiene al Layout del menú superior.
        menu_widget.setFixedHeight(100)                     #setFixedHeight(): Altura fija para un Widget.
        #En este caso el height de CSS lo que hace es modificar el tamaño de los widgets, no del contenedor.
        menu_widget.setStyleSheet("background-color: #002550; height: 20px;")
        menu_layout = QtWidgets.QHBoxLayout(menu_widget)    #Contenedor del menú superior.
        #---------------------------------------------CONTENEDOR MENÚ--------------------------------------------
        #--------------------------------------------CONTENEDOR MEDIO--------------------------------------------
        middle_widget1 = QtWidgets.QWidget()                #Widget que contiene al Layout intermedio 1.
        middle_widget2 = QtWidgets.QWidget()                #Widget que contiene al Layout intermedio 2.
        content_widget = QtWidgets.QWidget()                #Widget que contiene al Layout horizontal medio.
        #En este caso el height de CSS lo que hace es modificar el tamaño de los widgets, no del contenedor.
        middleWidgetStyle = "background-color: white; height: 100px; padding: 5px; border-radius: 25px;"
        middle_widget1.setStyleSheet(middleWidgetStyle)
        middle_widget2.setStyleSheet(middleWidgetStyle)
        content_widget.setStyleSheet("background-color: transparent;")
        #Objeto de la clase QGridLayout, el cual se utiliza para organizar los widgets en una en una cuadrícula 
        #bidimensional de filas y columnas.
        # - parent: Si el constructor de esta clase recibe como parámetro un objeto QWidget, ese será el 
        #   contenedor principal del objeto QGridLayout que organiza sus elementos en forma de rejilla.
        # - Si no recibe ningún parámetro, este es un contenedor vacío sin widget principal que aceptará 
        #   varios elementos o contenedores y los irá colocando dependiendo de las coordenadas que se les 
        #   indique al utilizar el método .addWidget().
        self.individual_layout1 = QtWidgets.QGridLayout(middle_widget1) #Contenedor individual intermedio 1.
        self.individual_layout2 = QtWidgets.QGridLayout(middle_widget2) #Contenedor individual intermedio 2.
        content_layout = QtWidgets.QHBoxLayout(content_widget)          #Contenedor de elementos intermedios.
        #--------------------------------------------CONTENEDOR MEDIO--------------------------------------------
        
        #PyQt5.QtWidgets.QVBoxLayout.addWidget(): Método usado para añadir un widget (elemento) de forma 
        #secuencial dentro de un Layout, estos se ordenarán de una forma u otra dependiendo de qué tipo de Layout 
        #sea, y los widgets pueden ser botones, listas desplegables, textos, imagenes, etc. Se indica el órden en 
        #el que se colocarán los elementos dependiendo de cual fue añadido primero y cual después en el código.
        #Además, cabe mencionar que si se quiere añadir un Layout dentro de otro, se usa el método .addLayout() 
        #de la misma forma. 
        #AÑADIENDO WIDGETS AL CONTENEDOR DEL MENÚ SUPERIOR:
        menu_layout.addWidget(logo_label)                   #Logo del contenedor del menú superior.
        menu_layout.addWidget(text_menu)                    #Texto del contenedor del menú superior.
        menu_layout.addWidget(self.timezones_combo)         #Combo box del contenedor del menú superior.
        #AÑADIENDO WIDGETS A LOS CONTENEDORES INTERMEDIOS 1 Y 2:
        #PyQt5.QtWidgets.QGridLayout.addWidget(): Método usado para añadir un widget en una cuadrícula 
        #bidimensional compuesta por filas y columnas, donde la primera coordenada de filas y columnas se indica 
        #desde el número 0:
        # - En su primer parámetro se indica el widget que se quiera aregar.
        # - En su segundo parámetro se indica la fila donde se quiere colocar el elemento, contando desde 0.
        # - En su tercer parámetro se indica la columna donde se quiere colocar el elemento, contando desde 0.
        #Fila 1 = x = 0; Columna 1 = y = 0; posicion = (Fila, Columna) 
        #CONTENEDOR INTERMEDIO 1:
        self.individual_layout1.addWidget(element_title1, 0, 0) #Agrega el título del layout en (0,0)
        self.individual_layout1.addWidget(element_text1, 1, 0)  #Agrega el texto del layout en (1,0)
        self.individual_layout1.addWidget(buttons_text1, 2, 0)  #Agrega el texto de los botones en (2,0)
        self.individual_layout1.addWidget(docButton1, 2, 1)     #Agrega el botón de documentación en (2,1)
        self.individual_layout1.addWidget(createButton1, 2, 2)  #Agrega el botón de documentación en (2,1)
        #CONTENEDOR INTERMEDIO 2:
        self.individual_layout2.addWidget(element_title2, 0, 0) #Agrega el título del layout en (0,0)
        self.individual_layout2.addWidget(element_text2, 1, 0)  #Agrega el texto del layout en (1,0)
        self.individual_layout2.addWidget(buttons_text2, 2, 0)  #Agrega el texto de los botones en (2,0)
        self.individual_layout2.addWidget(docButton2, 2, 1)     #Agrega el botón de documentación en (2,1)
        self.individual_layout2.addWidget(createButton2, 2, 2)  #Agrega el botón de documentación en (2,1)
        #CONTENEDOR DE LOS 2 INTERMEDIOS:
        content_layout.addWidget(middle_widget1)                #Logo del contenedor del menú superior.
        #PyQt5.QtWidgets.QVBoxLayout.addStretch(): Este método agrega un espacio elástico al layout que se 
        #expandirá para ocupar cualquier espacio adicional disponible dentro del contenedor.
        content_layout.addStretch()                             #Se agrega un espaciado stretch después.
        content_layout.addWidget(middle_widget2)                #Logo del contenedor del menú superior.
        
        #AÑADIENDO CONTENEDORES AL CONTENEDOR PRINCIPAL, QUE LOS ORDENA HORIZONTALMENTE DE ARRIBA A ABAJO: Es 
        #muy importante mencionar que para que el órden de los elementos se mantenga, se debe relacionar un 
        #widget a cada subcontenedor que se utilice en el diseño.
        main_layout.addWidget(menu_widget)                  #Se agrega el Widget menú al contenedor principal.
        #PyQt5.QtWidgets.QVBoxLayout.addStretch(): Este método agrega un espacio elástico al layout que se 
        #expandirá para ocupar cualquier espacio adicional disponible dentro del contenedor.
        main_layout.addStretch()                            #Se agrega un espaciado stretch después.
        main_layout.addWidget(content_widget)               #Se agrega el Widget medio al contenedor principal.
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
        self.show()
    
        #Instancia_Widget.evento_señal.connect(función_que_reacciona_al_evento): Este método se utiliza para 
        #enlazar un evento a un controlador de eventos, que es una función que se ejecuta cuando ocurra el 
        #evento, para ello se usa el nombre del widget, seguido del evento de tipo señal que detona el método, 
        #la palabra reservdada .connect() y entre paréntesis se coloca el nombre de la función que ejecutará 
        #alguna acción cuando ese evento ocurra. Normalmente las funciones que describen las acciones a 
        #realizar por los widgets de la GUI se encuentran dentro de esta misma clase, pero fuera de su 
        #constructor.
        # - Tipos de Eventos en Python: 
        #       - clicked: Señal emitida cuando se hace clic en un elemento, como un botón.
        #       - doubleClicked: Señal emitida cuando se hace doble clic en un elemento.
        #       - pressed: Señal emitida cuando se presiona un elemento, como un botón.
        #       - released: Señal emitida cuando se suelta un elemento, como un botón.
        #       - textChanged: Señal emitida cuando el texto de un elemento, como un campo de texto, cambia.
        #       - currentIndexChanged: Señal emitida cuando se cambia el índice seleccionado en un elemento, 
        #         como en un menú desplegable.
        #       - activated: Señal emitida cuando se selecciona un elemento, como un elemento de un menú 
        #         desplegable o una opción de una lista.
        #       - keyPressed: Señal emitida cuando se presiona una tecla en el teclado.
        #       - keyReleased: Señal emitida cuando se suelta una tecla en el teclado.
        #       - mousePressEvent: Señal emitida cuando se presiona un botón del mouse.
        #       - mouseReleaseEvent: Señal emitida cuando se suelta un botón del mouse.
        #       - mouseMoveEvent: Señal emitida cuando se mueve el mouse.
        #       - valueChanged: Señal emitida cuando se selecciona un nuevo elemento en un combo box (lista 
        #         desplegable).
        #       - timeout: Señal emitida cuando transcurre cada intervalo de tiempo especificado en un 
        #         temporizador.
        #Es importante mencionar que en  PyQt5, cuando se conecta una función a un evento, la función conectada 
        #puede recibir argumentos adicionales proporcionados por la señal emitida. Estos argumentos son 
        #transmitidos automáticamente por el sistema de señales y slots de PyQt5.
        # - Tipos de argumentos retornados al suceder un evento: 
        #       - *args y **kwargs: Muchas señales en PyQt5 permiten enviar argumentos adicionales a través de 
        #          *args (tupla de argumentos posicionales) y **kwargs (diccionario de argumentos de palabras 
        #          clave). Estos parámetros pueden variar según la señal específica y su contexto de uso.
        #       - checked: Algunas señales, como "clicked" en un botón, pueden enviar el estado de alternancia 
        #         del widget. Este parámetro indica si el widget está marcado y suele ser de tipo booleano.
        #       - text: En widgets de entrada de texto, como QLineEdit o QTextEdit, las señales pueden enviar el 
        #         texto ingresado o modificado como parámetro.
        #       - index: En widgets que tienen índices o selecciones, como QComboBox o QListView, las señales 
        #         pueden enviar el índice seleccionado como parámetro.
        #       - position: En widgets que trabajan con eventos de posición, como QMouseEvent, las señales 
        #         pueden enviar la posición del cursor o del evento como parámetro.
        #Al presionar el botón se ejecutará el método botonPresionado, declarado dentro de la misma clase.
        createButton1.clicked.connect(self.open_window1)
        createButton2.clicked.connect(self.open_window2)
        docButton1.clicked.connect(self.open_documentation_link1)
        docButton2.clicked.connect(self.open_documentation_link2)

    #función open_window1(): Método creado dentro de la clase propia llamada MainWindow que recibe como 
    #parámetro el evento que lo activa, para posteriormente ejecutar cierta acción.
    #En este caso el evento es activado cuando se presiona el botón y lo que hace es abrir una nueva ventana, 
    #que es instancia de la clase SecondaryWindow.
    def open_window1(self):
        #ABRIR SEGUNDA PANTALLA - INYECCIÓN DE DEPENDENCIAS CLASES PROPIAS DatabaseExcelHandler y SecondaryWindow:
        #Constantes del archivo ENUM_Constants.py:
        CONNECTION_STRING = AutomationConstants.CONNECTION_STRING.value #Constante PyODBC con server y database.
        SQL_QUERY_STRING = AutomationConstants.SQL_QUERY_STRING.value   #Constante con un SQL query.
        COMPAREDICC = AutomationConstants.COMPAREDICC.value             #Constante con un diccionario de filtrado.
        STATICDATA_ABOVE_AND_BELOW = AutomationConstants.STATICDATA_ABOVE_AND_BELOW.value   #Static Data.
        #DatabaseExcelHandler(): Objeto para extraer datos de la DB y crear un Excel.
        db_handler1 = DatabaseExcelHandler(CONNECTION_STRING, SQL_QUERY_STRING, COMPAREDICC, STATICDATA_ABOVE_AND_BELOW)
        EXCEL_FILE_PATH_1 = AutomationConstants.EXCEL_FILE_PATH_1.value #Constante del archivo ENUM_Constants.py
        table_copier1 = ExcelDataCopier(EXCEL_FILE_PATH_1, delay_segs = 20) #Objeto para copiar la tabla del Excel.
        #SecondaryWindow(): Creación de ventana adicional.
        secondary_window = SecondaryWindow("Ventana 1", db_handler1, table_copier1, EXCEL_FILE_PATH_1, STATICDATA_ABOVE_AND_BELOW, showTable = True) 
        secondary_window.setStyleSheet("background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 rgb(255, 255, 255), stop:1 rgb(179, 185, 188));")
        secondary_window.showMaximized()                #showMaximized(): Método para abrir maximizada una ventana.
        #En el código de la ventana principal MainWindow se creó una variable de lista vacía llamada 
        #self.open_windows, esta se utiliza cuando se quiera abrir ventanas nuevas, ya que cada vez que se hace 
        #clic en uno de los botones, se crea una nueva instancia de SecondaryWindow, pero si esta no se mantiene 
        #en ningún lugar, las ventanas se destruirán inmediatamente porque Python no tiene ninguna referencia a 
        #ellas. Al crear la lista self.open_windows en la clase MainWindow, proporcionamos un lugar para 
        #almacenar todas las instancias de la clase SecondaryWindow, asegurando que la ventana no se cierre 
        #después de que el método haya terminado de ejecutarse.
        self.open_windows.append(secondary_window)      #Instancia añadida a la lista de ventanas abiertas.
        #Si el archivo se ha creado correctamente, se ajusta el ancho de sus celdas a través de un objeto de 
        #la clase ExcelCellAdjuster. 
        anchoMaximoCelda = 40                                           #Ancho máximo de la celda de 40 letras.
        adjuster = ExcelCellAdjuster(EXCEL_FILE_PATH_1, anchoMaximoCelda)  #Instancia de la clase ExcelCellAdjuster.
        adjuster.ajustar_celdas()                                       #Método ajustar_celdas().
    #función open_window2(): Abre una ventana con una tabla vacía.
    def open_window2(self):
        #ABRIR SEGUNDA PANTALLA - INYECCIÓN DE DEPENDENCIAS CLASES PROPIAS DatabaseExcelHandler y SecondaryWindow:
        #Constantes del archivo ENUM_Constants.py:
        CONNECTION_STRING = AutomationConstants.CONNECTION_STRING.value #Constante PyODBC con server y database.
        SQL_QUERY_STRING = AutomationConstants.SQL_QUERY_STRING.value   #Constante con un SQL query.
        COMPAREDICC = AutomationConstants.COMPAREDICC.value             #Constante con un diccionario de filtrado.
        STATICDATA_ABOVE_AND_BELOW = AutomationConstants.STATICDATA_ABOVE_AND_BELOW.value   #Static Data.
        #DatabaseExcelHandler: Objeto para extraer datos de la DB y crear un Excel.
        db_handler2 = DatabaseExcelHandler(CONNECTION_STRING, SQL_QUERY_STRING, COMPAREDICC, STATICDATA_ABOVE_AND_BELOW)
        EXCEL_FILE_PATH_2 = "C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/a1.-Data Science/0.-Archivos_Ejercicios_Python/a23.-GUI PyQt5 Conexion DataBase/23.-Reporte Analisis de Datos 2.xlsx"
        table_copier2 = ExcelDataCopier(EXCEL_FILE_PATH_2, delay_segs = 20) #Objeto para copiar la tabla del Excel.
        #SecondaryWindow(): Creación de ventana adicional.
        secondary_window = SecondaryWindow("Ventana 2", db_handler2, table_copier2, EXCEL_FILE_PATH_2, STATICDATA_ABOVE_AND_BELOW, showTable = False)
        secondary_window.setStyleSheet("background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 rgb(255, 255, 255), stop:1 rgb(179, 185, 188));")
        secondary_window.showMaximized()                #showMaximized(): Método para abrir maximizada una ventana.
        self.open_windows.append(secondary_window)      #Instancia añadida a la lista de ventanas abiertas.

    #función open_documentation_link1(): Método creado dentro de la clase propia llamada MainWindow que recibe como 
    #parámetro el evento que lo activa, para posteriormente ejecutar cierta acción. La acción es simplemente abrir 
    #el navegador en un sitio web.
    def open_documentation_link1(self):
        #webbrowser.open(): Método que abre el navegador web predeterminado del sistema operativo en la dirección 
        #URL especificada.
        webbrowser.open("https://dicer0.com/")
    def open_documentation_link2(self):
        #webbrowser.open(): Método que abre el navegador web predeterminado del sistema operativo en la dirección 
        #URL especificada.
        webbrowser.open("https://github.com/dicer0")


#__name__ == __main__: Método main, esta función es super importante ya que sirve para instanciar las clases del 
#programa y ejecutar sus métodos, en python pueden existir varios métodos main en un solo programa, aunque no es 
#una buena práctica.
if __name__ == "__main__":
    #Instancia de la librería PyQt5 por medio del constructor de la clase QApplication, que hereda de la clase 
    #QtWidgets para crear un objeto que funcione como la base de una GUI.
    # - sys.argv: Se refiere a un vector llamado "argument vector" que puede ser accedido desde la librería sys, 
    #   este incluye en su contenido el nombre del archivo que se quiere ejecutar y los argumentos necesarios 
    #   que se le deben pasar para que efectúe su ejecución. Se le debe pasar como parámetro al constructor de 
    #   la clase QApplication para que se pueda crear la base de la GUI.
    #       - Por ejemplo, si se ejecutara el siguiente comando en consola:
    #           python mi_script.py arg1 arg2 arg3
    #         El contenido de sys.argv sería:
    #           ['mi_script.py', 'arg1', 'arg2', 'arg3']
    app = QtWidgets.QApplication(sys.argv)
    #Instancia de nuestra clase propia llamada MainWindow que fue creada en este mismo programa (window se 
    #refiere a la ventana del GUI en PyQt5) e incluye una instancia de la clase GraficaPyQt5 para agregar un 
    #widget que crea una gráfica dentro, el constructor vacío lo que hace es indicar que se cree y muestre la 
    #ventana.
    window = MainWindow()
    #widget.setStyleSheet(): Método que permite aplicar código CSS (la mayoría de métodos, no todos) a los 
    #widgets de una interfaz gráfica de usuario (GUI).
    window.setStyleSheet("background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 rgb(255, 255, 255), stop:1 rgb(179, 185, 188));")
    #PyQt5.QtWidgets.QMainWindow.show() = window.show(): Método aplicado al objeto de la clase QMainWindow, 
    #del que hereda esta clase propia para mostrar la ventana del GUI.
    window.show()
    #PyQt5.QtWidgets.QApplication.exec_(): Método para que se ejecute en un loop infinito el GUI, logrando así 
    #que no se ejecute una vez y luego cierre por sí solo, sino que solo se cierre solamente al dar clic en el 
    #tache del window.
    app.exec_()