# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy import text
import pandas
import traceback
class DatabaseExcelHandler:
    def __init__(self, db_url):
        self.db_url = db_url
        self.connected = False
    def __connect_to_database(self):
        try:
            self.mysql_engine = create_engine(self.db_url)
            self.connection1 = self.mysql_engine.connect()
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
            SQL_TextObject = text(SQL_Query_string)
            resultProxy = self.connection1.execute(SQL_TextObject)
            print("Tipo de Dato ResultProxy: ", type(resultProxy))
            dataFramePandas = pandas.DataFrame(data = resultProxy, columns = resultProxy.keys())    
            print(dataFramePandas, "\n")
            dataFramePandas['fecha_publicacion'] = pandas.to_datetime(dataFramePandas['fecha_publicacion']).dt.strftime('%d-%m-%Y')
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
            for indDicc in compareDicc:
                filtered_rows = []
                for (index, row) in (dataFramePandas.iterrows()):
                    if (row['estatus'] == indDicc['estatusFilter'] and
                        row['usuarios_id'] == indDicc['userIdFilter'] and
                        row['categorias_id'] == indDicc['categoryIdFilter']):
                        filtered_rows.append(row)
                for filtered_dataBase in filtered_rows:
                    standardContent = """Phasellus laoreet eros nec vestibulum varius. Nunc id efficitur lacus, non imperdiet quam. Aliquam porta, tellus at porta semper, felis velit congue mauris, eu pharetra felis sem vitae tortor. Curabitur bibendum vehicula dolor, nec accumsan tortor ultrices ac. Vivamus nec tristique orci. Nullam fringilla eros magna, vitae imperdiet nisl mattis et. Ut quis malesuada felis. Proin at dictum eros, eget sodales libero. Sed egestas tristique nisi et tempor. Ut cursus sapien eu pellentesque posuere. Etiam eleifend varius cursus.\n\nNullam viverra quam porta orci efficitur imperdiet. Quisque magna erat, dignissim nec velit sit amet, hendrerit mollis mauris. Mauris sapien magna, consectetur et vulputate a, iaculis eget nisi. Nunc est diam, aliquam quis turpis ac, porta mattis neque. Quisque consequat dolor sit amet velit commodo sagittis. Donec commodo pulvinar odio, ut gravida velit pellentesque vitae. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.\n\nMorbi vulputate ante quis elit pretium, ut blandit felis aliquet. Aenean a massa a leo tristique malesuada. Curabitur posuere, elit sed consectetur blandit, massa mauris tristique ante, in faucibus elit justo quis nisi. Ut viverra est et arcu egestas fringilla. Mauris condimentum, lorem id viverra placerat, libero lacus ultricies est, id volutpat metus sapien non justo. Nulla facilisis, sapien ut vehicula tristique, mauris lectus porta massa, sit amet malesuada dolor justo id lectus. Suspendisse sit amet tempor ligula. Nam sit amet nisl non magna lacinia finibus eget nec augue. Aliquam ornare cursus dapibus. Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\nDonec ornare sem eget massa pharetra rhoncus. Donec tempor sapien at posuere porttitor. Morbi sodales efficitur felis eu scelerisque. Quisque ultrices nunc ut dignissim vehicula. Donec id imperdiet orci, sed porttitor turpis. Etiam volutpat elit sed justo lobortis, tincidunt imperdiet velit pretium. Ut convallis elit sapien, ac egestas ipsum finibus a. Morbi sed odio et dui tincidunt rhoncus tempor id turpis.\n\nProin fringilla consequat imperdiet. Ut accumsan velit ac augue sollicitudin porta. Phasellus finibus porttitor felis, a feugiat purus tempus vel. Etiam vitae vehicula ex. Praesent ut tellus tellus. Fusce felis nunc, congue ac leo in, elementum vulputate nisi. Duis diam nulla, consequat ac mauris quis, viverra gravida urna."""
                    contentStatus = "standard" if (standardContent in filtered_dataBase["contenido"]) else "not conventional"
                    finalData.append({
                        "Titulo Static": indDicc["tituloStatic"],
                        "Content Status": contentStatus,
                        "Dato Static": indDicc["datoStatic"],
                        "Titulo": filtered_dataBase["titulo"],
                        "Fecha de Publicacion": filtered_dataBase["fecha_publicacion"]
                    })
            finalDataFrame = pandas.DataFrame(data = finalData)
            with pandas.ExcelWriter(path = pathExcel, engine = 'xlsxwriter', mode = "w") as objetoExcel:
                finalDataFrame.to_excel(excel_writer = objetoExcel, index = False, index_label = None, sheet_name = 'Sheet1', startrow = 0, startcol = 0, header = True, engine = 'xlsxwriter')
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
        except Exception as error:
            print("1.- Ups an Error ocurred while Opening the MySQL DataBase:\n" + str(error) + "\n")
            print("La línea donde ocurrió el error fue: ", traceback.format_exc())
            return "Error al procesar los datos y guardar en Excel."
        finally:
            if self.connection1:
                self.connection1.close()
                print("MySQL Connection closed.")
                return finalDataFrame