from sqlalchemy import create_engine, text
import pandas as pd
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QColor

finalData = []
compareDicc = [{
    "tituloStatic": "Grupo de Datos 1",
    "datoStatic": "Dato grupo 1",
    "estatusFilter": "activo",
    "userIdFilter": 1,
    "categoryIdFilter": 2
},
{
    "tituloStatic": "Grupo de Datos 2",
    "datoStatic": "Dato grupo 2",
    "estatusFilter": "inactivo",
    "userIdFilter": 2,
    "categoryIdFilter": 3
}]

try:
    mysql_engine = create_engine('mysql+pymysql://root:PincheTonto!123@localhost:3306/1_platziblog_db')
    connection1 = mysql_engine.connect()
    print("1.- MySQL Connection successful!!!\n")

    SQL_Query_string = """SELECT * FROM posts ORDER BY titulo DESC;"""
    SQL_TextObject = text(SQL_Query_string)
    resultProxy = connection1.execute(SQL_TextObject)
    print("Tipo de Dato ResultProxy: ", type(resultProxy))
    dataFramePandas = pd.DataFrame(data=resultProxy, columns=resultProxy.keys())
    print(dataFramePandas, "\n")

    for indDicc in compareDicc:
        filtered_rows = []
        for (index, row) in dataFramePandas.iterrows():
            if (row['estatus'] == indDicc['estatusFilter'] and
                row['usuarios_id'] == indDicc['userIdFilter'] and
                row['categorias_id'] == indDicc['categoryIdFilter']):
                filtered_rows.append(row)

        for filtered_dataBase in filtered_rows:
            finalData.append({
                "tituloStatic": indDicc["tituloStatic"],
                "datoStatic": indDicc["datoStatic"],
                "titulo": filtered_dataBase["titulo"],
                "fecha_publicacion": filtered_dataBase["fecha_publicacion"]
            })
    finalDataFrame = pd.DataFrame(data=finalData)
    print(finalDataFrame, "\n")
    finalDataFrame.to_excel('resultado.xlsx', index=False)

    app = QApplication(sys.argv)
    window = QMainWindow()
    tableWidget = QTableWidget()
    tableWidget.setRowCount(finalDataFrame.shape[0])
    tableWidget.setColumnCount(finalDataFrame.shape[1])

    for i in range(finalDataFrame.shape[0]):
        for j in range(finalDataFrame.shape[1]):
            item = QTableWidgetItem(str(finalDataFrame.iloc[i, j]))
            if i == 0:
                item.setBackground(QColor('blue'))
            elif j == 0 and i != 0:
                item.setBackground(QColor('green'))
            elif j == 1 and i != 0:
                item.setBackground(QColor('gray'))
            elif i == 0 and j == 1:
                item.setBackground(QColor('blue'))
            elif i == 0 and j != 0:
                item.setBackground(QColor('blue'))
            elif i != 0 and j == 0:
                item.setBackground(QColor('green'))
            else:
                item.setBackground(QColor('yellow'))
            tableWidget.setItem(i, j, item)

    window.setCentralWidget(tableWidget)
    window.show()
    sys.exit(app.exec_())

except Exception as error:
    print("1.- Ups an Error ocurred while Opening the MySQL DataBase:\n" + str(error) + "\n")

finally:
    if 'resultProxy' in locals():
        resultProxy.close()
    if 'connection1' in locals():
        connection1.close()