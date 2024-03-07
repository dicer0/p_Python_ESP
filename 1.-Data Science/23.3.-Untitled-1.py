# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer, String, CHAR
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

#5.- Microsoft SQL Server (Windows authentication): create_engine('mssql+pyodbc://ServerName/DatabaseName?trusted_connection=yes')
#instalation: pip install pyodbc
try:
    mssql_engine_windows = create_engine('mssql+pyodbc://ServerName/DatabaseName?trusted_connection=yes')
    connection5 = mssql_engine_windows.connect()
    print("5.- Microsoft SQL Server Connection successful with Windows authentication!!!\n")
    connection5.close()
except Exception as error:
    print("5.- Ups an Error ocurred while Opening the Microsoft SQL Server DataBase with Windows authentication:\n" + str(error) + "\n")
#6.- Microsoft SQL Server (SQL Server authentication): create_engine('mssql+pyodbc://username:password@mydsn')
#instalation: pip install pyodbc
try:
    mssql_engine_sql_auth = create_engine('mssql+pyodbc://username:password@mydsn')
    connection6 = mssql_engine_sql_auth.connect()
    print("6.- Microsoft SQL Server Connection successful with Server authentication!!!\n")
    connection6.close()
except Exception as error:
    print("6.- Ups an Error ocurred while Opening the Microsoft SQL Server DataBase with Server authentication:\n" + str(error) + "\n")