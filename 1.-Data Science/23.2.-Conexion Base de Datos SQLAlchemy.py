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
#MANEJO DE EXCEPCIONES: Es una parte de código que se conforma de dos partes, try y except: 
# - Primero se ejecuta el código que haya dentro del try y si es que llegara a ocurrir una excepción durante su 
#   ejecución, el programa brinca al código del except
# - En la parte de código donde se encuentra la palabra reservada except, se ejecuta cierta acción cuando ocurra 
#   el error esperado. 
#Se utiliza esta arquitectura de código cuando se quiera efectuar una acción donde se espera que pueda ocurrir un 
#error durante su ejecución.
#1.- MySQL: create_engine('mysql+pymysql://username:password@hostname:port/database_name')
#instalation: pip install mysqlclient
#instalation: pip install pymysql
informacionDB = []  #Array que almacenará lo que trae el ORM de la base de datos.
try:
    mysql_engine = create_engine('mysql+pymysql://root:PincheTonto!123@localhost:3306/1_platziblog_db')
    #create_engine().connect(): El método .connect() sirve para establecer la conexión con la base de datos.
    connection1 = mysql_engine.connect()
    print("1.- MySQL Connection successful!!!\n")

    #OBTENCIÓN DE DATOS DE LA BASE DE DATOS: Ya que estemos seguros que la conexión a la base de datos se ha 
    #realizado de forma exitosa, podremos utilizar comandos SQL para filtrar y obtener cierta información, 
    #esto se realiza a través de la variable que haya utilizado el método .connect(), el método .execute() y 
    #.text().  
    SQL_Query_string =  """SELECT 	  * 
                            FROM 	    posts
                            ORDER BY  titulo DESC;"""
    SQL_TextObject = text(SQL_Query_string)
    #.create_engine().connect().execute(): Ya que se haya realizado la conexión con la base de datos, a través 
    #de un objeto de variable textual (text) se puede realizar una consulta a la base de datos a través de SQL
    #y lo que devuelve es un objeto llamado ResultProxy, el cual en algunas cosas se maneja como un diccionario.
    resultProxy = connection1.execute(SQL_TextObject)
    print("Tipo de Dato ResultProxy: ", type(resultProxy))
    #pandas.DataFrame: La clase DataFrame representa una estructura de datos matricial en forma de tablas que 
    #pueden contener datos de diferentes tipos y se pueden manipular de manera eficiente para realizar diversas 
    #operaciones de análisis de datos, para crear un objeto su constructor recibe los siguientes parámetros:
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

    #CERRAR LA CONEXIÓN:
    #.create_engine().connect().execute().close(): El cerrar la conexión con la consulta hecha con el método 
    #.execute() asegura que se liberen los recursos asociados con ese objeto una vez que se haya terminado la 
    #consulta. Aunque no es estrictamente necesario hacer esto, es una buena práctica para limpiar y liberar 
    #cualquier recurso adicional que pueda estar asociado con él.
    resultProxy.close()
    #create_engine().close(): El método .close() sirve para cerrar una conexión previamente establecida con el 
    #método .connect().
    connection1.close()
except Exception as error:
    print("1.- Ups an Error ocurred while Opening the MySQL DataBase:\n" + str(error) + "\n")
#2.- PostgreSQL: create_engine('postgresql://username:password@hostname:port/database_name')
#instalation: pip install psycopg2 
try:
    postgresql_engine = create_engine('postgresql://username:password@hostname:port/database_name')
    connection2 = postgresql_engine.connect()
    print("2.- PostgresSQL Connection successful!!!\n")
    connection2.close()
except Exception as error:
    print("2.- Ups an Error ocurred while Opening the PostgresSQL DataBase:\n" + str(error) + "\n")
#3.- SQLite (path relativo): create_engine('sqlite:///mydatabase.db')
#No additional installation is needed.
try:
    sqlite_engine_relative = create_engine('sqlite:///mydatabase.db')
    connection3 = sqlite_engine_relative.connect()
    print("3.- SQLite Connection successful!!!\n")
    connection3.close()
