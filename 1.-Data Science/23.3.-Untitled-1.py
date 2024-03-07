# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, text
from sqlalchemy import Column
from sqlalchemy import Integer, String, CHAR
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

try:
    mysql_engine = create_engine('mysql+pymysql://root:PincheTonto!123@localhost:3306/1_platziblog_db')
    connection1 = mysql_engine.connect()
    print("1.- MySQL Connection successful!!!\n")

    #Ejecutar una consulta SQL utilizando el método execute de la conexión
    query =  """SELECT    *
                FROM      usuarios AS u
                LEFT JOIN  posts as p ON u.id = p.usuarios_id
                WHERE     p.usuarios_id IS NULL;"""
    resultado = connection1.execute(text(query))  #Using connection1 instead of mysql_engine

    infoDB = []

    #Iterar sobre los resultados
    for row in resultado:
        infoDB.append(row)

    print(infoDB)

    #Cerrar la conexión
    resultado.close()
    connection1.close()
except Exception as error:
    print("1.- Ups an Error ocurred while Opening the MySQL DataBase:\n" + str(error) + "\n")