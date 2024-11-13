# -*- coding: utf-8 -*-

#En Python se introducen comentarios de una sola linea con el simbolo #.
#La primera línea de código incluida en este programa se conoce como declaración de codificación o codificación 
#de caracteres. Al especificar utf-8 (caracteres Unicode) como la codificación, nos aseguramos de que el archivo 
#pueda contener caracteres especiales, letras acentuadas y otros caracteres no ASCII sin problemas, garantizando 
#que Python interprete correctamente esos caracteres y evite posibles errores de codificación.
#Se puede detener una ejecución con el comando [CTRL] + C puesto en consola, con el comando "cls" se borra su 
#historial y en Visual Studio Code con el botón superior derecho de Play se corre el programa.
#Para comentar en Visual Studio Code varias líneas de código se debe pulsar:
#[CTRL] + K (VSCode queda a la espera). Después pulsa [CTRL] + C para comentar y [CTRL] + U para descomentar.

import wx #wxPython: Librería para crear interfaces de usuario GUI (Graphycal User Interface)

#GUI (Graphical User Interface): Es una ventana con elementos como botones, áreas de texto, desplegables, 
#imágenes, etc. que sirven para realizar alguna acción de forma gráfica para el usuario. A continuación, veremos 
#como se crean este tipo de elementos en Python utilizando la librería wxPython.

#GUI CREADO CON PROGRAMACIÓN ORIENTADA A OBJETOS Y LA LIBRERÍA WX PYTHON QUE INCLUYE UN PANEL (CONTENEDOR DE 
#ELEMENTOS) CON UN BOTÓN PARA CARGAR UNA IMÁGEN DEL EXPLORADOR DE ARCHIVOS Y MUESTRE SU RUTA EN UNA CAJA DE 
#TEXTO: Vamos a agregar un panel, que es un contenedor donde se pueden incluir varios elementos (widgets) como 
#botones, cuadros de texto, imágenes, etc. dentro de un marco (frame).

#Cuando se genere un GUI que incluya un panel (contenedor) se debe crear el código en el siguiente órden:
# - clase Panel: El contenedor incluye un objeto que instancíe la clase de cada widget que se quiera incluir.
#       - Widget: Dentro del constructor de la clase Panel se crea un objeto de cada widget que se quiera 
#         incluir en el contenedor, pero si es que alguno de estos elementos realiza una acción, fuera del 
#         constructor pero dentro de la clase Panel, se debe crear una función que describa lo que realiza. 
#         Los widgets que realizan acciones pueden ser: botones, checkboxes, áreas de texto, comboboxes, 
#         radiobuttons, listboxes, ventanas de diálogo, etc.
# - clase Frame: Dentro de la clase frame se declara su título y se instancía la clase panel para agregar el 
#   contenedor previamente creado a la ventana.
# - método main: A través del método main se ejecuta la clase frame para mostrar y ejecutar la ventana del GUI.

