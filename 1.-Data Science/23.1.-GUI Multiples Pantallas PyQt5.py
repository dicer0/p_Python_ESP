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
#PyQt5 - QtWidgets: Clase que incluye métodos para trabajar con temporizadores, tamaño de elementos, fechas, 
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
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Time Zone Selector")
        self.setGeometry(100, 100, 900, 500)
        self.open_windows = []  # List to hold references to opened windows

        self.create_widgets()
        
    def create_widgets(self):
        # Logo
        logo_label = QtWidgets.QLabel()
        iconPath = "C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/1.-Data Science/0.-Archivos_Ejercicios_Python/Img/logoDi_cer0MarkIII.png"
        pixmap = QtGui.QPixmap(iconPath)
        # Resize the image
        pixmap = pixmap.scaled(200, 200, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        logo_label.setPixmap(pixmap)
        
        # Text in the middle
        text_label = QtWidgets.QLabel(text ="<p style = 'font-size: 30px; font-family: Consolas, monospace; color: white; font-weight: bold;'>" +
                                                "GUI MultiPantalla"
                                            "</p>")
        
        # ComboBox for time zones
        self.timezones_combo = QtWidgets.QComboBox()
        self.timezones_combo.setStyleSheet("font-size: 15px; font-family: Consolas, monospace; color: #002550; font-weight: bold; background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 rgb(255, 255, 255), stop:1 rgb(179, 185, 188))")
        self.timezones_combo.addItems(["GMT", "UTC", "CET", "PST", "EST"])
        
        # Container for squares
        self.container_layout = QtWidgets.QHBoxLayout()
        self.container_layout.addWidget(self.create_square("Square 1", "This is square 1", "Create 1", 1))
        self.container_layout.addWidget(self.create_square("Square 2", "This is square 2", "Create 2", 2))
        
        # Main layout
        main_layout = QtWidgets.QVBoxLayout()
        
        # Create a widget to contain the menu items
        menu_widget = QtWidgets.QWidget()
        menu_layout = QtWidgets.QHBoxLayout(menu_widget)
        menu_layout.addWidget(logo_label)
        menu_layout.addWidget(text_label)
        menu_layout.addWidget(self.timezones_combo)
        
        # Set fixed height for the menu widget
        menu_widget.setFixedHeight(100)
        
        # Apply the background color to the menu widget
        menu_widget.setStyleSheet("background-color: #002550;")
        
        main_layout.addWidget(menu_widget)
        main_layout.addStretch()  # Add stretch to push the next widget to the top
        
        # Create a light gray container widget
        light_gray_container = QtWidgets.QWidget()
        light_gray_container.setStyleSheet("background-color: transparent; font-size: 20px; font-family: Consolas, monospace; color: #002550; font-weight: bold;")
        light_gray_layout = QtWidgets.QVBoxLayout(light_gray_container)
        light_gray_layout.addStretch()  # Add stretch to push content to the middle
        light_gray_layout.addLayout(self.container_layout)
        light_gray_layout.addStretch()  # Add stretch to push content to the middle
        
        main_layout.addWidget(light_gray_container)
        main_layout.addStretch()  # Add stretch to push content to the middle
        
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        
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