except Exception as error:
    print("3.- Ups an Error ocurred while Opening the SQLite DataBase with a Relative Path:\n" + str(error) + "\n")
#4.- SQLite (path absoluto): create_engine('sqlite:////absolute/path/to/mydatabase.db')
#No additional installation is needed.
try:
    sqlite_engine_absolute = create_engine('sqlite:////absolute/path/to/mydatabase.db')
    connection4 = sqlite_engine_absolute.connect()
    print("4.- SQLite Connection successful!!!\n")
    connection4.close()
except Exception as error:
    print("4.- Ups an Error ocurred while Opening the SQLite DataBase with an Absolute Path:\n" + str(error) + "\n")
#5.- Microsoft SQL Server (Windows authentication): create_engine('mssql+pyodbc://@mydsn')
#instalation: pip install pyodbc
#Este tipo de conexión es más compleja que las demás, ya que se debe ejecutar un paso intermedio donde se crea un 
#acceso llamado ODBC (Open DataBase Connectivity), que es una  API estándar de la industria diseñada para permitir 
#que las distintas aplicaciones (código backend Python, Node.js, Java, etc.) puedan acceder a diferentes tipos de 
#bases de datos y/o sistemas de gestión de bases de datos (DBMS) independientemente del sistema operativo o lenguaje 
#de programación que utilicen, proporcionando así una capa intermedia entre ellas.
#Para crear el ODBC se deben seguir los siguientes pasos:
#Panel de Control -> Sistema y Seguridad -> Herramientas Administrativas -> OBDC Data Sources 64 Bit -> Agregar -> SQL
#Server -> Finalizar -> Nombre: Nombre del OBDC -> Servidor: Servidor al que nos queremos conectar -> Siguiente -> 
#Autentificacion de Windows -> Siguiente -> Establecer la siguiente base de datos como predeterminada: Base de datos a 
#la que nos queremos conectar -> Siguiente -> Finalizar -> Probar Origen de Datos -> Aceptar -> Aceptar.
#Después de haber realizado estos pasos, el nombre del ODBC se deberá añadir en el mydsn del URL de conexión. 
try:
    mssql_engine_windows = create_engine('mssql+pyodbc://@mydsn')
    connection5 = mssql_engine_windows.connect()
    print("5.- Microsoft SQL Server Connection successful with Windows authentication!!!\n")
    connection5.close()
except Exception as error:
    print("5.- Ups an Error ocurred while Opening the Microsoft SQL Server DataBase with Windows authentication:\n" + str(error) + "\n")
#6.- Microsoft SQL Server (SQL Server authentication): create_engine('mssql+pyodbc://username:password@mydsn')
#instalation: pip install pyodbc
#Este tipo de conexión es la misma a la descrita en el número 5, con la única diferencia que se incluye el nombre de 
#usuario y contraseña para la conexión en vez del puro ODBC, para ello se siguen los siguientes pasos:
#Panel de Control -> Sistema y Seguridad -> Herramientas Administrativas -> OBDC Data Sources 64 Bit -> Agregar -> SQL
#Server -> Finalizar -> Nombre: Nombre del OBDC -> Servidor: Servidor al que nos queremos conectar -> Siguiente -> 
#SQL Server Authentication -> Login: Nombre de usuario de la DB -> Password: Contraseña de la DB -> Siguiente -> 
#Establecer la siguiente base de datos como predeterminada: Base de datos a la que nos queremos conectar -> Siguiente -> 
#Finalizar -> Probar Origen de Datos -> Aceptar -> Aceptar.
#Después de haber realizado estos pasos, el nombre del ODBC se deberá añadir en el mydsn del URL de conexión y de igual 
#manera se podrán añadir el nombre de usuario y contraseña de forma opcional.
try:
    mssql_engine_sql_auth = create_engine('mssql+pyodbc://username:password@mydsn')
    connection6 = mssql_engine_sql_auth.connect()
    print("6.- Microsoft SQL Server Connection successful with Server authentication!!!\n")
    connection6.close()
except Exception as error:
    print("6.- Ups an Error ocurred while Opening the Microsoft SQL Server DataBase with Server authentication:\n" + str(error) + "\n")


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