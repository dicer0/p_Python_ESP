# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, text
import pandas

compareDicc = [{
    "tituloStatic": "Titulo 1",     #Datos que así se pasan al diccionario final.
    "datoStatic": "Dato 1",         
    "estatusStatic": "activo"       #Datos de filtrado.
},
{
    "tituloStatic": "Titulo 2",     #Datos que así se pasan al diccionario final.
    "datoStatic": "Dato 2",         
    "estatusStatic": "activo"       #Datos de filtrado.
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
    print("Oliwis", type(resultado))
    # Convertir los resultados a un DataFrame de Pandas
    dataFramePandas = pandas.DataFrame(data = resultado, columns = resultado.keys())
    # Mostrar el DataFrame como tabla
    print(dataFramePandas)

    resultado.close()
    connection1.close()
except Exception as error:
    print("1.- Ups an Error ocurred while Opening the MySQL DataBase:\n" + str(error) + "\n")