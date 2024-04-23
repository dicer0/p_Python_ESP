# -*- coding: utf-8 -*-

#En Python se introducen comentarios de una sola linea con el simbolo #.
#La primera línea de código incluida en este programa se conoce como declaración de codificación o codificación 
#de caracteres. Al especificar utf-8 (caracteres Unicode) como la codificación, nos aseguramos de que el archivo 
#pueda contener caracteres especiales, letras acentuadas y otros caracteres no ASCII sin problemas, garantizando 
#que Python interprete correctamente esos caracteres y evite posibles errores de codificación.
#Se puede detener una ejecución con el comando [CTRL] + C puesto en consola, con el comando "cls" se borra su 
#historial y en Visual Studio Code con el botón superior derecho de Play se corre el programa.
#Para comentar en Visual Studio Code varias líneas de código se debe pulsar:
#[CTRL] + K (VSCode queda a la espera). Después pulsa [CTRL] + C para comentar y [CTRL] + U para descomentar.

#enum: Librería que permite declarar enumeraciones (enum) en Python, las cuales son un conjunto de nombres 
#simbólicos (miembros) que están vinculados a valores constantes. Su utilidad principal radica en la legibilidad 
#y mantenibilidad del código, además de que de esta manera se pueden separar datos sensibles que necesitan más 
#seguridad como claves, contraseñas, etc. en un archivo por separado. La sintaxis para usar un enum es:
# - Clase donde se declaran los enums dentro de un archivo file_enums.py:
#       class nombreClasePersonalizadaQueHeredaDeEnum(enum.Enum):
#           NOMBRE_CONSTANTE = VALOR
# - Clase donde se importan los enums para utilizarlos:
#       from path.file_enums import nombreClasePersonalizadaQueHeredaDeEnum
#       constanteEnum = nombreClasePersonalizadaQueHeredaDeEnum.NOMBRE_CONSTANTE.value
import enum

#AutomationConstants(): Clase propia que hereda de enum.Enum para poder declarar enums en el código.
class AutomationConstants(enum.Enum):
    #SENSITIVE DATA:
    #Datos que se importan dentro de la clase DatabaseExcelHandler:
    #SQL_QUERY_STRING: Query para consulta a una base de datos que se conecta a través de la librería PyODBC, 
    #para ello pide el nombre del servidor y la base de datos a donde nos queremos conectar a través de la 
    #constante CONNECTION_STRING, que de igual manera se encuentra dentro de este ENUM.
    SQL_QUERY_STRING  =  """SELECT 	  * 
                            FROM 	    posts
                            ORDER BY  titulo DESC;"""
    #COMPAREDICC: Diccionario de filtrado que compara cada dato extraído del database con los Datos de filtrado 
    #y conserva solamente los que tengan un valor igual, además de que en el diccionario final añade ciertos 
    #Datos que así se pasan al diccionario final.
    COMPAREDICC = [{
        "tituloStatic": "Grupo de Datos 1",     #Datos que así se pasan al diccionario final.
        "datoStatic": "Dato grupo 1",         
        "estatusFilter": "activo",              #Datos de filtrado.
        "userIdFilter": 1,
        "categoryIdFilter": 2
    },
    {
        "tituloStatic": "Grupo de Datos 2",     #Datos que así se pasan al diccionario final.
        "datoStatic": "Dato grupo 2",         
        "estatusFilter": "inactivo",            #Datos de filtrado.
        "userIdFilter": 2,
        "categoryIdFilter": 3
    }]

    #Datos que se importan dentro de la clase DatabaseExcelHandler y SecondaryWindow:
    #STATICDATA_ABOVE_AND_BELOW: Son los datos estáticos que se añaden encima y abajo de la tabla dinámica 
    #extraída y filtrada de una base de datos, esto se utiliza para darle formato al Excel creado con los datos 
    #estáticos/dinámicos y para darle formato de forma separada al QTableWidget de la GUI hecha con PyQt5. 
    STATICDATA_ABOVE_AND_BELOW = [
        #STATICDATA_ABOVE_1
        [
            ['Title A1.1', 'Title A1.2', 'Title A1.3'],
            ['Static Row 1', '', ''],
            ['Static Row 2', '', ''],
            ['Static Row 3', '', ''],
            ['Static Row 4', '', ''],
            ['Static Row 5', '', ''],
            ['Static Row 6', '', '']
        ],
        #STATICDATA_ABOVE_2
        [
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
        ],
        #STATICDATA_BELOW_1
        [
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
    ]
    print("STATICDATA_ABOVE_1 = ", STATICDATA_ABOVE_AND_BELOW[0], "\n")
    print("STATICDATA_ABOVE_2 = ", STATICDATA_ABOVE_AND_BELOW[1], "\n")
    print("STATICDATA_BELOW_1 = ", STATICDATA_ABOVE_AND_BELOW[2], "\n")

    #Datos que se importan dentro de la clase principal MainWindow:
    #CONNECTION_STRING: Este string de conexión se le pasa como parámetro a cualquier objeto de la clase 
    #DatabaseExcelHandler para lograr así que este se pueda conectar a la base de datos y realizar sus 
    #funciones, para ello este pide el nombre del servidor y la base de datos a donde nos queremos conectar. 
    CONNECTION_STRING = 'DRIVER={MySQL ODBC 8.3 Unicode Driver}; SERVER=localhost;PORT=3306;DATABASE=1_platziblog_db;USER=root;PASSWORD=Diego1234;'
    #EXCEL_FILE_PATH_1: Este string indica la ruta global o local de donde se guardará el archivo de Excel 
    #usado para almacenar temporalmente los datos filtrados antes de mandarlos al portapapeles (clipboard).
    EXCEL_FILE_PATH_1 = "C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/1.-Data Science/0.-Archivos_Ejercicios_Python/23.-GUI PyQt5 Conexion DataBase/23.-Reporte Analisis de Datos 1.xlsx"