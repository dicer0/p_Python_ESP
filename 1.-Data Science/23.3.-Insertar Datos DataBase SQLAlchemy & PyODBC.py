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

#SQLAlchemy: Para instalarlo se debe ejecutar el comando pip install sqlalchemy, y es una biblioteca de Python 
#para SQL ORM (Object-Relacional-Mapping) que proporciona a los desarrolladores un conjunto de herramientas para 
#interactuar con bases de datos utilizando objetos y métodos de Python, en lugar de escribir consultas SQL.
#Entidad: Se refiere a una tabla que almacena datos sobre un tipo de objeto o elemento del mundo real. Cada fila 
#en la tabla representa una instancia individual de esa entidad, y cada columna representa un atributo o 
#característica de esa entidad.
#Atributo: Son las columnas de una tabla que representan las características o propiedades de la entidad que está 
#siendo modelada, todas ellas tienen un nombre y tipo de dato asociado.
#Registro: También conocido como "fila" o "tupla", representa una instancia individual de una entidad en la tabla. 
#Cada registro contiene los valores de los atributos correspondientes a esa instancia específica de la entidad.

#SQLAlchemy - create_engine: El método create_engine sirve para configurar la conexión a la base de datos.
from sqlalchemy import create_engine
#SQLAlchemy - text: El método text se utiliza para crear un objeto de expresión textual que recibe como parámetro 
#el código de una consulta SQL en forma de String.
from sqlalchemy import text
#SQLAlchemy - Column: La clase Column de la biblioteca SQLAlchemy se utiliza para definir las columnas 
#(atributos) en las tablas (entidades) de la base de datos utilizando el mapeo de objeto-relacional (ORM).
from sqlalchemy import Column
#SQLAlchemy - Integer, String, CHAR: Son los tipos de datos que pueden adoptar los objetos Column.
from sqlalchemy import Integer, String, CHAR
#SQLAlchemy.ext.declarative - declarative_base: El método declarative_base perteneciente al paquete orm permite 
#definir clases de modelo en Python, las cuales definen la estructura de los datos que se busca crear o manipular 
#en una database. Luego estas se mapean automáticamente a una tabla (entidad) en una base de datos relacional.
from sqlalchemy.orm import declarative_base
#SQLAlchemy.orm - sessionmaker: Una vez que se hayan definido las clases de modelo (si es que se quiere ingresar 
#datos a la DB) y se haya configurado la conexión a la base de datos con el método create_engine, es necesario 
#crear sesiones para poder realizar operaciones del CRUD (Create-Read-Update-Delete) como agregar, modificar o 
#eliminar filas (registros) en las tablas (entidades) de la base de datos.
from sqlalchemy.orm import sessionmaker
#pandas: Librería que proporciona estructuras de datos y herramientas de manipulación y análisis de datos. 
import pandas

