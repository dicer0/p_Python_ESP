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

finalData = []
try:
    mysql_engine = create_engine('mysql+pymysql://root:PincheTonto!123@localhost:3306/1_platziblog_db')
    connection1 = mysql_engine.connect()
    print("1.- MySQL Connection successful!!!\n")

    SQL_Query_string =  """SELECT 	  * 
                            FROM 	    posts
                            ORDER BY  titulo DESC;"""
    SQL_TextObject = text(SQL_Query_string)
    resultProxy = connection1.execute(SQL_TextObject)
    dataFramePandas = pandas.DataFrame(data = resultProxy, columns = resultProxy.keys())
    print(dataFramePandas, "\n")

    for filter_item in compareDicc:
        filtered_rows = []
        for index, row in dataFramePandas.iterrows():
            if (row['estatus'] == filter_item['estatusFilter'] and
                row['usuarios_id'] == filter_item['userIdFilter'] and
                row['categorias_id'] == filter_item['categoryIdFilter']):
                filtered_rows.append(row)

        for row in filtered_rows:
            finalData.append({
                "tituloStatic": filter_item["tituloStatic"],
                "datoStatic": filter_item["datoStatic"],
                "titulo": row["titulo"],
                "fecha_publicacion": row["fecha_publicacion"]
            })

    resultProxy.close()
    connection1.close()
    finalDataFrame = pandas.DataFrame(finalData)
    print(finalDataFrame, "\n")
except Exception as error:
    print("1.- Ups an Error ocurred while Opening the MySQL DataBase:\n" + str(error) + "\n")