#ImageBrowsePanel: La clase hereda de la clase Panel, que pertenece a la librería wxPython y representa un 
#contenedor.
class ImageBrowsePanel(wx.Panel):
    #CONSTRUCTOR O INICIALIZADOR DE LA CLASE: En él se declaran los atributos que se reutilizarán en los demás 
    #métodos y que además, deben a fuerza de tener un valor.
    #El parámetro image_size se declaró en el constructor de la clase para que cuando se cree un objeto del 
    #panel en la clase Frame, se le tenga que indicar el tamaño del widget donde aparecerá la imagen, que no es 
    #igual al tamaño de la imagen misma, solo al de la ventana donde aparece.
    def __init__(self, parent, image_size):
        #super().__init__(parent): Lo que hace el método super() es heredar todos los métodos y atributos de la 
        #clase padre. En este caso es necesario incluirlo porque el constructor de la clase Panel recibe como 
        #parámetro al elemento parent.
        super().__init__(parent)
        #wx.Panel.SetBackgroundColour() = self.SetBackgroundColour(): Método aplicado al objeto de la clase 
        #Panel que recibe como parámetro el constructor de esta clase para cambiar el color del fondo del 
        #contenedor, el método realiza esto recibiendo un parámetro que instancíe la clase Colour de la librería 
        #wxPython, indicando el color en formato RGB:
        #  - wx.Colour(R, G, B): Los valores de RGB van de 0 a 255 y su combinación de colores rojo, verde y 
        #    azul crean cualquier color existente, el valor (0, 0, 0) corresponde al color negro y 
        #    (255, 255, 255) al blanco.
        self.SetBackgroundColour(wx.Colour(150, 0, 0))

        #CREACIÓN DE LOS WIDGETS: Botón
        #Instancia de la librería wxPython por medio del constructor de la clase Button para crear un widget de 
        #tipo botón, en este se debe indicar como parámetro el texto que aparece sobre él y su posición.
        # - label = "": Con este parámetro se indica el texto que aparecerá sobre el botón.
        # - pos = (x, y): Con este atributo se indica la posición fija en pixeles del widget, siendo la posición 
        #   0,0 la esquina superior izquierda, donde las "y" positivas indican que se mueva el botón hacia abajo 
        #   y las "x" positivas hacia la derecha.
        #       - Es importante mencionar que si después se utiliza la clase BoxSizer para posicionar los 
        #         elementos de forma relativa, esta posición no es respetada.
        browse_btn = wx.Button(self, label = "Browse", pos = (0,0)) 
        #No se declaran como self.nombreObjeto los widgets a los que no se les vaya a extraer o introducir datos 
        #en el transcurso del funcionamiento de la interfaz gráfica.
        
        #CREACIÓN DE LOS WIDGETS: Imágen
        #Las clases wx.Image y wx.Bitmap están relacionadas y se utilizan en conjunto para trabajar con 
        #imágenes en la interfaz gráfica.
        #   wx.Image: Representa una imagen en memoria creada con datos en bruto, osea un formato matricial 3D 
        #   conformado 3 capas o dimensiones RGB que contienen valores de 0 a 255. Esta clase proporciona 
        #   métodos para cargar, manipular y transformar imágenes.
        #  
        #   wx.Bitmap: Es una representación de imagen que puede ser utilizada directamente en los controles y 
        #   widgets de la interfaz gráfica de wxPython.

        #Cargar una Imagen: Se crea una instancia de la librería wxPython por medio del constructor de la clase 
        #Image para cargar una imagen en memoria con datos en bruto.
        # - filepath (str): En este atributo se indica el nombre de archivo junto con la ruta completa de donde 
        #   se encuentra la imagen que se va a cargar, la cual debe estar indicada en forma de string, con este 
        #   atributo no se sigue la nomenclatura de poner el nombre del atributo seguido de su valor 
        #   (filepath = valor), solamente se pone el path entre comillas.
        # - type (int): Indica el tipo de imagen a cargar. Puede ser uno de los siguientes valores predefinidos:
        #           - wx.BITMAP_TYPE_BMP: Bitmap de Windows.
        #           - wx.BITMAP_TYPE_JPEG: JPEG.
        #           - wx.BITMAP_TYPE_GIF: GIF.
        #           - wx.BITMAP_TYPE_PNG: PNG.
        #           - wx.BITMAP_TYPE_TIFF: TIFF.
        #           - wx.BITMAP_TYPE_PNM: PNM (Portable anymap).
        #           - wx.BITMAP_TYPE_PCX: PCX (ZSoft IBM PC Paintbrush file).
        #           - wx.BITMAP_TYPE_TGA: TGA (Truevision TGA file).
        #           - wx.BITMAP_TYPE_ICO: ICO (Icon file).
        #           - wx.BITMAP_TYPE_CUR: CUR (Cursor file).
        #           - wx.BITMAP_TYPE_XBM: XBM (X11 Bitmap).
        #           - wx.BITMAP_TYPE_XPM: XPM (X11 Pixmap).
        #           - wx.BITMAP_TYPE_WEBP: WEBP (WebP image format).
        #           - wx.BITMAP_TYPE_ANY: Cualquier tipo de imagen compatible.
        # - index (int): Este método se utiliza cuando se carga una imagen que contiene varias subimágenes 
        #   (como un archivo ICO o un archivo animado GIF). El valor predeterminado es -1 para cargar la imagen 
        #   principal.
        # - data (str o bytes): Datos en bruto de la imagen en formato binario. Se utiliza cuando la imagen no 
        #   se carga desde un archivo, sino desde una fuente de datos en memoria.
        # - mask (wx.Image o None): Representa una máscara opcional que se utilizará para darle transparencia 
        #   a la imagen. La máscara debe tener el mismo tamaño que la imagen principal y esta especifica cuáles 
        #   píxeles están completamente transparentes y cuáles son opacos.
        # - size (tuple): Parámetro opcional que especifica el tamaño deseado para la imagen cargada. Se utiliza 
        #   para redimensionar la imagen a un tamaño específico. El tamaño debe ser una tupla de dos elementos 
        #   en forma de (ancho, alto). 
        #       - Desempaquetar (*): Si es que se quiere indicar el tamaño de una imagen perteneciente a un GUI 
        #         fuera de la clase donde fue creada se debe usar el operador * el cual se utiliza en Python 
        #         para desempaquetar una secuencia (como una lista, tupla o conjunto) en sus elementos 
        #         individuales. 
        #         Esto significa que los elementos de la secuencia se extraen en el órden en el que fueron 
        #         declarados, se pasan y usan como argumentos separados a una función o constructor que espera 
        #         múltiples argumentos.
        #En sí existen dos widgets en esta GUI, uno vacío que se crea cuando se ejecuta la GUI sin haber 
        #seleccionado todavía el botón de Browse para cargar una imagen y el otro es el el que ya incluye la 
        #imagen cargada. El widget que se crea a continuación es el que se muestra inicialmente vacío, 
        #posteriormente en la función loadImage() se creará el otro que ya incluye la imagen después de haberse 
        #cargado.
        img = wx.Image(*image_size)
        #Crear un Bitmap: Una vez que se tiene una instancia de la clase wx.Image, se puede crear un objeto 
        #Bitmap, esto se puede realizar de dos formas: 
        #   - wx.Bitmap(wx.Image): El constructor de la clase Bitmap recibe como parámetro un objeto que 
        #     instancíe la clase Image, ambos pertenecientes a la librería de wxPython.
        #   - wx.Image.ConvertToBitmap(): Método utilizado para convertir un objeto Image en uno Bitmap. 
        #Esto convierte la imagen en un formato adecuado para que pueda ser utilizado en controles como 
        #wx.StaticBitmap, wx.Button, wx.BitmapButton, entre otros.

        #Mostrar la imagen en un widget: Para mostrar la imagen de tipo Bitmap en un widget gráfico de se usa 
        #una instancia de la clase wx.StaticBitmap, que es parte de la biblioteca wxPython y se utiliza para 
        #mostrar una imagen estática en un panel. Los parámetros que puede recibir la clase wx.StaticBitmap son 
        #los siguientes:
        # - parent: Es el objeto padre al que se añadirá el widget wx.StaticBitmap.
        # - id: Un identificador único para el widget. Puede ser de tipo entero o wx.ID_ANY para permitir que 
        #   wxPython asigne automáticamente un ID.
        # - bitmap: El objeto wx.Bitmap que se utilizará como imagen para el wx.StaticBitmap.
        # - pos: Una tupla (x, y) o un objeto wx.Point que indica la posición inicial del widget. Si no se 
        #   proporciona, se utilizará la posición predeterminada.
        # - size: Una tupla (width, height) o un objeto wx.Size que indica el tamaño del widget. Si no se 
        #   proporciona, se utilizará el tamaño predeterminado.
        # - style: Un estilo adicional para el widget wx.StaticBitmap. Puede incluir combinaciones de banderas:
        #           - wx.ALIGN_LEFT: Alinea el contenido del widget a la izquierda.
        #           - wx.ALIGN_RIGHT: Alinea el contenido del widget a la derecha.
        #           - wx.ALIGN_CENTER_HORIZONTAL: Centra horizontalmente el contenido del widget.
        #           - wx.ALIGN_TOP: Alinea el contenido del widget en la parte superior.
        #           - wx.ALIGN_BOTTOM: Alinea el contenido del widget en la parte inferior.
        #           - wx.ALIGN_CENTER_VERTICAL: Centra verticalmente el contenido del widget.
        #           - wx.ST_NO_AUTORESIZE: Evita que el widget se redimensione automáticamente cuando cambia el 
        #             tamaño de su contenido.
        #   Además de estos estilos, hay otros disponibles que permiten modificar aspectos estéticos, se pueden 
        #   combinar varios estilos utilizando el operador OR (|) para crear la combinación deseada:
        #           - wx.BORDER_NONE: No muestra ningún borde alrededor del widget.
        #           - wx.BORDER_SIMPLE: Muestra un borde simple alrededor del widget.
        #           - wx.BORDER_RAISED: Muestra un borde elevado alrededor del widget.
        #           - wx.BORDER_SUNKEN: Muestra un borde hundido alrededor del widget.
        #           - wx.BORDER_STATIC: Muestra un borde estático alrededor del widget.
        # - name: El nombre del widget.
        #Es importante destacar que los parámetros pos, size, style y name son opcionales y tienen valores 
        #predeterminados si no se proporcionan, el que si es necesario indicarlo es el objeto bitmap.
        self.image_ctrl = wx.StaticBitmap(parent = self, bitmap = wx.Bitmap(img))
        #Se declaran como self.nombreObjeto los widgets a los que sí se les vaya a extraer o introducir datos 
        #en el transcurso del funcionamiento de la interfaz gráfica.

        #CREACIÓN DE LOS WIDGETS: Área de Texto
        #Instancia de la librería wxPython por medio del constructor de la clase TextCtrl para crear un widget  
        #que proporciona una caja de texto de una sola línea o de varias líneas en la que los usuarios pueden 
        #ingresar y editar texto, en este se deben indicar los siguientes parámetros:
        # - parent: El widget padre al que pertenece la caja de texto, en este caso es self porque pertenece 
        #   al Panel.
        # - id: Un identificador único. Puede ser un número entero o el valor wx.ID_ANY para que wxPython 
        #   seleccione automáticamente un identificador.
        # - value: El texto inicial que se mostrará en la caja de texto.
        # - pos: La posición de la caja de texto en coordenadas (x, y) relativas al widget padre.
        # - size: El tamaño de la caja de texto en píxeles (ancho, alto).
        #           - El valor -1 indica que la altura se ajustará automáticamente según el contenido de la 
        #             caja de texto.
        # - style: Estilos que se aplicarán a la caja de texto para modificar su apariencia y comportamiento.
        #           - wx.TE_MULTILINE: Permite la edición de texto en varias líneas en lugar de una sola.
        #           - wx.TE_PASSWORD: Oculta el texto ingresado, como en el caso de contraseñas, mostrando 
        #             asteriscos o puntos en su lugar.
        #           - wx.TE_READONLY: Hace que la caja de texto sea de solo lectura, lo que impide que los 
        #             usuarios editen el contenido.
        #           - wx.TE_PROCESS_ENTER: Genera un evento wx.EVT_TEXT_ENTER cuando se presiona la tecla 
        #             Enter en la caja de texto.
        #           - wx.TE_CENTER: Centra el texto dentro de la caja de texto.
        #           - wx.TE_LEFT: Alinea el texto a la izquierda dentro de la caja de texto.
        #           - wx.TE_RIGHT: Alinea el texto a la derecha dentro de la caja de texto.
        # - validator: Un objeto wx.Validator que se utiliza para validar y controlar la entrada de texto, esto 
        #   se utiliza por ejemplo en las cajas de texto donde se ingresa un correo, en donde a fuerza debe 
        #   existir un @, hotmail.com, gmail.com, etc.
        #           - wx.TextValidator: Permite validar la entrada de texto utilizando expresiones regulares 
        #             y otras restricciones personalizadas.
        #           - wx.IntegerValidator: Permite ingresar solo valores enteros en la caja de texto.
        #           - wx.FloatingPointValidator: Permite ingresar solo valores de punto flotante en la caja de 
        #             texto.
        #           - wx.Validator: Clase base para crear validadores personalizados. Permite controlar el 
        #             formato y las restricciones de entrada.
        # - name: El nombre de la caja de texto.
        # - maxLength: La longitud máxima de caracteres que conforman el texto que se puede ingresar.
        # - initialValue: El valor inicial de la caja de texto antes de que se haya ingresado cualquier texto.
        # - autoCompleteMode: El modo de autocompletado que se aplicará a la caja de texto.
        # - autoCompleteChoices: Una lista de opciones para el autocompletado.
        # - passwordStyle: Si se establece en True, el texto ingresado se ocultará (por ejemplo, para ingresar 
        #   contraseñas).
        # - readonly: Si se establece en True, la caja de texto será de solo lectura y no se permitirá la 
        #   edición del texto.
        # - multiline: Si se establece en True, la caja de texto permitirá la entrada de múltiples líneas de 
        #   texto.
        self.photo_txt = wx.TextCtrl(self, style = wx.TE_READONLY, size = (200, -1))

        #POSICIONAMIENTO DE ELEMENTOS:
        #El siguiente código crea una instancia de la clase BoxSizer, la cual permite un posicionamiento 
        #relativo, colocando así un elemento respecto a otro, para poder usar esta clase el primer objeto se 
        #debe encontrar dentro del segundo. Si no se usa la clase BoxSizer, los elementos se colocarán unos 
        #encima de los otros.
        #Al crear la Instancia de la clase BoxSizer perteneciente a la librería wxPython se le puede pasar como 
        #parámetro solamente dos posibles atributos para indicar la dirección de la posición del objeto:
        # - wx.HORIZONTAL: Hace que la dirección de la alineación del primer objeto sea horizontal respecto al 
        #   segundo, esto se refiere a que se empiece indicar la posición del widget desde la esquina izquierda 
        #   dentro del contenedor.
        # - wx.VERTICAL: Hace que la dirección de la alineación del primer objeto sea vertical respecto al 
        #   segundo, esto se refiere a que se empiece indicar la posición del widget desde la parte superior de 
        #   en medio, dentro del contenedor.
        hsizer = wx.BoxSizer(wx.HORIZONTAL)     #Sizer del botón y Área de texto de su ruta.
        main_sizer = wx.BoxSizer(wx.VERTICAL)   #Sizer que incluye una imagen y al contenedor hziser.

        #Ya se mencionó que la clase BoxSizer sirve al posicionar un elemento respecto a otro, para ello uno de 
        #los elementos se debe encontrar dentro del otro, con el objetivo de indicar cuál es el primer objeto 
        #(el que tiene posicionamiento relativo) y cuál es el segundo objeto (el que contiene al primer objeto), 
        #se utilizan los métodos .Add() y .SetSizer() de la siguiente forma:

        #Instancia_BoxSizer.Add(): Método utilizado para agregar un elemento al sizer, sizer se refiere al 
        #elemento que contiene a otro que está colocado dentro de él con posicionamiento relativo, para ello 
        #dentro de su paréntesis se agregan los siguientes parámetros:
        # - primer_parámetro: Con este parámetro se indica qué objeto que será agregado dentro del otro, el 
        #   objeto contenedor es llamado sizer.
        # - proportion: Este parámetro determina cómo se asignará el espacio de todos los elementos que se 
        #   encuentran dentro del contenedor, aún si el sizer se expande o se reduce. 
        #           - proportion = 0: El elemento no crecerá ni se encogerá en relación a otros elementos 
        #             dentro del sizer.
        #           - proportion = valor: El elemento se expandirá o se encogerá proporcionalmente en el sizer, 
        #             dependiendo del valor de los demás elementos.
        #                   Por ejemplo, si hay dos elementos en el sizer, ambos con proportion = 1, cada uno 
        #                   ocupará la mitad del espacio disponible cuando el sizer se expanda. Si uno de los 
        #                   elementos tiene proportion = 2, ocupará dos tercios del espacio disponible, mientras 
        #                   que el otro elemento ocupará un tercio cuando el sizer se expanda.
        # - flag: El parámetro flag se utiliza para especificar las opciones de posicionamiento y alineación 
        #   del elemento dentro del sizer por medio de banderas, las acciones de estas banderas se pueden 
        #   combinar usando la operación lógica OR (|), las flags que se pueden usar son descritas a 
        #   continuación:
        #           - wx.EXPAND: Hace que el elemento se expanda para ocupar todo el espacio disponible en la 
        #             dirección del sizer.
        #           - wx.ALL: Agrega un borde en todos los lados del elemento.
        #           - wx.LEFT: Agrega un borde en el lado izquierdo del elemento.
        #           - wx.RIGHT: Agrega un borde en el lado derecho del elemento.
        #           - wx.TOP: Agrega un borde en la parte superior del elemento.
        #           - wx.BOTTOM: Agrega un borde en la parte inferior del elemento.
        #           - wx.CENTER: Centra el elemento dentro del espacio asignado por el sizer.
        #           - wx.ALIGN_LEFT: Alinea el elemento a la izquierda dentro del espacio asignado por el sizer.
        #           - wx.ALIGN_RIGHT: Alinea el elemento a la derecha dentro del espacio asignado por el sizer.
        #           - wx.ALIGN_TOP: Alinea el elemento en la parte superior dentro del espacio asignado por el 
        #             sizer.
        #           - wx.ALIGN_BOTTOM: Alinea el elemento en la parte inferior dentro del espacio asignado por 
        #             el sizer.
        # - border: Establece el espacio en píxeles entre el elemento y los bordes del sizer.
        #Botón agregado al contenedor hsizer
        hsizer.Add(browse_btn, proportion = 0,              #Botón agregado al hsizer, proportion = 0
                                flag = wx.ALL | wx.CENTER)  #Borde en todos los lados del elemento y Centrado.
        #Área de texto agregada al contenedor hsizer
        hsizer.Add(self.photo_txt, proportion = 1,          #Área de texto agregada al hsizer, proportion = 1
                                flag = wx.ALL | wx.CENTER,  #Borde en todos los lados del elemento y Centrado.
                                border = 10)                #Borde de 10 pixeles.
        #Imagen agregada al contenedor main_sizer
        main_sizer.Add(self.image_ctrl, proportion = 1,     #Imágen agregada al main_sizer, proportion = 0
                                flag = wx.ALL | wx.CENTER | wx.BOTTOM, #Bordes, Centrado y Alineado abajo.
                                border = 10)                #Borde de 10 pixeles.
        #Contenedor hsizer agregado al contenedor main_sizer
        main_sizer.Add(hsizer, proportion = 0,              #Panel hsizer agregado al main_sizer, proportion = 0
                                flag = wx.ALL | wx.EXPAND,  #Borde en todos los lados del elemento y Expandido.
                                border = 10)                #Borde de 10 pixeles.
        #wx.Panel.SetSizer() = self.SetSizer(): Método aplicado al objeto de la clase Panel que recibe como 
        #parámetro esta clase, el cuál recibe como parámetro un objeto de la clase BoxSizer para indicar cuál es 
        #el elemento contenedor al que ya se han agregado anteriormente uno o más widgets posicionados 
        #relativamente con el método .Add().
        self.SetSizer(main_sizer)
        #wx.BoxSizer.Fit() = sizer.SetSizer(): Método aplicado al objeto de la clase BoxSizer, el cual recibe 
        #como parámetro al parent del constructor de la clase Panel. El método se utiliza para ajustar 
        #automáticamente el tamaño del contenedor al tamaño óptimo para que quepa y se vea todo su contenido.
        main_sizer.Fit(parent)
        #wx.Panel.SetSizer() = self.SetSizer(): Método aplicado al objeto de la clase Panel que recibe como 
        #parámetro esta clase, el no recibe nada como parámetro. El método se utiliza para recalcular la 
        #disposición y la posición de los elementos dentro del contenedor después de realizar cambios en ellos, 
        #osea al haber dado clic sobre un botón y que se haya ejecutado su acción en el GUI o que se haya 
        #cambiado de tamaño la ventana.
        #Ambos métodos .Fit() y .Layout() son importantes para garantizar que los elementos se muestren 
        #correctamente y se ajusten adecuadamente en la interfaz de usuario. 
        self.Layout()

        #ACCIONES DEL BOTÓN: Para ejecutar la acción de un botón en Python, dentro del constructor de la clase 
        #Panel se debe mandar a llamar una función (método) que describa la acción a ejecutar, esta función se 
        #debe encontrar fuera del constructor pero pertenecer igualmente a la clase Panel.

        #ATRIBUTOS DEL CONSTRUCTOR DE LA CLASE PANEL: Dentro del constructor se deben declarar las variables con 
        #las que interactúen los botones para realizar acciones dentro del GUI.
        self.max_img_size = image_size #Atributo de la clase Panel que indica el tamaño del widget imagen.

        #Instancia_Button.Bind(): Este método se utiliza para enlazar un evento a un controlador de eventos, 
        #indicando en su primer parámetro el evento que detona el método y en el segundo la función que 
        #se ejecutará cuando ese evento ocurra. Normalmente las funciones que describen las acciones a 
        #realizar por los elementos del Panel se encuentran dentro de esta misma clase, pero fuera de su 
        #constructor.
        # - Tipos de Eventos en Python: 
        #       - wx.EVT_BUTTON: Evento que se activa cuando se hace clic en un botón.
        #       - wx.EVT_TEXT: Evento que se activa cuando se cambia el contenido de un control de texto.
        #       - wx.EVT_CHECKBOX: Evento que se activa cuando se cambia el estado de una casilla de 
        #         verificación.
        #       - wx.EVT_COMBOBOX: Evento que se activa cuando se selecciona un elemento de una lista 
        #         desplegable (combobox).
        #       - wx.EVT_LISTBOX: Evento que se activa cuando se selecciona un elemento de una lista (listbox).
        #       - wx.EVT_RADIOBUTTON: Evento que se activa cuando se selecciona un botón de opción (radiobutton) 
        #         en un grupo de botones de opción. 
        #       - wx.EVT_MENU: Evento que se activa cuando se selecciona una opción de menú.
        #       - wx.EVT_CLOSE: Evento que se activa cuando se intenta cerrar una ventana o diálogo.
        #       - wx.EVT_KEY_DOWN y wx.EVT_KEY_UP: Evento que se activan cuando se presiona o se suelta una 
        #         tecla del teclado, respectivamente.
        #       - wx.EVT_MOUSE_EVENTS: Son una serie de eventos relacionados con las interacciones del ratón, 
        #         como clics, movimiento, etc. Estos eventos son descritos a continuación:
        #               - wx.EVT_LEFT_DOWN: Se activa cuando se presiona el botón izquierdo del ratón.
        #               - wx.EVT_LEFT_UP: Se activa cuando se suelta el botón izquierdo del ratón.
        #               - wx.EVT_LEFT_DCLICK: Se activa cuando se hace doble clic con el botón izquierdo del 
        #                 ratón.
        #               - wx.EVT_RIGHT_DOWN: Se activa cuando se presiona el botón derecho del ratón.
        #               - wx.EVT_RIGHT_UP: Se activa cuando se suelta el botón derecho del ratón.
        #               - wx.EVT_RIGHT_DCLICK: Se activa cuando se hace doble clic con el botón derecho del 
        #                 ratón.
        #               - wx.EVT_MIDDLE_DOWN: Se activa cuando se presiona el botón central del ratón.
        #               - wx.EVT_MIDDLE_UP: Se activa cuando se suelta el botón central del ratón.
        #               - wx.EVT_MIDDLE_DCLICK: Se activa cuando se hace doble clic con el botón central del 
        #                 ratón.
        #               - wx.EVT_MOTION: Se activa cuando se mueve el ratón dentro del área del objeto 
        #                 capturador.
        #               - wx.EVT_ENTER_WINDOW: Se activa cuando el ratón entra en el área del objeto 
        #                 capturador.
        #               - wx.EVT_LEAVE_WINDOW: Se activa cuando el ratón sale del área del objeto capturador.
        #               - wx.EVT_MOUSEWHEEL: Se activa cuando se desplaza la rueda del ratón.
        #Evento de clic en botón, ejecutado por la función on_browse de esta clase Panel.
        browse_btn.Bind(wx.EVT_BUTTON, self.on_browse)
        

    #función on_browse(): Método creado dentro de la clase propia llamada ImageBrowsePanel que recibe como 
    #parámetro el evento que lo activa, para posteriormente ejecutar cierta acción.
    #En este caso el evento es activado por dar un clic sobre un botón y debe abrir el explorador de archivos 
    #para seleccionar la imagen que se va a mostrar en el GUI, además se introduce el directorio de su ubicación
    #en el área de texto de la ventana.
    def on_browse(self, event):
        #VARIABLES DE LA FUNCIÓN:
        #La variable img_type es una variable propia de esta función, esta declara un string para indicar cuál 
        #es el tipo de imágenes que se acepta para mostrar en el GUI.
        img_type = "JPEG files (*.jpg)|*.jpg"  #Palabra que se muestra al en el explorador de archivos para jpg.
        
        #Instancia de la librería wxPython por medio del constructor de la clase FileDialog para ejecutar una 
        #ventana de selección de archivos. A través de este cuadro de diálogo, los usuarios pueden seleccionar 
        #un archivo.
        # - with: La palabra reservada with se utiliza para garantizar una gestión adecuada de los recursos del 
        #   explorador de archivos. Cuando se finaliza el bloque with, se liberan automáticamente los recursos 
        #   utilizados por el cuadro de diálogo.
        #   - parent: Si se le pasa un valor None a este argumento lo que es significa que no hay un padre 
        #     específico para el cuadro de diálogo.
        #   - message: Con este parámetro se indica el texto que aparecerá sobre el explorador de archivos.
        #   - wildcard: Define el tipo de archivos que se pueden seleccionar, esto se debe ingresar como un 
        #     string.
        #   - style: Indica el estilo o comportamiento de la ventana de selección de archivos. Puede tomar 
        #     varios valores para personalizar la apariencia y la funcionalidad del cuadro de diálogo. 
        #         - wx.FD_OPEN: Este es el estilo predeterminado y se utiliza para permitir al usuario 
        #           seleccionar un archivo existente. El explorador mostrará los archivos y directorios en la 
        #           ubicación especificada.
        #         - wx.FD_SAVE: Este estilo se utiliza cuando se desea permitir al usuario seleccionar una 
        #           ubicación para guardar un archivo nuevo. El explorador mostrará los archivos y directorios 
        #           en la ubicación especificada y proporcionará una opción para ingresar un nombre de archivo.
        #         - wx.FD_OVERWRITE_PROMPT: Este estilo se utiliza en combinación con wx.FD_SAVE y muestra una 
        #           advertencia si el archivo seleccionado ya existe. El cuadro de diálogo mostrará un mensaje 
        #           preguntando al usuario si desea sobrescribir el archivo existente. las acciones de estos 
        #           estilos se pueden combinar usando la operación lógica OR (|).
        #         - wx.FD_MULTIPLE: Este estilo permite la selección de múltiples archivos. En lugar de 
        #           seleccionar un solo archivo, el usuario puede seleccionar varios archivos a la vez 
        #           utilizando la tecla de modificación apropiada (como Ctrl o Shift).
        #         - wx.FD_CHANGE_DIR: Este estilo indica que el cuadro de diálogo debe cambiar el directorio de 
        #           trabajo actual según la ubicación seleccionada por el usuario. Esto puede ser útil si desea 
        #           cambiar automáticamente el directorio de trabajo al directorio del archivo seleccionado.
        #         - wx.FD_PREVIEW: Este estilo muestra una vista previa del archivo seleccionado en el cuadro de 
        #           diálogo, si es posible. La vista previa puede ser una imagen, un documento o cualquier tipo 
        #           de archivo que pueda ser mostrado en el cuadro de diálogo.
        # - dialog: Objeto que permite mostrar cuadros de diálogo.
        #   - dialog.ShowModal(): Muestra el cuadro de diálogo y bloquea la ejecución del programa hasta que el 
        #     usuario seleccione un archivo o cierre el cuadro de diálogo, este método devuelve un código que 
        #     indica el resultado de la interacción del usuario con el cuadro de diálogo, como lo son: 
        #         - wx.ID_OK: Indica que el usuario ha seleccionado y confirmado una opción en el explorador de 
        #           archivos.
        #         - wx.ID_CANCEL: Indica que el usuario ha cancelado el cuadro de diálogo sin seleccionar ningún 
        #           archivo. Puede ocurrir si el usuario hace clic en el botón "Cancelar" o si cierra el 
        #           explorador de archivos.
        #         - wx.ID_YES: Indica que el usuario ha confirmado la selección en el cuadro de diálogo. Este 
        #           valor puede ser devuelto si se utiliza wx.FD_SAVE en el estilo del cuadro de diálogo y el 
        #           usuario decide sobrescribir un archivo existente.
        #         - wx.ID_NO: Indica que el usuario ha rechazado la selección en el cuadro de diálogo. Esto 
        #           puede ocurrir si se utiliza wx.FD_SAVE en el estilo del cuadro de diálogo y el usuario 
        #           decide no sobrescribir un archivo existente.
        #         - wx.ID_APPLY: Este valor puede ser utilizado para realizar alguna acción adicional después de 
        #           seleccionar un archivo en el cuadro de diálogo. No está directamente relacionado con la 
        #           selección del archivo en sí, y su uso depende de la implementación específica.
        #   - dialog.GetPath(): Devuelve la ruta completa del archivo seleccionado por el usuario en el cuadro 
        #     de diálogo. La ruta incluirá tanto el directorio como el nombre del archivo.
        #   - dialog.GetPaths(): Si el cuadro de diálogo permite la selección múltiple de archivos (configurado 
        #     con wx.FD_MULTIPLE en el argumento style), este método devuelve una lista de las rutas completas 
        #     de los archivos seleccionados.
        #   - dialog.GetDirectory(): Devuelve el directorio seleccionado por el usuario en el cuadro de diálogo. 
        #     Si el usuario ha seleccionado múltiples archivos de diferentes directorios, esta función devuelve 
        #     el directorio del primer archivo seleccionado.
        #   - dialog.GetFilenames(): Devuelve una lista de los nombres de archivo seleccionados por el usuario 
        #     en el cuadro de diálogo. Los nombres de archivo no incluyen la ruta del directorio.
        with wx.FileDialog(parent = None, message = 'Elige una imagen jpg',
                                wildcard = img_type,                #Tipo de archivo aceptado = Imagen .jpg
                                style = wx.FD_OPEN) as dialog:      #Permite seleccionar un archivo
            #Si el usuario ha seleccionado un archivo correctamente, por lo cual el método dialog.ShowModal() ha 
            #devuelto un valor wx.ID_OK, se devuelve la ruta completa de su ubicación y se coloca en el área de 
            #texto del GUI llamada photo_txt.
            if (dialog.ShowModal() == wx.ID_OK):
                #Setters y Getters: Como los valores de los atributos están encapsulados por haber sido creados 
                #dentro del constructor de la clase, existen dos tipos de métodos especiales para poder editar 
                #o extraer el valor de estas variables de clase:
                #   - nombre_Atributo.SetValue(): Método setter que permite editar el valor de un atributo.
                #   - nombre_Atributo.GetValue(): Método getter que permite obtener el valor de un atributo.

                self.photo_txt.SetValue(dialog.GetPath())
                #Una vez que se haya abierto la imagen, obtenido su directorio y colocado en el área de texto 
                #del GUI llamada photo_txt, se ejecuta una segunda función llamada loadImage() para colocar la 
                #imagen en el área de imagen del GUI. 
                self.loadImage()
    

    #función loadImage(): Método creado dentro de la clase propia llamada ImageBrowsePanel que recibe como 
    #parámetro a la instancia del objeto Frame que recibe esta misma clase como parámetro, por eso se usa la 
    #palabra reservada self. Esta función es llamada cuando termina su ejecución la función on_browse(), que a 
    #su vez es llamada cuando ocurre un evento de clic de botón.
    def loadImage(self):
        #Setters y Getters: Como los valores de los atributos están encapsulados por haber sido creados dentro 
        #del constructor de la clase, existen dos tipos de métodos especiales para poder editar o extraer el 
        #valor de estas variables de clase:
        #   - nombre_Atributo.SetValue(): Método setter que permite editar el valor de un atributo.
        #   - nombre_Atributo.GetValue(): Método getter que permite obtener el valor de un atributo.
        filepath = self.photo_txt.GetValue()
        print("Directorio de la imagen\n", filepath)

        #Cargar una Imagen: Se crea una instancia de la librería wxPython por medio del constructor de la clase 
        #Image para cargar una imagen en memoria con datos en bruto.
        # - filepath (str): En este atributo se indica el nombre de archivo o ruta completa de la imagen que se 
        #   va a cargar, su tipo de dato debe de ser string, con este atributo no se sigue la nomenclatura de 
        #   poner el nombre del atributo seguido de su valor (filepath = valor), solamente se pone el path 
        #   entre comillas.
        # - type (int): El tipo de imagen a cargar. Puede ser uno de los siguientes valores predefinidos:
        #           - wx.BITMAP_TYPE_BMP: Bitmap de Windows.
        #           - wx.BITMAP_TYPE_JPEG: JPEG.
        #           - wx.BITMAP_TYPE_GIF: GIF.
        #           - wx.BITMAP_TYPE_PNG: PNG.
        #           - wx.BITMAP_TYPE_TIFF: TIFF.
        #           - wx.BITMAP_TYPE_PNM: PNM (Portable anymap).
        #           - wx.BITMAP_TYPE_PCX: PCX (ZSoft IBM PC Paintbrush file).
        #           - wx.BITMAP_TYPE_TGA: TGA (Truevision TGA file).
        #           - wx.BITMAP_TYPE_ICO: ICO (Icon file).
        #           - wx.BITMAP_TYPE_CUR: CUR (Cursor file).
        #           - wx.BITMAP_TYPE_XBM: XBM (X11 Bitmap).
        #           - wx.BITMAP_TYPE_XPM: XPM (X11 Pixmap).
        #           - wx.BITMAP_TYPE_WEBP: WEBP (WebP image format).
        #           - wx.BITMAP_TYPE_ANY: Cualquier tipo de imagen compatible.
        # - index (int): Este método se utiliza cuando se carga una imagen esta que contiene varias subimágenes 
        #   (como un archivo ICO o un archivo animado GIF). El valor predeterminado es -1 para cargar la imagen 
        #   principal.
        # - data (str o bytes): Datos en bruto de la imagen en formato binario. Se utiliza cuando no se carga 
        #   desde un archivo, sino desde una fuente de datos en memoria.
        # - mask (wx.Image o None): Una imagen de máscara opcional que se utilizará para transparencia. La 
        #   imagen de máscara debe tener el mismo tamaño que la imagen principal y especifica qué píxeles están 
        #   completamente transparentes y cuáles son opacos.
        # - size (tuple): Parámetro opcional que especifica el tamaño deseado para la imagen cargada. Se utiliza 
        #   para redimensionar la imagen a un tamaño específico. El tamaño debe ser una tupla de dos elementos 
        #   en forma de (ancho, alto). 
        #       - Desempaquetar (*): Si es que se quiere indicar el tamaño de una imagen perteneciente a un GUI 
        #         fuera de la clase donde fue creada se debe usar el operador * el cual se utiliza en Python 
        #         para desempaquetar una secuencia (como una lista, tupla o conjunto) en sus elementos 
        #         individuales. 
        #         Esto significa que los elementos de la secuencia se extraen en el órden en el que fueron 
        #         declarados, se pasan y usan como argumentos separados a una función o constructor que espera 
        #         múltiples argumentos.
        img = wx.Image(filepath, type = wx.BITMAP_TYPE_ANY)

        #Una vez que se haya cargado la imagen y asignado el tamaño del widget donde aparece por medio del 
        #constructor, se ejecuta una función declarada dentro de la clase ImagePanel llamada loadImage(), que 
        #sirve para ajustar el tamaño de la imagen cargada antes de asignarla al widget y que aparezca en el 
        #GUI.
        img = self.scale_image(img, self.max_img_size)

        #Mostrar la imagen en un widget: Para mostrar la imagen de tipo Bitmap en un widget gráfico de se usa 
        #una instancia de la clase wx.StaticBitmap, que es parte de la biblioteca wxPython y se utiliza para 
        #mostrar una imagen estática en un panel. Los parámetros que puede recibir la clase wx.StaticBitmap son 
        #los siguientes:
        # - parent: Es el objeto padre al que se añadirá el widget wx.StaticBitmap.
        # - id: Un identificador único para el widget. Puede ser de tipo entero o wx.ID_ANY para permitir que 
        #   wxPython asigne automáticamente un ID.
        # - bitmap: El objeto wx.Bitmap que se utilizará como imagen para el wx.StaticBitmap.
        # - pos: Una tupla (x, y) o un objeto wx.Point que indica la posición inicial del widget. Si no se 
        #   proporciona, se utilizará la posición predeterminada.
        # - size: Una tupla (width, height) o un objeto wx.Size que indica el tamaño del widget. Si no se 
        #   proporciona, se utilizará el tamaño predeterminado.
        # - style: Un estilo adicional para el widget wx.StaticBitmap. Puede incluir combinaciones de banderas:
        #           - wx.ALIGN_LEFT: Alinea el contenido del widget a la izquierda.
        #           - wx.ALIGN_RIGHT: Alinea el contenido del widget a la derecha.
        #           - wx.ALIGN_CENTER_HORIZONTAL: Centra horizontalmente el contenido del widget.
        #           - wx.ALIGN_TOP: Alinea el contenido del widget en la parte superior.
        #           - wx.ALIGN_BOTTOM: Alinea el contenido del widget en la parte inferior.
        #           - wx.ALIGN_CENTER_VERTICAL: Centra verticalmente el contenido del widget.
        #           - wx.ST_NO_AUTORESIZE: Evita que el widget se redimensione automáticamente cuando cambia el 
        #             tamaño de su contenido.
        #   Además de estos estilos, hay otros disponibles que permiten modificar aspectos estéticos, se pueden 
        #   combinar varios estilos utilizando el operador OR (|) para crear la combinación deseada:
        #           - wx.BORDER_NONE: No muestra ningún borde alrededor del widget.
        #           - wx.BORDER_SIMPLE: Muestra un borde simple alrededor del widget.
        #           - wx.BORDER_RAISED: Muestra un borde elevado alrededor del widget.
        #           - wx.BORDER_SUNKEN: Muestra un borde hundido alrededor del widget.
        #           - wx.BORDER_STATIC: Muestra un borde estático alrededor del widget.
        # - name: El nombre del widget.
        #Es importante destacar que los parámetros pos, size, style y name son opcionales y tienen valores 
        #predeterminados si no se proporcionan, el que si es necesario indicarlo es el objeto bitmap.
        self.image_ctrl.SetBitmap(wx.Bitmap(img))
        self.Refresh()
    

    #función scale_image(): Método creado dentro de la clase propia llamada ImagePanel que recibe como 
    #parámetro a la imagen cargada con el objeto wx.Image y el tamaño del widget donde aparecerá dicha imagen, 
    #para después ajustar el tamaño de la imagen y que se vea completa en el widget del GUI.
    def scale_image(self, img, size):
        #De la variable size, la cual es una tupla de dos elementos en forma de (ancho, alto) que se le pasa 
        #como parámetro al constructor de esta clase y representa el tamaño del widget que mostrará la imagen, 
        #se obtiene y separa en dos variables distintas su ancho y alto para posteriormente ajustar el tamaño 
        #del objeto Image, que es la imagen cargada y representada en datos brutos.
        widget_width, widget_height = size  #Ancho y Alto en pixeles del widget.
        #wx.Image.GetWidth(): Método para obtener el ancho en pixeles de una imagen.
        img_width = img.GetWidth()          #Ancho en pixeles de la imagen en datos brutos.
        print("Ancho imagen:\t", img_width)
        #wx.Image.GetHeight(): Método para obtener la altura en pixeles de una imagen.
        img_height = img.GetHeight()        #Alto en pixeles de la imagen en datos brutos.
        print("Alto imagen:\t", img_height)

        #Si el ancho de la imagen es mayor que el ancho del widget, entonces se crearán nuevos valores para su 
        #ancho y alto, logrando así que se ajuste su tamaño al del widget, manteniendo su forma original:
        if img_width > widget_width:
            #El nuevo ancho de la imagen es igual al ancho del widget
            new_width = widget_width
            #La nueva altura de la imagen se obtiene al realizar una regla de 3 donde se busca obtener la altura 
            #proporcional del widget, conociendo ya la altura y el ancho de la imagen original y el ancho del 
            #widget al que se quiere llegar, por lo tanto la fórmula de la regla de 3 sería la siguiente:
            #   img_width   ->  widget_width
            #   img_height  ->  widget_height
            #Por lo cual, para obtener el widget_height y asignarlo a el nuevo ancho se utiliza la siguiente 
            #fórmula: widget_height = new_height = img_height*(widget_width/img_width)
            #El doble signo de "//" se utiliza en Python para realizar una división entera o "floor division", 
            #a diferencia del operador de división normal ("/"), que devuelve un número decimal, el operador 
            #"//" devuelve el cociente entero de la división, redondeando hacia abajo al número entero más 
            #cercano.
            #No se debe poner paréntesis en la operación matemática porque sino se puede confundir el programa 
            #y realizar mal la operación, ya que si primero realiza la división y obtiene un número decimal, 
            #esto se redondearía a cero y la operación daría un resultado erróneo.
            new_height = img_height * (widget_width // img_width)
            print("Operación Errónea // y ():\t\t", new_height, "=", img_height, "*(", widget_width, "//", img_width, ")")
            new_height = img_height * widget_width // img_width
            print("Operación Correcta //:\t\t\t", new_height, "=", img_height, "*", widget_width, "//", img_width)
            new_height = int(img_height * (widget_width / img_width))
            print("Operación Correcta método int() y /:\t", new_height, "= int(", img_height, "*(", widget_width, "/", img_width, "))")

            #wx.Image.Scale(): Método para redimensionar una imagen. Este método ajusta la imagen al tamaño 
            #especificado y devuelve una nueva instancia del objeto wx.Image con las dimensiones modificadas.
            img = img.Scale(new_width, new_height, wx.IMAGE_QUALITY_HIGH)
        #Si la altura de la imagen es mayor que la altura del widget, entonces se crearán nuevos valores para su 
        #ancho y alto, logrando así que se ajuste su tamaño al del widget, manteniendo su forma original:
        elif img_height > widget_height:
            #La nueva altura de la imagen es igual a la altura del widget
            new_height = widget_height
            #El nuevo ancho de la imagen se obtiene a través de una regla de 3, muy similar a como se realizó en 
            #el condicional de arriba. 
            new_width = widget_height * img_width // img_height

            #wx.Image.Scale(): Método para redimensionar una imagen. Este método ajusta la imagen al tamaño 
            #especificado y devuelve una nueva instancia del objeto wx.Image con las dimensiones modificadas.
            img = img.Scale(new_width, new_height, wx.IMAGE_QUALITY_HIGH)
        #Al terminar la función se devuelve la nueva img redimensionada para que esa sea puesta en el Bitmap.
        return img


#MainFrame: La clase hereda de la clase Frame que pertenece a la librería wxPython, representa la ventana del 
#GUI y crea una instancia de la clase MyPanel para agregar dentro de la ventana un contenedor con elementos 
#dentro.
class MainFrame(wx.Frame):
    #CONSTRUCTOR O INICIALIZADOR DE LA CLASE: En él se declaran los atributos que se reutilizarán en los demás 
    #métodos y que además, deben a fuerza de tener un valor.
    def __init__(self):
        #Dentro del constructor de la GUI se declara una instancia de la librería wxPython por medio de la cual 
        #se accede al constructor de la clase Frame, que representa la ventana del GUI, a dicha ventana se le 
        #asigna un título por medio de su segundo parámetro.
        super().__init__(None, title = "Hello World 4 -P00: Image Viewer")

        #ATRIBUTOS DEL CONSTRUCTOR DE LA CLASE FRAME: Dentro del constructor se deben declarar las variables con 
        #las que interactúen los elementos dentro del Frame.
        #No es lo mismo el tamaño de la imagen que está descrito por el atributo max_img_size dentro de la 
        #clase ImageBrowsePanel al tamaño de la ventana donde se muestra la imagen, que ahora se está declarando 
        #como un atributo propio de la clase Frame llamado img_widget_size, esto siempre y cuando se quiera que 
        #la imagen aparezca en un cuadrado, con ancho y alto del mismo valor.
        self.img_widget_size = 500      #Tamaño de la ventana de imagen, dado en pixeles = (ancho, alto)

        #Instancia de la clase ImageBrowsePanel para agregar el panel al Frame, osea el contenedor de elementos 
        #a la ventana de la GUI, se le pasa como parámetro a la instancia del objeto Frame que recibe esta misma 
        #clase como parámetro, por eso se usa la palabra reservada self.
        #Además se le indica el tamaño que tendrá el área donde aparecerá la imagen en la ventana con el 
        #parámetro image_size, que fue declarado como un parámetro del constructor.
        panel = ImageBrowsePanel(self, image_size = (self.img_widget_size, self.img_widget_size))
        #wx.Frame.show() = self.show(): Método aplicado al objeto de la clase Frame, del que hereda esta clase 
        #propia para mostrar la ventana del GUI.
        self.Show()


#__name__ == __main__: Método main, esta función es super importante ya que sirve para ejecutar los métodos de 
#las clases declaradas en el archivo, en python pueden existir varios métodos main en un solo programa.
if(__name__ == '__main__'):
    #Instancia de la librería wxPython por medio del constructor de la clase App para crear un objeto que 
    #funcione como la base de un GUI.
    app = wx.App(redirect= False)
    #Instancia de nuestra clase propia llamada Frame_With_Panel que fue creada en este mismo programa (frame se 
    #refiere a la ventana del GUI) e incluye una instancia de la clase Panel para agregar un contenedor con 
    #elementos dentro, el constructor vacío lo que hace es indicar que se cree y muestre la ventana.
    frame = MainFrame()
    #wxPython.App.MainLoop(): Método para que se ejecute en un loop infinito el GUI, logrando que no se 
    #ejecute una vez y luego cierre por sí solo, sino que solo se cierre al dar clic en el tache del frame.
    app.MainLoop()