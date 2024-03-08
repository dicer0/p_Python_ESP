# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, text
import pandas

compareDicc = [{
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

finalDicc = []
try:
    mysql_engine = create_engine('mysql+pymysql://root:PincheTonto!123@localhost:3306/1_platziblog_db')
    connection1 = mysql_engine.connect()
    print("1.- MySQL Connection successful!!!\n")

    query =  """SELECT 	  *
                FROM 	    posts
                ORDER BY  titulo DESC;"""
    resultado = connection1.execute(text(query))
    dataFramePandas = pandas.DataFrame(data = resultado, columns = resultado.keys())
    print(dataFramePandas)

    resultado.close()
    connection1.close()
except Exception as error:
    print("1.- Ups an Error ocurred while Opening the MySQL DataBase:\n" + str(error) + "\n")