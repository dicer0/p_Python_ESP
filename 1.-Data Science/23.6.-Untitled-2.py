# -*- coding: utf-8 -*-

import pyodbc
import pandas
import traceback

class DatabaseExcelHandler:
    def __init__(self, db_connection_string):
        self.db_connection_string = db_connection_string
        self.connected = False
    def __connect_to_database(self):
        try:
            self.connection1 = pyodbc.connect(self.db_connection_string)
            self.cursor = self.connection1.cursor()
            print("1.- MySQL Connection successful!!!")
            self.connected = True
        except Exception as error:
            print("Error occurred while opening the MySQL database:\n" + str(error) + "\n") 

    def process_data_and_save_to_excel(self, pathExcel):
        self.__connect_to_database()
        if self.connected == False:
            return "No se pudo realizar la conexión con la base de datos."
        try:
            SQL_Query_string =  """SELECT 	  * 
                                    FROM 	    posts
                                    ORDER BY  titulo DESC;"""
            self.cursor.execute(SQL_Query_string)
            resultProxy = self.cursor.fetchall()
            print("Tipo de Dato ResultProxy: ", type(resultProxy))
            cursorRows = [tuple(row) for row in resultProxy]
            cursorCols = [col[0] for col in self.cursor.description] 
            dataFramePandas = pandas.DataFrame(data = cursorRows, columns = cursorCols)
            print(dataFramePandas, "\n")
            dataFramePandas['fecha_publicacion'] = pandas.to_datetime(dataFramePandas['fecha_publicacion']).dt.strftime('%d-%m-%Y')

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

            finalData = []
            for indDicc in compareDicc:
                filtered = dataFramePandas[(dataFramePandas['estatus'] == indDicc['estatusFilter']) &
                                        (dataFramePandas['usuarios_id'] == indDicc['userIdFilter']) &
                                        (dataFramePandas['categorias_id'] == indDicc['categoryIdFilter'])]
                if (not(filtered.empty)):
                    for (index, row) in (filtered.iterrows()):
                        standardContent = """Phasellus laoreet eros nec vestibulum varius. Nunc id efficitur lacus, non imperdiet quam. Aliquam porta, tellus at porta semper, felis velit congue mauris, eu pharetra felis sem vitae tortor. Curabitur bibendum vehicula dolor, nec accumsan tortor ultrices ac. Vivamus nec tristique orci. Nullam fringilla eros magna, vitae imperdiet nisl mattis et. Ut quis malesuada felis. Proin at dictum eros, eget sodales libero. Sed egestas tristique nisi et tempor. Ut cursus sapien eu pellentesque posuere. Etiam eleifend varius cursus.\n\nNullam viverra quam porta orci efficitur imperdiet. Quisque magna erat, dignissim nec velit sit amet, hendrerit mollis mauris. Mauris sapien magna, consectetur et vulputate a, iaculis eget nisi. Nunc est diam, aliquam quis turpis ac, porta mattis neque. Quisque consequat dolor sit amet velit commodo sagittis. Donec commodo pulvinar odio, ut gravida velit pellentesque vitae. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.\n\nMorbi vulputate ante quis elit pretium, ut blandit felis aliquet. Aenean a massa a leo tristique malesuada. Curabitur posuere, elit sed consectetur blandit, massa mauris tristique ante, in faucibus elit justo quis nisi. Ut viverra est et arcu egestas fringilla. Mauris condimentum, lorem id viverra placerat, libero lacus ultricies est, id volutpat metus sapien non justo. Nulla facilisis, sapien ut vehicula tristique, mauris lectus porta massa, sit amet malesuada dolor justo id lectus. Suspendisse sit amet tempor ligula. Nam sit amet nisl non magna lacinia finibus eget nec augue. Aliquam ornare cursus dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\nDonec ornare sem eget massa pharetra rhoncus. Donec tempor sapien at posuere porttitor. Morbi sodales efficitur felis eu scelerisque. Quisque ultrices nunc ut dignissim vehicula. Donec id imperdiet orci, sed porttitor turpis. Etiam volutpat elit sed justo lobortis, tincidunt imperdiet velit pretium. Ut convallis elit sapien, ac egestas ipsum finibus a. Morbi sed odio et dui tincidunt rhoncus tempor id turpis.\n\nProin fringilla consequat imperdiet. Ut accumsan velit ac augue sollicitudin porta. Phasellus finibus porttitor felis, a feugiat purus tempus vel. Etiam vitae vehicula ex. Praesent ut tellus tellus. Fusce felis nunc, congue ac leo in, elementum vulputate nisi. Duis diam nulla, consequat ac mauris quis, viverra gravida urna."""
                        contentStatus = "standard" if (standardContent in row["contenido"]) else "not conventional"
                        finalData.append({
                            "Titulo Static": indDicc["tituloStatic"],
                            "Content Status": contentStatus,
                            "Dato Static": indDicc["datoStatic"],
                            "Titulo": row["titulo"],
                            "Fecha de Publicacion": row["fecha_publicacion"]
                        })
                else:
                    finalData.append({
                        "Titulo Static": "Not categorized",
                        "Content Status": "Not categorized",
                        "Dato Static": "Not categorized",
                        "Titulo": row["titulo"],
                        "Fecha de Publicacion": row["fecha_publicacion"]
                    })
            finalDataFrame = pandas.DataFrame(data = finalData)

            staticDataAbove_1 = [
                ['Title A1.1', 'Title A1.2', 'Title A1.3'],
                ['Static Row 1', '', ''],
                ['Static Row 2', '', ''],
                ['Static Row 3', '', ''],
                ['Static Row 4', '', ''],
                ['Static Row 5', '', ''],
                ['Static Row 6', '', '']
            ]
            staticDataAbove_2 = [
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
            ]
            staticDataBelow_1 = [
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
            (filasDataFrame, columnasDataFrame) = finalDataFrame.shape
            staticDataAbove_1_Rows = len(staticDataAbove_1)
            staticDataAbove_2_Rows = len(staticDataAbove_2)
            staticDataBelow_1_Rows = len(staticDataBelow_1)
            staticDataAbove_1_Cols = len(staticDataAbove_1[0])
            staticDataAbove_2_Cols = len(staticDataAbove_2[0])
            staticDataBelow_1_Cols = len(staticDataBelow_1[0])

            with pandas.ExcelWriter(path = pathExcel, engine = 'xlsxwriter', mode = "w") as objetoExcel:
                staticDataAbove_1_DataFrame = pandas.DataFrame(staticDataAbove_1)
                staticDataAbove_1_DataFrame_textAligned = staticDataAbove_1_DataFrame.style.set_properties(**{'text-align': 'center', 'vertical-align': 'middle'})
                staticDataAbove_1_DataFrame_textAligned.to_excel(excel_writer = objetoExcel, index = False, startrow = 0, header = False)
                
                pandas.DataFrame(staticDataAbove_2).to_excel(excel_writer = objetoExcel, index = False, startrow = staticDataAbove_1_Rows + 1, header = False)

                finalDataFrame_textAligned = finalDataFrame.style.set_properties(**{'text-align': 'center', 'vertical-align': 'middle'})
                finalDataFrame_textAligned.to_excel(excel_writer = objetoExcel, index = False, index_label = None, sheet_name = 'Sheet1', startrow = staticDataAbove_1_Rows + staticDataAbove_2_Rows + 1 + 1, header = True)
                
                staticDataBelow_1_DataFrame = pandas.DataFrame(staticDataBelow_1)
                staticDataBelow_1_DataFrame_textAligned = staticDataBelow_1_DataFrame.style.set_properties(**{'text-align': 'center', 'vertical-align': 'middle'})
                staticDataBelow_1_DataFrame_textAligned.to_excel(excel_writer = objetoExcel, index = False, startrow = staticDataAbove_1_Rows + staticDataAbove_2_Rows + filasDataFrame + 2 + 1 + 1, header = False)
                
                workbook = objetoExcel.book
                worksheet = objetoExcel.sheets['Sheet1']
                worksheet.set_column('A:G', None, None, {'text_wrap': True, 'align': 'left', 'valign': 'vcenter'})

                #FORMATOS DE COLOR DE LA TABLA ESTÁTICA SUPERIOR 1:
                blueRowDataAbove1_format = workbook.add_format({
                    'bg_color': '#4f81bd',  #Color de celda azul claro.
                    'color': 'white',       #Letras blancas.
                    'bold': True,           #Letras negritas.
                    'align': 'center',      #Alineación en el centro.
                    'valign': 'vcenter'     #Alineación vertical en el centro.
                })                                                                          #Fila 1 azul, letras blancas y negritas y alineadas al centro.
                blueColDataAbove1_format = workbook.add_format({'bg_color': '#0070c0'})     #Col  2 azul.
                blueTableDataAbove1_format = workbook.add_format({
                    'bg_color': '#d3dfee',  #Color de celda azul muy claro.
                    'bold': True            #Letras negritas.
                })                                                                          #Demás celdas azules.
                #FORMATOS DE COLOR DE LA TABLA ESTÁTICA SUPERIOR 1:
                blueRowDataAbove1_format = workbook.add_format({
                    'bg_color': '#4f81bd',  #Color de celda azul claro.
                    'color': 'white',       #Letras blancas.
                    'bold': True            #Letras en negritas.
                })                                                                          #Fila 1 azul, letras blancas, negritas y alineadas al centro.
                blueColDataAbove1_format = workbook.add_format({'bg_color': '#0070c0'})     #Col  2 azul obscuro.
                blueTableDataAbove1_format = workbook.add_format({
                    'bg_color': '#d3dfee',  #Color de celda azul muy claro.
                    'bold': True            #Letras en negritas.
                })                                                                          #Demás celdas azules muy claro, letras negritas y alineadas al centro.
                #FORMATOS DE COLOR DE LA TABLA ESTÁTICA SUPERIOR 2:
                blueRowDataAbove2_format = workbook.add_format({
                    'bg_color': '#4f81bd',  #Color de celda azul obscuro.
                    'bold': True,           #Letras en negritas.
                    'underline': True       #Letras subrayadas.
                })                                                                          #Fila 1 azul obscuro y letras negritas.
                whiteRowDataAbove2_format = workbook.add_format({
                    'bg_color': 'white',    #Color de celda blanco.
                    'bold': True,           #Letras en negritas.
                    'underline': True       #Letras subrayadas.
                })                                                                          #Fila 2 blanca, con letras negritas y subrayadas.
                whiteTableDataAbove2_format = workbook.add_format({'bg_color': 'white'})    #Demás celdas blancas.
                #FORMATOS DE COLOR DE LA TABLA DINÁMICA:
                blueDB_format = workbook.add_format({'bg_color': 'blue'})                   #Fila 1 azul.
                greenDB_format = workbook.add_format({
                    'bg_color': 'green',    #Color de celda verde.
                    'bold': True            #Letras en negritas.
                })                                                                          #Col  1 verde.
                grayDB_format = workbook.add_format({'bg_color': 'gray'})                   #Col  2 gris.
                yellowDB_format = workbook.add_format({'bg_color': 'yellow'})               #Demás celdas amarillas.
                #FORMATOS DE COLOR DE LA TABLA ESTÁTICA INFERIOR 1:
                whiteRowDataBelow1_format = workbook.add_format({
                    'bg_color': 'white',    #Color de celda blanco.
                    'bold': True,           #Letras en negritas.
                    'underline': True       #Letras subrayadas.
                })                                                                          #Fila 1 blanca.
                darkBlueRowDataBelow1_format = workbook.add_format({
                    'bg_color': '#4f81bd',  #Color de celda azul obscuro.
                    'bold': True            #Letras en negritas.
                })                                                                          #Fila 2 azul.
                lightBlueRowDataBelow1_format = workbook.add_format({
                    'bg_color': '#A7BFDE',  #Color de celda azul claro.
                    'bold': True            #Letras en negritas.
                })                                                                          #Fila 3 azul claro.
                greenColDataBelow1_format = workbook.add_format({
                    'bg_color': '#5EC268',  #Color de celda verde.
                    'bold': True            #Letras en negritas.
                })                                                                          #Col  1 verde.
                grayColDataBelow1_format = workbook.add_format({'bg_color': 'gray'})        #Col  2 gris.
                yellowColDataBelow1_format = workbook.add_format({'bg_color': '#FFF2CC'})   #Demás celdas amarillas.
                #FORMATO DE COLOR PARA LOS SEPARADORES DE DATOS:
                dataSeparation_format = workbook.add_format({'bg_color': 'white'})
                #worksheet.conditional_format(first_row, first_col, last_row, last_col, {'type': 'condition', 'format': formato})
                worksheet.conditional_format(0, 0, 0, (staticDataAbove_1_Cols - 1), {'type': 'no_blanks', 'format': blueRowDataAbove1_format})
                worksheet.conditional_format(0, 0, 0, (staticDataAbove_1_Cols - 1), {'type': 'blanks', 'format': blueRowDataAbove1_format})
                worksheet.conditional_format(1, 0, staticDataAbove_1_Rows, 0, {'type': 'no_blanks', 'format': blueTableDataAbove1_format})
                #COLOR DEL SEPARADOR DE DATOS: Este se debe poner siempre antes del color de las columnas, considerar el tamaño de los conjuntos de 
                #datos y anteriores las filas de separación.
                worksheet.conditional_format(staticDataAbove_1_Rows, 0, staticDataAbove_1_Rows, (staticDataAbove_2_Cols - 1), {'type': 'blanks', 'format': dataSeparation_format})
                #COLOR DE LAS COLUMNAS:
                worksheet.conditional_format(1, 1, staticDataAbove_1_Rows, 1, {'type': 'no_blanks', 'format': blueColDataAbove1_format})
                worksheet.conditional_format(1, 1, staticDataAbove_1_Rows, 1, {'type': 'blanks',    'format': blueColDataAbove1_format})
                worksheet.conditional_format(1, 2, staticDataAbove_1_Rows, 2, {'type': 'no_blanks', 'format': blueTableDataAbove1_format})
                worksheet.conditional_format(1, 2, staticDataAbove_1_Rows, 2, {'type': 'blanks',    'format': blueTableDataAbove1_format})

                rowPositionStaticDataAbove2 = (staticDataAbove_1_Rows + 1) + 1
                for i in range(rowPositionStaticDataAbove2, rowPositionStaticDataAbove2 + staticDataAbove_2_Rows): #Position  A10:G10 - A19:G19
                    ExcelCellsStaticDataAbove2 = "A" + str(i) + ":G" + str(i)
                    worksheet.merge_range(ExcelCellsStaticDataAbove2, data = None)
                    if (i == 9):                                                        #Posición  A9:G9
                        worksheet.conditional_format((i - 1), 0, (i - 1), (staticDataAbove_2_Cols - 1), {'type': 'no_blanks', 'format': blueRowDataAbove2_format})
                    elif (i == 10 or i == 13 or i == 16):                               #Posición  A10:G10 - A19:G19
                        worksheet.conditional_format((i - 1), 0, (i - 1), (staticDataAbove_2_Cols - 1), {'type': 'no_blanks', 'format': whiteRowDataAbove2_format})
                    else:                                                               #Posición  Las demás celdas de la tabla.
                        worksheet.conditional_format((i - 1), 0, (i - 1), (staticDataAbove_2_Cols - 1), {'type': 'no_blanks', 'format': whiteTableDataAbove2_format})
                #COLOR DEL SEPARADOR DE DATOS: Este se debe poner siempre antes del color de las columnas, considerar el tamaño de los conjuntos de 
                #datos y anteriores las filas de separación.
                worksheet.conditional_format((staticDataAbove_1_Rows + 1 + staticDataAbove_2_Rows), 0, (staticDataAbove_1_Rows + 1 + staticDataAbove_2_Rows), (staticDataAbove_2_Cols - 1), {'type': 'blanks', 'format': dataSeparation_format})
                
                worksheet.conditional_format((staticDataAbove_1_Rows + staticDataAbove_2_Rows + 1 + 1), 0, (staticDataAbove_1_Rows + staticDataAbove_2_Rows + 1 + 1), (columnasDataFrame - 1), {'type': 'no_blanks', 'format': blueDB_format})
                #COLOR DEL SEPARADOR DE DATOS: Este se debe poner siempre antes del color de las columnas, considerar el tamaño de los conjuntos de 
                #datos y anteriores las filas de separación.
                worksheet.conditional_format((staticDataAbove_1_Rows + 1 + staticDataAbove_2_Rows + 1 + filasDataFrame + 1), 0, (staticDataAbove_1_Rows + 1 + staticDataAbove_2_Rows + 1 + filasDataFrame + 1), (staticDataAbove_2_Cols - 1), {'type': 'blanks', 'format': dataSeparation_format})
                worksheet.conditional_format(((staticDataAbove_1_Rows + staticDataAbove_2_Rows + 1 + 1) + 1), 0, filasDataFrame + ((staticDataAbove_1_Rows + staticDataAbove_2_Rows + 1 + 1) + 1), 0, {'type': 'no_blanks', 'format': greenDB_format})
                worksheet.conditional_format(((staticDataAbove_1_Rows + staticDataAbove_2_Rows + 1 + 1) + 1), 0, filasDataFrame + ((staticDataAbove_1_Rows + staticDataAbove_2_Rows + 1 + 1) + 1), 0, {'type': 'blanks',    'format': greenDB_format})
                worksheet.conditional_format(((staticDataAbove_1_Rows + staticDataAbove_2_Rows + 1 + 1) + 1), 1, filasDataFrame + ((staticDataAbove_1_Rows + staticDataAbove_2_Rows + 1 + 1) + 1), 1, {'type': 'no_blanks', 'format': grayDB_format})
                worksheet.conditional_format(((staticDataAbove_1_Rows + staticDataAbove_2_Rows + 1 + 1) + 1), 1, filasDataFrame + ((staticDataAbove_1_Rows + staticDataAbove_2_Rows + 1 + 1) + 1), 1, {'type': 'blanks',    'format': grayDB_format})
                for col in range(2, columnasDataFrame):
                    worksheet.conditional_format(((staticDataAbove_1_Rows + staticDataAbove_2_Rows + 1 + 1) + 1), col, filasDataFrame + ((staticDataAbove_1_Rows + staticDataAbove_2_Rows + 1 + 1) + 1), col, {'type': 'no_blanks', 'format': yellowDB_format})
                    worksheet.conditional_format(((staticDataAbove_1_Rows + staticDataAbove_2_Rows + 1 + 1) + 1), col, filasDataFrame + ((staticDataAbove_1_Rows + staticDataAbove_2_Rows + 1 + 1) + 1), col, {'type': 'blanks',    'format': yellowDB_format})
                
                #worksheet.conditional_format(first_row, first_col, last_row, last_col, {'type': 'condition', 'format': formato})
                #Variable para fusión de celdas: Para ello se considera las filas de los conjuntos anteriores y sus separaciones.
                rowPositionStaticDataBelow1 = (staticDataAbove_1_Rows + 1 + staticDataAbove_2_Rows + 1 + filasDataFrame + 1 + 1) + 1
                for i in range(rowPositionStaticDataBelow1, rowPositionStaticDataBelow1 + staticDataBelow_1_Rows): #Position  A29:G29 - A40:G40
                    if (i == 29):                                                       #Posición  A29:G29
                        #Creación de coordenadas: El método .merge_range() pide las coordenadas en formato de Excel.
                        ExcelCellsStaticDataBelow1 = "A" + str(i) + ":G" + str(i)
                        worksheet.merge_range(ExcelCellsStaticDataBelow1, data = None)
                        #pandas.ExcelWriter().sheets["nombreSheet"].conditional_format(fila_inicial, col_inicial, fila_final, col_final, {type})
                        worksheet.conditional_format((i - 1), 0, (i - 1), (staticDataAbove_2_Cols - 1), {'type': 'no_blanks', 'format': whiteRowDataBelow1_format})
                    elif (i == 30):                                                     #Posición  A30:G30
                        worksheet.conditional_format((i - 1), 0, (i - 1), (staticDataAbove_2_Cols - 1), {'type': 'no_blanks', 'format': darkBlueRowDataBelow1_format})
                    elif (i == 31 or i == 39):                                          #Posición  A31:G31 o A39:G39
                        ExcelCellsStaticDataBelow1 = "A" + str(i) + ":G" + str(i)
                        worksheet.merge_range(ExcelCellsStaticDataBelow1, data = None)
                        worksheet.conditional_format((i - 1), 0, (i - 1), (staticDataAbove_2_Cols - 1), {'type': 'no_blanks', 'format': lightBlueRowDataBelow1_format})
                    else:                                                               #Posición  Las demás celdas de la tabla.
                        worksheet.conditional_format((i - 1), 0, (i - 1), (staticDataAbove_2_Cols - 1), {'type': 'no_blanks', 'format': whiteTableDataAbove2_format})
                #Formato de Columnas de la tabla.
                worksheet.conditional_format((staticDataAbove_1_Rows + 1 + staticDataAbove_2_Rows + 1 + filasDataFrame + 1), 0, (staticDataAbove_1_Rows + 1 + staticDataAbove_2_Rows + 1 + filasDataFrame + 1 + staticDataBelow_1_Rows), 0, {'type': 'no_blanks',   'format': greenColDataBelow1_format})
                worksheet.conditional_format((staticDataAbove_1_Rows + 1 + staticDataAbove_2_Rows + 1 + filasDataFrame + 1), 0, (staticDataAbove_1_Rows + 1 + staticDataAbove_2_Rows + 1 + filasDataFrame + 1 + staticDataBelow_1_Rows), 0, {'type': 'blanks',      'format': greenColDataBelow1_format})
                worksheet.conditional_format((staticDataAbove_1_Rows + 1 + staticDataAbove_2_Rows + 1 + filasDataFrame + 1), 1, (staticDataAbove_1_Rows + 1 + staticDataAbove_2_Rows + 1 + filasDataFrame + 1 + staticDataBelow_1_Rows), 1, {'type': 'no_blanks',   'format': grayColDataBelow1_format})
                worksheet.conditional_format((staticDataAbove_1_Rows + 1 + staticDataAbove_2_Rows + 1 + filasDataFrame + 1), 1, (staticDataAbove_1_Rows + 1 + staticDataAbove_2_Rows + 1 + filasDataFrame + 1 + staticDataBelow_1_Rows), 1, {'type': 'blanks',      'format': grayColDataBelow1_format})
                for col in range(2, staticDataBelow_1_Cols):
                    worksheet.conditional_format((staticDataAbove_1_Rows + 1 + staticDataAbove_2_Rows + 1 + filasDataFrame + 1), col, (staticDataAbove_1_Rows + 1 + staticDataAbove_2_Rows + 1 + filasDataFrame + 1 + staticDataBelow_1_Rows), col, {'type': 'no_blanks',   'format': yellowColDataBelow1_format})
                    worksheet.conditional_format((staticDataAbove_1_Rows + 1 + staticDataAbove_2_Rows + 1 + filasDataFrame + 1), col, (staticDataAbove_1_Rows + 1 + staticDataAbove_2_Rows + 1 + filasDataFrame + 1 + staticDataBelow_1_Rows), col, {'type': 'blanks',      'format': yellowColDataBelow1_format})
                #COLOR DEL SEPARADOR DE DATOS: Este se debe poner siempre antes del color de las columnas, considerar el tamaño de los conjuntos de 
                #datos y anteriores las filas de separación.
                worksheet.conditional_format((staticDataAbove_1_Rows + 1 + staticDataAbove_2_Rows + 1 + filasDataFrame + 1 + staticDataBelow_1_Rows + 1), 0, (staticDataAbove_1_Rows + 1 + staticDataAbove_2_Rows + 1 + filasDataFrame + 1), (staticDataAbove_2_Cols - 1), {'type': 'blanks', 'format': dataSeparation_format})

                max_lengths = [len(str(col)) for col in finalDataFrame.columns]
                for index, row in finalDataFrame.iterrows():
                    for i, value in enumerate(row):
                        max_lengths[i] = max(max_lengths[i], len(str(value)))
                for i, max_length in enumerate(max_lengths):
                    worksheet.set_column(i, i, max_length + 1)
            
            return finalDataFrame
        except Exception as error:
            print("1.- Ups an Error ocurred while Opening the MySQL DataBase:\n" + str(error) + "\n")
            print("La línea donde ocurrió el error fue: ", traceback.format_exc())
            return "Error al procesar los datos y guardarlos en un Excel."
        finally:
            if self.connection1:
                self.connection1.close()
                print("MySQL Connection closed.")

if __name__ == "__main__":
    connectionString = 'DRIVER={MySQL ODBC 8.3 Unicode Driver};SERVER=localhost;PORT=3306;DATABASE=1_platziblog_db;USER=root;PASSWORD=PincheTonto!123;'
    db_handler1 = DatabaseExcelHandler(connectionString)
    excelFilePath2 = "C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/1.-Data Science/0.-Archivos_Ejercicios_Python/23.-GUI PyQt5 Conexion DataBase/23.-Reporte Analisis de Datos 2.xlsx"
    db_handler1.process_data_and_save_to_excel(excelFilePath2)