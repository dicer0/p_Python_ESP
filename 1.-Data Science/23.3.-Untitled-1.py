# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtGui
import sys

#Clase personalizada para la extracción de datos de la database y creación de un archivo de Excel.
from Clases_Personalizadas.POO_23_3_DataBaseExcel.POO_DB_ExcelReport import DatabaseExcelHandler

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Time Zone Selector")
        self.setGeometry(100, 100, 1000, 500)
        self.open_windows = []
        #WIDGETS MENU:
        iconPath = "C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/1.-Data Science/0.-Archivos_Ejercicios_Python/Img/logoDi_cer0MarkIII.png"
        pixmap = QtGui.QPixmap(iconPath)
        scaledImage = pixmap.scaled(200, 200, QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        logo_label = QtWidgets.QLabel(pixmap = scaledImage)
        text_menu =  QtWidgets.QLabel(text ="<p style = 'font-size: 30px; font-family: Consolas, monospace; color: white; font-weight: bold;'>" +
                                                "GUI MultiPantalla"
                                            "</p>")
        self.timezones_combo = QtWidgets.QComboBox()
        self.timezones_combo.setStyleSheet("font-size: 15px; font-family: Consolas, monospace; color: #002550; font-weight: bold; background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 rgb(255, 255, 255), stop:1 rgb(179, 185, 188))")
        self.timezones_combo.addItems(["GMT", "UTC", "CET", "PST", "EST"])
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
        iconPath = "C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/1.-Data Science/0.-Archivos_Ejercicios_Python/Img/LogoBlancoDi_cer0.png"
        logoButton = QtGui.QIcon(iconPath)
        docButton1 = QtWidgets.QPushButton(text = "", icon = logoButton, iconSize = QtCore.QSize(30, 30))
        createButton1 = QtWidgets.QPushButton(text = "Create")
        docButton2 = QtWidgets.QPushButton(text = "", icon = logoButton, iconSize = QtCore.QSize(30, 30))
        createButton2 = QtWidgets.QPushButton(text = "Create")
        doctButtonStyle = "background-color: transparent; max-width: 50px; height: 50px; border: 2px solid #e6ebf3; border-radius: 23px;"
        docButton1.setStyleSheet(doctButtonStyle)
        docButton2.setStyleSheet(doctButtonStyle)
        createButtonStyle = "min-width: 100px; height: 50px; font-size: 17px; font-weight: bold; font-family: Consolas, monospace; color: white; background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 rgb(0,187,255), stop:1 rgb(0,125,173));"
        createButton1.setStyleSheet(createButtonStyle)
        createButton2.setStyleSheet(createButtonStyle)
        
        #CONTENEDORES DE ELEMENTOS: La biblioteca PyQt5 ofrece varios tipos de contenedores que se pueden 
        main_layout = QtWidgets.QVBoxLayout()
        menu_widget = QtWidgets.QWidget()
        menu_widget.setFixedHeight(100)
        menu_widget.setStyleSheet("background-color: #002550; height: 20px;")
        menu_layout = QtWidgets.QHBoxLayout(menu_widget)
        middle_widget1 = QtWidgets.QWidget()
        middle_widget2 = QtWidgets.QWidget()
        content_widget = QtWidgets.QWidget()
        middleWidgetStyle = "background-color: white; height: 100px; padding: 5px; border-radius: 25px;"
        middle_widget1.setStyleSheet(middleWidgetStyle)
        middle_widget2.setStyleSheet(middleWidgetStyle)
        content_widget.setStyleSheet("background-color: transparent;")
        self.individual_layout1 = QtWidgets.QGridLayout(middle_widget1)
        self.individual_layout2 = QtWidgets.QGridLayout(middle_widget2)
        content_layout = QtWidgets.QHBoxLayout(content_widget)
        menu_layout.addWidget(logo_label)
        menu_layout.addWidget(text_menu)
        menu_layout.addWidget(self.timezones_combo)
        #CONTENEDOR INTERMEDIO 1:
        self.individual_layout1.addWidget(element_title1, 0, 0)
        self.individual_layout1.addWidget(element_text1, 1, 0)
        self.individual_layout1.addWidget(buttons_text1, 2, 0)
        self.individual_layout1.addWidget(docButton1, 2, 1)
        self.individual_layout1.addWidget(createButton1, 2, 2)
        #CONTENEDOR INTERMEDIO 2:
        self.individual_layout2.addWidget(element_title2, 0, 0)
        self.individual_layout2.addWidget(element_text2, 1, 0)
        self.individual_layout2.addWidget(buttons_text2, 2, 0)
        self.individual_layout2.addWidget(docButton2, 2, 1)
        self.individual_layout2.addWidget(createButton2, 2, 2)
        #CONTENEDOR DE LOS 2 INTERMEDIOS:
        content_layout.addWidget(middle_widget1)
        content_layout.addStretch()
        content_layout.addWidget(middle_widget2)
        
        #AÑADIENDO CONTENEDORES AL CONTENEDOR PRINCIPAL, QUE LOS ORDENA HORIZONTALMENTE DE ARRIBA A ABAJO:
        main_layout.addWidget(menu_widget)
        main_layout.addStretch()
        main_layout.addWidget(content_widget)
        main_layout.addStretch()
        
        #Creación de un objeto QWidget para acomodar el contenedor principal dentro del frame.
        centralWidget = QtWidgets.QWidget()
        centralWidget.setLayout(main_layout)
        self.setCentralWidget(centralWidget)
        self.show()
        createButton1.clicked.connect(self.open_window1)
        createButton2.clicked.connect(self.open_window2)

    #función open_window1(): Método creado dentro de la clase propia llamada MainWindow que recibe como 
    #parámetro el evento que lo activa, para posteriormente ejecutar cierta acción.
    #En este caso el evento es activado cuando se presiona el botón y lo que hace es abrir una nueva ventana, 
    #que es instancia de la clase SecondaryWindow.
    def open_window1(self):
        #ABRIR SEGUNDA PANTALLA:
        secondary_window = SecondaryWindow("Ventana 1")
        secondary_window.setStyleSheet("background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 rgb(255, 255, 255), stop:1 rgb(179, 185, 188));")
        secondary_window.showMaximized()
        self.open_windows.append(secondary_window)
    def open_window2(self):
        #ABRIR SEGUNDA PANTALLA:
        secondary_window = SecondaryWindow("Ventana 2")
        secondary_window.setStyleSheet("background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 rgb(255, 255, 255), stop:1 rgb(179, 185, 188));")
        secondary_window.showMaximized()
        self.open_windows.append(secondary_window)


class SecondaryWindow(QtWidgets.QMainWindow):
    def __init__(self, title):
        super().__init__()
        self.setWindowTitle(title)
        
        #EXTRAER DATOS DE LA BASE DE DATOS Y CREAR UN REPORTE EN EXCEL:
        db_handler = DatabaseExcelHandler('mysql+pymysql://root:PincheTonto!123@localhost:3306/1_platziblog_db')
        resultDataFrame = db_handler.process_data_and_save_to_excel("C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/1.-Data Science/0.-Archivos_Ejercicios_Python/23.-GUI PyQt5 Conexion DataBase/23.-Reporte Analisis de Datos.xlsx")
        print(resultDataFrame)
        #QtWidgets.QTableWidget(): Widget que proporciona una funcionalidad de hoja de cálculo o tabla editable 
        #para mostrar filas y columnas de información en una GUI de PyQt5, las cuales pueden contener texto, 
        #números, imágenes u otros widgets.
        table = QtWidgets.QTableWidget()
        #Analizar la tabla para crear un archivo de Excel estático, que tenga información vacía e información 
        #que se llena de forma automática. 
        headers = resultDataFrame.columns.tolist()
        resultDataFrame.loc[-1] = headers
        resultDataFrame.index = resultDataFrame.index + 1
        resultDataFrame = resultDataFrame.sort_index()
        num_rows, num_cols = resultDataFrame.shape
        table.setRowCount(num_rows)
        table.setColumnCount(num_cols)
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
        
        #CREACIÓN DE WIDGETS DE LAS VENTANAS ADICIONALES, QUE NO SON LA TABLA:
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
        #CONTENEDORES:
        widgetContenedor = QtWidgets.QWidget()
        widgetContenedor.setFixedHeight(100)
        widgetContenedor.setStyleSheet("background-color: #002550; padding: 5px;")
        contenedorMatricial = QtWidgets.QGridLayout(widgetContenedor)
        contenedorVertical = QtWidgets.QVBoxLayout()
        contenedorMatricial.addWidget(texto_1, 0, 0)
        contenedorMatricial.addWidget(texto_2, 1, 0)  
        contenedorMatricial.addWidget(confirmButton, 1, 2)
        contenedorVertical.addWidget(table) 
        contenedorVertical.addWidget(widgetContenedor)
        centralWidget = QtWidgets.QWidget()      
        centralWidget.setLayout(contenedorVertical)
        self.setCentralWidget(centralWidget)         

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setStyleSheet("background: qlineargradient(x1:1, y1:1, x2:0, y2:0, stop:0 rgb(255, 255, 255), stop:1 rgb(179, 185, 188));")
    window.show()
    app.exec_()