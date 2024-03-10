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
            standardContent = """Phasellus laoreet eros nec vestibulum varius. Nunc id efficitur lacus, non imperdiet quam. Aliquam porta, tellus at porta semper, felis velit congue mauris, eu pharetra felis sem vitae tortor. Curabitur bibendum vehicula dolor, nec accumsan tortor ultrices ac. Vivamus nec tristique orci. Nullam fringilla eros magna, vitae imperdiet nisl mattis et. Ut quis malesuada felis. Proin at dictum eros, eget sodales libero. Sed egestas tristique nisi et tempor. Ut cursus sapien eu pellentesque posuere. Etiam eleifend varius cursus.\n\nNullam viverra quam porta orci efficitur imperdiet. Quisque magna erat, dignissim nec velit sit amet, hendrerit mollis mauris. Mauris sapien magna, consectetur et vulputate a, iaculis eget nisi. Nunc est diam, aliquam quis turpis ac, porta mattis neque. Quisque consequat dolor sit amet velit commodo sagittis. Donec commodo pulvinar odio, ut gravida velit pellentesque vitae. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.\n\nMorbi vulputate ante quis elit pretium, ut blandit felis aliquet. Aenean a massa a leo tristique malesuada. Curabitur posuere, elit sed consectetur blandit, massa mauris tristique ante, in faucibus elit justo quis nisi. Ut viverra est et arcu egestas fringilla. Mauris condimentum, lorem id viverra placerat, libero lacus ultricies est, id volutpat metus sapien non justo. Nulla facilisis, sapien ut vehicula tristique, mauris lectus porta massa, sit amet malesuada dolor justo id lectus. Suspendisse sit amet tempor ligula. Nam sit amet nisl non magna lacinia finibus eget nec augue. Aliquam ornare cursus dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\nDonec ornare sem eget massa pharetra rhoncus. Donec tempor sapien at posuere porttitor. Morbi sodales efficitur felis eu scelerisque. Quisque ultrices nunc ut dignissim vehicula. Donec id imperdiet orci, sed porttitor turpis. Etiam volutpat elit sed justo lobortis, tincidunt imperdiet velit pretium. Ut convallis elit sapien, ac egestas ipsum finibus a. Morbi sed odio et dui tincidunt rhoncus tempor id turpis.\n\nProin fringilla consequat imperdiet. Ut accumsan velit ac augue sollicitudin porta. Phasellus finibus porttitor felis, a feugiat purus tempus vel. Etiam vitae vehicula ex. Praesent ut tellus tellus. Fusce felis nunc, congue ac leo in, elementum vulputate nisi. Duis diam nulla, consequat ac mauris quis, viverra gravida urna."""
            contentStatus = "standard" if (standardContent in filtered_dataBase["contenido"]) else "not conventional"
            finalData.append({
                "tituloStatic": indDicc["tituloStatic"],
                "contentStatus": contentStatus,
                "datoStatic": indDicc["datoStatic"],
                "titulo": filtered_dataBase["titulo"],
                "fecha_publicacion": filtered_dataBase["fecha_publicacion"]
            })
    finalDataFrame = pd.DataFrame(data=finalData)
    print(finalDataFrame, "\n")

    excel_writer = pd.ExcelWriter('resultado.xlsx', engine='xlsxwriter')
    finalDataFrame.to_excel(excel_writer, index=False, sheet_name='Sheet1', startrow=1)
    workbook = excel_writer.book
    worksheet = excel_writer.sheets['Sheet1']
    for j, col in enumerate(finalDataFrame.columns):
        worksheet.write(0, j, col, workbook.add_format({'bg_color': 'blue', 'bold': True}))
    for i in range(finalDataFrame.shape[0] + 1):
        for j in range(finalDataFrame.shape[1]):
            cell_format = workbook.add_format()
            if j == 0:
                cell_format.set_bg_color('green')
            elif j == 1:
                cell_format.set_bg_color('gray')
            elif i == finalDataFrame.shape[0]:
                cell_format.set_bg_color('yellow')
            else:
                cell_format.set_bg_color('yellow')
            worksheet.write(i + 1, j, finalDataFrame.iloc[i - 1, j], cell_format)
    date_format = workbook.add_format({'num_format': 'yyyy-mm-dd', 'bg_color': 'yellow'})
    for i in range(finalDataFrame.shape[0]):
        worksheet.write(i + 1, finalDataFrame.columns.get_loc('fecha_publicacion'), pd.to_datetime(finalDataFrame.iloc[i]['fecha_publicacion']).date(), date_format)
    for idx, col in enumerate(finalDataFrame):
        max_len = max(finalDataFrame[col].astype(str).map(len).max(), len(str(col))) + 1
        worksheet.set_column(idx, idx, max_len)
    excel_writer.save()

    app = QApplication(sys.argv)
    window = QMainWindow()
    tableWidget = QTableWidget()
    tableWidget.setRowCount(finalDataFrame.shape[0] + 1)  # +1 para incluir la fila de nombres de columna
    tableWidget.setColumnCount(finalDataFrame.shape[1])
    for j in range(finalDataFrame.shape[1]):
        item = QTableWidgetItem(finalDataFrame.columns[j])
        item.setBackground(QColor('blue'))
        tableWidget.setItem(0, j, item)

    for i in range(finalDataFrame.shape[0]):
        for j in range(finalDataFrame.shape[1]):
            item = QTableWidgetItem(str(finalDataFrame.iloc[i, j]))
            if j == 0:
                item.setBackground(QColor('green'))
            elif j == 1:
                item.setBackground(QColor('gray'))
            else:
                item.setBackground(QColor('yellow'))
            tableWidget.setItem(i + 1, j, item)  # +1 para evitar la superposición con la fila de nombres de columna

    window.setCentralWidget(tableWidget)
    window.showMaximized()
    sys.exit(app.exec_())
except Exception as error:
    print("1.- Ups an Error ocurred while Opening the MySQL DataBase:\n" + str(error) + "\n")
finally:
    if ('resultProxy' in locals()):
        resultProxy.close()
    if ('connection1' in locals()):
        connection1.close()