#CONFIGURAR LA CONEXIÓN A DISTINTOS TIPOS DE BASES DE DATOS: Para ello de igual manera se debe realizar la
#instalación de diferentes librerías.
#MANEJO DE EXCEPCIONES: Es una parte de código que se conforma de 2 o3 partes, try, except y finally: 
# - Primero se ejecuta el código que haya dentro del try, y si es que llegara a ocurrir una excepción durante su 
#   ejecución, el programa brinca al código del except.
# - En la parte de código donde se encuentra la palabra reservada except, se ejecuta cierta acción cuando ocurra 
#   el error esperado.
# - Por último, cuando no ocurra una excepción durante la ejecución del gestor de excepciones, se ejecutará el 
#   código que esté incluido dentro del finally después de haber terminado de ejecutar lo que haya en el try, pero
#   si ocurre una excepción, la ejecución terminará cuando se llegue al except.
#Se utiliza esta arquitectura de código cuando se quiera efectuar una acción donde se espera que pueda ocurrir un 
#error durante su ejecución.
#1.- MySQL: create_engine('mysql+pymysql://username:password@hostname:port/database_name')
#instalation: pip install mysqlclient
#instalation: pip install pymysql
try:
    #create_engine: Método que sirve para configurar la conexión a un tipo de base de datos en específico.
    mysql_engine = create_engine('mysql+pymysql://root:PincheTonto!123@localhost:3306/1_platziblog_db')
    #CONTEXTO DE EJECUCIÓN: Es un concepto de programación que se utiliza cuando se quiere trabajar con recursos 
    #que necesitan ser gestionados de forma prioritaria, como una apertura de archivos, conexiones de red o 
    #conexiones a bases de datos. Su sintaxis básica es la siguiente: 
    #       with expresion as variable:
    # - expresion: Este parámetro recibe un método que devuelva un objeto, ya que este se comportará como el 
    #   "contexto de ejecución", osea el recurso que debe ser gestionado, un ejemplo es open('archivo.txt', 'r').
    # - variable: Es el nombre de la variable que se asigna al objeto de contexto dentro del bloque with.
    #Utilizar el operador with es igual a asignar una variable, la única diferencia es que al utilizar el operador
    #with nos aseguramos que el objeto que devuelva el método utilizado sea gestionado por un entorno temporal y 
    #complete sus tareas correctamente, como cerrar un archivo, incluso si ocurren errores: 
    #   nombreVariable = método() 
    #   with método() as nombreVariable
    #De igual manera, el operador with se asegura que no debamos guardar el archivo al terminar la acción, o cerrar 
    #una conexión a la base de datos, ya que esta se maneja de forma automática por el operador.
    #create_engine().connect(): El método .connect() sirve para establecer la conexión con la base de datos.
    with mysql_engine.connect() as connection1:
        print("1.- MySQL Connection successful!!!")
        #OBTENCIÓN DE DATOS DE LA BASE DE DATOS: Ya que estemos seguros que la conexión a la base de datos se ha 
        #realizado de forma exitosa, podremos utilizar comandos SQL para filtrar y obtener cierta información, esto se 
        #realiza a través de la variable que haya utilizado el método .connect(), el método .execute() y .text().  
        SQL_Query_string =  """SELECT 	  * 
                                FROM 	    posts
                                ORDER BY  titulo DESC;"""
        SQL_TextObject = text(SQL_Query_string)
        #.create_engine().connect().execute(): Ya que se haya realizado la conexión con la base de datos, a través de 
        #un objeto de variable textual (text) se puede realizar una consulta a la base de datos a través de SQL y lo 
        #que devuelve es un objeto llamado ResultProxy, el cual en algunas cosas se maneja como un diccionario.
        resultProxy = connection1.execute(SQL_TextObject)
        print("Tipo de Dato ResultProxy: ", type(resultProxy))
        #pandas.DataFrame: La clase DataFrame de la librería pandas representa una estructura de datos matricial en 
        #forma de tablas que pueden contener datos de diferentes tipos y se pueden manipular de manera eficiente para 
        #realizar diversas operaciones de análisis de datos, su constructor recibe los siguientes parámetros:
        # - data: Este es el parámetro principal que especifica los datos que se utilizarán para crear el DataFrame.
        #   Puede ser un diccionario, una lista de listas, un numpyArray, otra estructura de datos de Pandas (como 
        #   otro DataFrame o una Serie), etc.
        # - index (opcional): Este parámetro especifica las etiquetas de índice para las filas del DataFrame. 
        #   Puede ser una lista, una matriz, una Serie, etc. Si no se especifica, se utilizarán índices enteros.
        # - columns (opcional): Este parámetro opcional especifica los nombres de las columnas del DataFrame. Si no 
        #   se especifica, se utilizarán nombres de columnas predeterminados (0, 1, 2, ...).
        #       - .keys(): Como los objetos ResultProxy se manejan como diccionarios, se puede obtener el nombre de 
        #         sus etiquetas (keys) para de esa manera asignar los nombres de las columnas de un DataFrame, pero 
        #         si se quisiera obtener sus valores, no existe un método .values(), se debe acceder de otra forma. 
        # - dtype (opcional): Este parámetro especifica el tipo de datos para cada columna del DataFrame.
        dataFramePandas = pandas.DataFrame(data = resultProxy, columns = resultProxy.keys())    
        print(dataFramePandas, "\n")
except Exception as error:
    print("1.- Ups an Error ocurred while Opening the MySQL DataBase:\n" + str(error) + "\n")

#MANDAR DATOS A LA BASE DE DATOS:
#declarative_base(): Método para definir clases de modelo en python para mandar datos a la DB por medio del ORM.
Base = declarative_base()
#Las clases que vayan a mandar datos a la DB deben heredar de la variable que haya usado el método 
#declarative_base().
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(CHAR)

#Create a session to interact with the database
Session = sessionmaker(bind = mysql_engine)
session = Session()

#Example: Inserting data into the database
new_user = User(name = 'John', age = 30, gender = 'm')
session.add(new_user)
session.commit()

#Example: Querying data from the database
users = session.query(User).all()
for user in users:
    print(user.name, user.age)

#Close the session when done
session.close()