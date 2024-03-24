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
            dataFramePandas = pandas.DataFrame(data = cursorRows, columns = [column[0] for column in self.cursor.description])
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
                if not filtered.empty:
                    for index, row in filtered.iterrows():
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
            
            # staticDataAbove_1
            static_data_above_1 = [
                ['Title A1.1', 'Title A1.2', 'Title A1.3'],
                ['Static Row 1', '', '', '', '', '', ''],
                ['Static Row 2', '', '', '', '', '', ''],
                ['Static Row 3', '', '', '', '', '', ''],
                ['Static Row 4', '', '', '', '', '', ''],
                ['Static Row 5', '', '', '', '', '', ''],
                ['Static Row 6', '', '', '', '', '', '']
            ]
            
            # staticDataAbove_2
            static_data_above_2 = [
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

            # staticDataBelow_1
            static_data_below_1 = [
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
            
            with pandas.ExcelWriter(path = pathExcel, engine = 'xlsxwriter', mode = "w") as objetoExcel:
                # Escribir staticDataAbove_1
                pandas.DataFrame(static_data_above_1).to_excel(excel_writer=objetoExcel, index=False, header=False)
                
                # Escribir finalDataFrame
                finalDataFrame.to_excel(excel_writer=objetoExcel, index=False, startrow=len(static_data_above_1) + 1)
                
                # Escribir staticDataAbove_2
                pandas.DataFrame(static_data_above_2).to_excel(excel_writer=objetoExcel, index=False, startrow=len(static_data_above_1) + len(finalDataFrame) + 3, header=False)
                
                # Escribir staticDataBelow_1
                pandas.DataFrame(static_data_below_1).to_excel(excel_writer=objetoExcel, index=False, startrow=len(static_data_above_1) + len(finalDataFrame) + len(static_data_above_2) + 5, header=False)

                workbook = objetoExcel.book
                worksheet = objetoExcel.sheets['Sheet1']
                blue_format = workbook.add_format({'bg_color': '#0000FF'})
                green_format = workbook.add_format({'bg_color': '#00FF00'})
                grey_format = workbook.add_format({'bg_color': '#D3D3D3'})
                yellow_format = workbook.add_format({'bg_color': '#FFFF00'})
                (filasDataFrame, columnasDataFrame) = finalDataFrame.shape
                worksheet.conditional_format(0, 0, 0, columnasDataFrame - 1, {'type': 'no_blanks', 'format': blue_format})
                worksheet.conditional_format(1, 0, filasDataFrame, 0, {'type': 'no_blanks', 'format': green_format})
                worksheet.conditional_format(1, 1, filasDataFrame, 1, {'type': 'no_blanks', 'format': grey_format})
                for col in range(2, columnasDataFrame):
                    worksheet.conditional_format(1, col, filasDataFrame, col, {'type': 'no_blanks', 'format': yellow_format})
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