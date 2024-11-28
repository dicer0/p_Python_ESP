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

#IMPORTACIÓN DE LIBRERÍAS:
#IMPORTACIÓN DE LLAVE: Cuando se quiera utilizar una API que utiliza un key, por seguridad es de buenas prácticas 
#declararla en un archivo externo, además cabe mencionar que el nombre de dicho archivo y constante no pueden empezar 
#con un número, sino cuando la quiera importar obtendré un error y se va accediendo a sus carpetas por medio de puntos:
# - Directorio normal:      carpeta1/carpeta2/carpeta3
# - Directorio paquetes:    carpeta1.carpeta2.carpeta3
#La parte del directorio se coloca después de la palabra reservada import y posteriormente se manda a llamar sus 
#variables o constantes de igual manera a través de un punto.
import API_Keys.Llaves_ChatGPT_Bard_etc
#ChatGPT API key
ApiKey = API_Keys.Llaves_ChatGPT_Bard_etc.LlaveChatGPT 





#1.-MODELOS (Models): El modelo se refiere a la red neuronal que se va a utilizar para procesar el texto de entrada y 
#generar una respuesta, los Large Language Model (LLM) responden preguntas sin guardar un historial, mientras que los 
#Chats si guardan las preguntas y respuestas realizadas para crear una conversación. Existen varios modelos dentro de 
#una misma compañía, por ejemplo, OpenAI cuenta con gpt3, gpt4, gpt3.5 turbo, etc.
print("\n\n-----------------------------------------------1.-MODELOS-----------------------------------------------")
#OpenAI: Clase de la librería langchain que permite utilizar el LLM (Large Language Model) de OpenAI con Python, este
#puede resolver tareas sencillas, pero no se le proporciona roles y no guarda un historial de conversación.
from langchain.llms import OpenAI               #OpenAI: Modelo LLM.
#Cabe mencionar que, al utilizar la API en su modo gratuito, solo se podrán realizar 100 llamadas a la API por día, 
#si se excede ese límite, se recibirá el error RateLimitError al intentar ejecutar el programa de Python, pero si se 
#compra el servicio de la API, se cobrará a través de Tokens, que representan pedazos de palabras; como máximo se 
#pueden recibir o mandar a la vez 4096 tokens, que aproximadamente son 3,072 palabras.
#OpenAI(): En el constructor de la clase OpenAI perteneciente al paquete llms de la librería langchain se indica: 
# - model_name: Parámetro que indica el modelo que se quiere utilizar, en este caso se utilizará text-davinci-003 que 
#   pertenece a GPT-3.5.
# - openai_api_key: Con este parámetro se proporciona la API key, que por buenas prácticas debe provenir de otro 
#   archivo.
# - prompt_length: La longitud del prompt.
# - max_tokens: El número máximo de tokens que se pueden generar.
# - stop_token: El token de parada.
# - temperature: La temperatura es un valor entre 0 y 1 que indica la creatividad con la que contesta el LLM, si es 
#   demasiado grande, puede responder con algo totalmente aleatorio y si es muy bajo responderá lo mismo siempre, 
#   función que podría ser deseada cuando por ejemplo se contestan problemas matemáticos.
#Todos los modelos disponibles para usarse con OpenAI estan enlistados en el siguiente enlace y cada uno es mejor 
#en ciertas funciones que el otro:
#https://platform.openai.com/docs/models
openaiLLM = OpenAI(model_name = "text-davinci-003", openai_api_key = ApiKey, temperature = 0.5)           #LLM.

#ChatOpenAI: Clase de la librería langchain que permite utilizar el modelo de chat (ChatGPT) de OpenAI con Python, este
#puede contestar preguntas adoptando un rol y guardar un historial durante la conversación.
from langchain.chat_models import ChatOpenAI    #ChatOpenAI: Modelo de Chat.
#ChatOpenAI(): En el constructor de la clase ChatOpenAI del paquete chat_models de la librería langchain se indica: 
# - model_name: Parámetro que indica el modelo que se quiere utilizar, en este caso se utilizará gpt-3.5-turbo que 
#   pertenece a GPT-3.5.
# - openai_api_key: Con este parámetro se proporciona la API key, que por buenas prácticas debe provenir de otro 
#   archivo.
# - prompt_length: Longitud del prompt.
# - max_tokens: Número máximo de tokens que se pueden generar.
# - stop_token: El token de parada.
# - temperature: La temperatura es un valor entre 0 y 1 que indica la creatividad con la que contesta el LLM, si es 
#   demasiado grande, puede responder con algo totalmente aleatorio y si es muy bajo responderá lo mismo siempre, 
#   función que podría ser deseada cuando por ejemplo se contestan problemas matemáticos.
#Todos los modelos disponibles para usarse con OpenAI estan enlistados en el siguiente enlace y cada uno es mejor 
#en ciertas funciones que el otro:
#https://platform.openai.com/docs/models
openaiChatGPT = ChatOpenAI(model_name = "gpt-3.5-turbo", openai_api_key = ApiKey, temperature = 0.7)    #Chat.





#5.0.-EMBEDDINGS: Los LLM convierten y asocian palabras a través de un vector llamado Embedding, el cual es un simple 
#array de varias dimensiones que se encuentra en un espacio vectorial, cuya función es asociar de forma gráfica una 
#palabra con otras parecidas y/o alejarla de otras que sean muy distintas, de esta manera es como el modelo entiende 
#el lenguaje humano para realizar búsquedas, agrupaciones, clasificaciones, recomendaciones, etc.
print("\n-----------------------------------------------5.-ÍNDICES-----------------------------------------------")
#   - OpenAIEmbeddings: Clase que convierte cualquier texto que se le mande en un vector numérico.
from langchain.embeddings import OpenAIEmbeddings
#OpenAIEmbeddings(): El constructor de la clase OpenAIEmbeddings recibe los siguientes parámetros de OpenAI:
# - openai_api_key: Con este parámetro se roporciona la API key, que por buenas prácticas debe provenir de otro 
#   archivo.
# - model: Parámetro que indica el modelo que se quiere utilizar, en este caso se utilizará el más recomendado, que es 
#   el text-embedding-ada-002, que puede recibir como máximo 8191 y da como salida un vector con tamaño de 1536.
#https://platform.openai.com/docs/guides/embeddings/what-are-embeddings
modeloEmbedding = OpenAIEmbeddings(openai_api_key = ApiKey, model = "text-embedding-ada-002")
promptEmbedding = "Soy di_cer0!!!"
#OpenAIEmbeddings().embed_query(): El método .embed_query() toma una cadena de texto como entrada y devuelve un vector 
#(osea una lista) de números que representa su embedding. 
respuestaEmbedding = modeloEmbedding.embed_query(promptEmbedding)
#len(lista): Devuelve el tamaño de la lista a la que se le aplique, en este caso devuelve el tamaño del embedding.
print("Embedding obtenido del Prompt: ", promptEmbedding, "=", str(respuestaEmbedding), "con tamaño de",  
      str(len(respuestaEmbedding)), "\n\n")

#5.1.-ÍNDICES (Retrieval o Data connection): La forma en la que más se aprovechan los modelos de lenguaje es cuando se 
#les da acceso a distintas fuentes de información, como lo puede ser un archivo PDF, Word, Excel, PowerPoint, etc. 
#Los índices en LangChain son los que nos van a permitir enlazar un gran número de documentos para que sean procesados 
#por el modelo, para ello la librería cuenta con diferentes clases que permiten realizar el enlace.

#CARGAR VARIOS DOCUMENTOS .TXT, .DOCX O .PDF A LA VEZ DE UNA CARPETA CON LA CLASE DirectoryLoader: La gran 
#funcionalidad de esto radica cuando se quiere crear una base de datos de nuestros propios archivos, para hacerle 
#preguntas sobre ellos. 
#   - DirectoryLoader: Clase perteneciente al paquete document_loaders que permite cargar en el programa el contenido 
#     de todos los archivos incluidos en una carpeta, para ello se debe proporcionar el path completo del directorio e 
#     indicar el tipo de documento que se quiere importar. 
#     Cabe mencionar que esta Clase se apoya en la librería unstructured al ejecutarse, por lo que para cada tipo de 
#     documento que sea distinto a archivos con extensión .txt se deberá hacer una instalación adicional.
#       LEER DIRECTORIO CON ARCHIVOS .TXT:             Instalar con comando: pip install unstructured
#       LEER DIRECTORIO CON ARCHIVOS .PDF:             Instalar con comando: pip install unstructured[pdf]
#       LEER DIRECTORIO CON ARCHIVOS DE WORD .DOCX:    Instalar con comando: pip install unstructured[docx]
#   - CharacterTextSplitter: Esta clase perteneciente al paquete text_splitter de la librería langchain permite 
#     dividir un texto muy grande en cachos limitados por cierto número de caracteres, ya que recordemos que el máximo 
#     de tokens que admiten los modelos de OpenAI son de 4096 tokens, que aproximadamente son 3,072 palabras.
from langchain.document_loaders import DirectoryLoader             #DirectoryLoader: Carga varios archivos a la vez.
from langchain.text_splitter import CharacterTextSplitter          #CharacterTextSplitter: División por caracteres.
#DirectoryLoader(): El constructor recibe dos parámetros, el path global del directorio al que se quiere acceder y 
#el parámetro glob indica el tipo de archivos que se recibirá de la carpeta indicada: glob = "**/*.extensiónArchivo".
cargarDirectorio = DirectoryLoader("C:/Users/diego/OneDrive/Documents/Aprendiendo/Python/5.-Inteligencia Artificial/0.-Archivos_Ejercicios_Python/", glob = "**/*.txt")
#DirectoryLoader().load(): El método .load() carga en una variable todos los archivos contenidos en la carpeta 
#indicada dentro del constructor del objeto DirectoryLoader.
documentosTxt = cargarDirectorio.load() #Carga todos los archivos txt de una carpeta.
print("Documentos txt originales extraídos de un directorio:\n", documentosTxt, "\n")
#DirectoryLoader().load()[0].page_content: El método page_content devuelve el contenido del documento.
#len(lista): Devuelve el tamaño de la lista a la que se le aplique, en este caso devuelve el número de palabras del 
#documento.
print("El número de palabras del documento es de:\n", len(documentosTxt[0].page_content), "\n")
#CharacterTextSplitter(): El constructor del objeto lo que hace es indicar las características con las que se dividirá 
#un texto grande que se quiere procesar a través de algún modelo de lenguaje, ya que estos están limitados en el 
#número de tokens que pueden recibir, por ejemplo OpenAI solo admite 4096 tokens, que son aproximadamente 3,072 
#palabras. Esta clase se utiliza cuando se busca que los trozos sean grandes.
# - chunk_size: Con este parámetro se indica el número de caracteres de cada cacho de texto, llamado chunk, este 
#   número usualmente se encuentra entre 400 y 1000 caracteres. Pero es importante mencionar que, si el modelo 
#   considera que al cortar cierta parte del texto con el chunk_size indicado hace que se pierda contexto, este número 
#   será cambiado automáticamente por el método .split_documents().
# - chunk_overlap: Con este parámetro se indica los caracteres que se entrelazan con el cacho que tiene alado, para 
#   que de esta forma no se pierda ninguna palabra.
dividirTexto = CharacterTextSplitter(chunk_size = 40, chunk_overlap = 0)    #División de texto por caracteres.
#CharacterTextSplitter().split_documents(): Método que divide el texto grande que recibe como parámetro en cachos 
#cuyas características fueron descritas en el constructor de la clase CharacterTextSplitter.
documentosDivididos = dividirTexto.split_documents(documentosTxt)
print("\n\nDocumentos txt divididos con la clase CharacterTextSplitter:\n", documentosDivididos, "\n")
print("Cacho de documento txt dividido:\n", documentosDivididos[5], "\n\n\n")

#CARGAR UN DOCUMENTO PDF A LA VEZ Y DIVIDIRLO POR PÁGINAS CON LA CLASE PyPDFLoader DE LANGCHAIN:
#   - PyPDFLoader: Clase del paquete document_loaders que permite leer documentos PDF con la librería langchain. Su 
#     mayor ventaja es que de forma muy sencilla permite separar su contenido por página. 
#   - OnlinePDFLoader: Clase del paquete document_loaders que permite leer documentos PDF a través de un enlace. Se 
#     carga su contenido con el método .load() como se hace con el objeto DirectoryLoader.
from langchain.document_loaders import PyPDFLoader                 #PyPDFLoader: Carga 1 documento PDF a la vez.
#PyPDFLoader(): El constructor recibe como único parámetro el path global del archivo PDF al que se quiere acceder.
cargarDocumentoPDF = PyPDFLoader("C:/Users/diego/OneDrive/Documents/Aprendiendo/Python/5.-Inteligencia Artificial/0.-Archivos_Ejercicios_Python/0.-Python - Conceptos Básicos.pdf")
#PyPDFLoader().load_and_split(): Método que divide el texto grande del archivo PDF recibido en el constructor de la 
#clase PyPDFLoader por páginas, dentro un objeto document que incluye todo el contenido del PDF, esto después no 
#podrá ser dividido de nuevo con alguna clase del paquete text_splitter perteneciente a la librería langchain, por 
#lo que directamente con ella se creará el embedding de cada página.
paginasPDF = cargarDocumentoPDF.load_and_split()                   #División del texto de un PDF por página.
print("Documento PDF dividido por páginas con la clase PyPDFLoader de langchain:\n", paginasPDF[2], "\n")
print("Número total de páginas en el documento:\n", len(paginasPDF), "\n")
print("Contenido de la segunda página del documento PyPDFLoader:\n", paginasPDF[2].page_content, "\n")
print("Número de caracteres de la segunda página del documento PyPDFLoader:\n", len(paginasPDF[2].page_content), "\n")
print("Tipo de dato del resultado obtenido con la clase PyPDFLoader:\n", type(paginasPDF), "\n\n\n")

#CARGAR UN DOCUMENTO PDF, DIVIDIRLO POR PÁGINAS Y LUEGO ESAS PÁGINAS PARTIRLAS EN CACHOS CON LA LIBRERÍA PyPDF2:
#   - PdfReader: Esta clase de la librería open source PyPDF2 permite leer escribir y manipular archivos PDF con 
#     python.
#   - RecursiveCharacterTextSplitter: Esta clase permite dividir un texto grande en cachos para que pueda ser 
#     procesado por un modelo de lenguaje, pero limita los cachos en los que se divide el texto en forma de tokens, 
#     no de caracteres.
from PyPDF2 import PdfReader                                       #PdfReader: Carga 1 documento PDF a la vez.
from langchain.text_splitter import RecursiveCharacterTextSplitter #RecursiveCharacterTextSplitter: Cachos de tokens.
documentoPDF = PdfReader("C:/Users/diego/OneDrive/Documents/Aprendiendo/Python/5.-Inteligencia Artificial/0.-Archivos_Ejercicios_Python/2.-Op-Amp Inversor con Filtro Pasa Altas.pdf")
#PdfReader().pages: Con el atributo .pages se accede al número de páginas del documento pdf leído con el constructor 
#del objeto PdfReader.
#PdfReader().pages[i].extract_text(): Con el método .extract_text() se extrae todo el texto perteneciente a una 
#página en específico del documento pdf ingresado a través del constructor del objeto PdfReader.
#len(): Método que devuelve el tamaño de la lista a la que se le aplique, en este caso devuelve el número de páginas 
#del documento pdf.
textoPDF = ""                               #Variable textoPDF que después guardará todo el texto del pdf.
for i in range(len(documentoPDF.pages)):    #Bucle for que lee todas las páginas del documento.
    pagina = documentoPDF.pages[i]          #En la variable página se guarda el número de página.
    textoPagina = pagina.extract_text()     #En la variable textoPagina se guarda el texto contenido en cada página.
    textoPDF += textoPagina                 #Concatenación del texto extraído de cada página.
print("Texto extraído de un documento PDF completo con la clase PdfReader de PyPDF2:\n", textoPDF, "\n\n")
print("Documento PDF dividido por páginas con la clase PdfReader de PyPDF2:\n", documentoPDF.pages[2].extract_text(), "\n")
print("Número total de páginas en el documento:\n", len(documentoPDF.pages), "\n")
print("Tipo de dato del resultado obtenido con la clase PyPDF2:\n", type(documentoPDF), "\n\n\n")
#RecursiveCharacterTextSplitter(): El constructor del objeto lo que hace es indicar las características con las que se 
#separará en cachos un texto grande para que se pueda procesar con algún modelo de lenguaje, pero esto se hace eun 
#función de un número de tokens, no de caracteres. Esta clase se utiliza cuando se busca que los trozos sean pequeños.
# - chunk_size: Con este parámetro se indica el número de tokens de cada cacho de texto, llamado chunk, este número 
#   usualmente se encuentra entre 512 y 1000 tokens. Pero es importante mencionar que si el modelo considera que al 
#   cortar cierta parte del texto con el chunk_size indicado hace que pierda contexto, este número será cambiado 
#   automáticamente por el método .create_documents().
# - chunk_overlap: Con este parámetro se indica los caracteres que se entrelazan con el cacho que tiene alado, para 
#   que de esta forma no se pierda ninguna palabra.
# - length_function: Indica qué función se utilizará para contar el número de tokens de cada cacho, puede ser la 
#   función predefinida len(lista) o una función propia.
dividirPaginasPDF = RecursiveCharacterTextSplitter(chunk_size = 160, chunk_overlap = 10, length_function = len)
#CharacterTextSplitter().create_documents(): Método que divide el texto grande que recibe como parámetro en cachos 
#cuyas características fueron descritas en el constructor de la clase RecursiveCharacterTextSplitter.
chunksPaginasPDF = dividirPaginasPDF.create_documents([textoPDF])
print("Documento pdf dividido con la clase RecursiveCharacterTextSplitter:\n", chunksPaginasPDF, "\n")
print("Cacho de documento pdf dividido:\n", chunksPaginasPDF[10], "\n\n\n")
print("Cacho de documento pdf dividido:\n", chunksPaginasPDF[11].page_content, "\n\n\n")

#5.2.-VECTOR STORES: Los LLM convierten y asocian palabras a través de un vector llamado Embedding, las clases FAISS 
#y Chroma que representan Vector Stores ayudan a integrar bases de datos optimizadas para almacenar los vectores 
#obtenidos después de procesar los Chunks de información.
#Embeddings: Es la herramienta que convierte los pedazos de palabras obtenidos de un documento (chunks) en vectores
#numéricos.
from langchain.embeddings import OpenAIEmbeddings
#OpenAIEmbeddings(): El constructor de la clase OpenAIEmbeddings recibe los siguientes parámetros de OpenAI:
# - openai_api_key: Con este parámetro se roporciona la API key, que por buenas prácticas debe provenir de otro 
#   archivo.
# - model: Parámetro que indica el modelo que se quiere utilizar, en este caso se utilizará el más recomendado, que es 
#   el text-embedding-ada-002, que puede recibir como máximo 8191 y da como salida un vector con tamaño de 1536.
#https://platform.openai.com/docs/guides/embeddings/what-are-embeddings
modeloEmbedding = OpenAIEmbeddings(openai_api_key = ApiKey, model = "text-embedding-ada-002")
#Vectorstores: Representa una base de datos donde se asocian los chunks de palabras con sus embeddings 
#correspondientes para que así se alimente a cualquier modelo de lenguaje con nuestra información, pudiendo así 
#realizarle consultas sobre ella.
from langchain.vectorstores import FAISS    #FAISS: Vector store rápida, poco flexible y difícil de usar.
from langchain.vectorstores import Chroma   #Chroma: Vector store no tan rápida, flexible y fácil de usar.
#FAISS o Chroma.from_documents(): Método que crea la base de datos de vectores tipo FAISS o Chroma, esta recibe los 
#chunks extraídos del texto y el modelo de embeddings declarado para su almacenamiento.
baseDeDatosFAISS_PyPDFLoader = Chroma.from_documents(paginasPDF, modeloEmbedding) #PyPDFLoader (langchain).
baseDeDatosFAISS_PdfReader = FAISS.from_documents(chunksPaginasPDF, modeloEmbedding) #PdfReader (PyPDF2).
baseDeDatosFAISS_DirectoryLoader = Chroma.from_documents(documentosDivididos, modeloEmbedding) #Dir..Load (langchain).

#5.3.-RETRIEVER: Este tipo de clases permiten extraer información de alguna fuente en específico, que suelen ser VECTOR 
#STORES, sabiendo a dónde tiene que ir a buscar para obtener la respuesta solicitada a través de cadenas de búsqueda o 
#algoritmos de búsqueda de proximidad.
#El concepto de cadena de búsqueda se refiere a un modelo de lenguaje que se ha entrenado con un conjunto de datos de 
#preguntas y respuestas. Puede utilizarse para responder a preguntas sobre un documento personal ingresado a un VECTOR 
#STORE. Para ello se puede utilizar alguna de las siguientes herramientas:
from langchain.chains.question_answering import load_qa_chain
# - load_qa_chain(): Método que carga una cadena de búsqueda de preguntas y respuestas preentrenada.
#   - llm: Indica el modelo de lenguaje o chat a utilizar.
#   - chain_type: Indica el tipo de cadena de búsqueda a utilizar:
#       - "stuff": Cadena de búsqueda predeterminada (LLM factual de Google AI) que es capaz de generar texto, 
#         traducir idiomas, escribir diferentes tipos de contenido creativo y responder a sus preguntas de manera 
#         informativa.
cadenaBusquedaPreentrenada = load_qa_chain(llm = openaiLLM, chain_type = "stuff")
#PREGUNTAS HECHAS A UN MODELO LLM:
from langchain.chains import RetrievalQA
# - RetrievalQA.from_chain_type(): Método que crea una cadena de búsqueda de preguntas y respuestas de un tipo 
#   específico. Los tipos de cadenas de búsqueda disponibles son: "map_reduce", "refine" y "map_rerank".
#   - llm: Indica el modelo de lenguaje o chat a utilizar.
#   - chain_type: Indica el tipo de cadena de búsqueda a utilizar:
#       - "stuff": Cadena de búsqueda predeterminada (LLM factual de Google AI) que es capaz de generar texto, 
#         traducir idiomas, escribir diferentes tipos de contenido creativo y responder a sus preguntas de manera 
#         informativa.
#       - "map_reduce": Cadena de búsqueda que primero utiliza un retriever para recuperar documentos relevantes.
#       - "refine": Cadena de búsqueda que primero utiliza un retriever para recuperar documentos relevantes y 
#         luego utiliza el LLM para refinar las respuestas.
#       - "map_rerank": Cadena de búsqueda que primero utiliza un retriever para recuperar documentos relevantes y 
#         luego utiliza el LLM para reordenar las respuestas.
#   - retriever: Tipo de retriever que se utilizará para recuperar los documentos relevantes para contestar la 
#     pregunta.
#       - "faiss": Retriever predeterminado que utiliza el algoritmo de búsqueda vectorial faiss para recuperar los 
#         documentos relevantes.
#       - "chroma": Retriever que utiliza el algoritmo de búsqueda vectorial chroma para recuperar los documentos 
#         relevantes.
#       - "multi_query_retriever": Este retriever genera variantes de la pregunta de entrada y luego utiliza un 
#         algoritmo de búsqueda vectorial para recuperar los documentos relevantes para cada variante.
#       - vectorStore.as_retriever(): El método as_retriever() convierte cualquier base de datos vectorial en un 
#         retriever para que de ahí se extraiga la información para responder la pregunta del usuario.
cadenaBusquedaPersonalizada = RetrievalQA.from_chain_type(llm = openaiLLM, chain_type = "map_reduce", 
                                                          retriever = baseDeDatosFAISS_PdfReader.as_retriever())
#PREGUNTAS HECHAS A UN MODELO DE CHAT:
from langchain.chains import ConversationalRetrievalChain
# - ConversationalRetrievalChain.from_llm(): Método que crea una cadena de búsqueda de preguntas y respuestas a través 
#   de un modelo de lenguaje probabilístico. El modelo de lenguaje se puede utilizar para generar respuestas más 
#   naturales y conversacionales a través de la memoria de un historial de chat.
#   - llm: Indica el modelo de lenguaje o chat a utilizar.
#   - chain_type: Indica el tipo de cadena de búsqueda a utilizar:
#       - "stuff": Cadena de búsqueda predeterminada (LLM factual de Google AI) que es capaz de generar texto, 
#         traducir idiomas, escribir diferentes tipos de contenido creativo y responder a sus preguntas de manera 
#         informativa.
#   - retriever: Tipo de retriever que se utilizará para recuperar los documentos relevantes para contestar la 
#     pregunta.
#       - "faiss": Retriever predeterminado que utiliza el algoritmo de búsqueda vectorial faiss para recuperar los 
#         documentos relevantes.
#       - "chroma": Retriever que utiliza el algoritmo de búsqueda vectorial chroma para recuperar los documentos 
#         relevantes.
#       - "multi_query_retriever": Este retriever genera variantes de la pregunta de entrada y luego utiliza un 
#         algoritmo de búsqueda vectorial para recuperar los documentos relevantes para cada variante.
#       - vectorStore.as_retriever(): El método as_retriever() convierte cualquier base de datos vectorial en un 
#         retriever para que de ahí se extraiga la información para responder la pregunta del usuario.
#   - memory: Recibe un objeto de memoria que se utilizará para almacenar el historial de la cadena de búsqueda.
#   - prompt: Plantilla de preguntas variables que se utilizará para generar respuestas.
#   - verbose: Variable booleana que controla la información impresa en consola. Cuando verbose es True, el objeto 
#     ConversationChain imprimirá información sobre el proceso de generación de la conversación, incluyendo el prompt, 
#     los tokens generados, y las puntuaciones de los tokens, pero cuando es False, no se imprimirá ninguna 
#     información.
#   - return_source_documents: Variable booleana que por default se encuentra con valor de False, pero cuando vale 
#     True retorna la página de mis documentos en la cual se basó para contestar la pregunta.
cadenaBusquedaHistorialChat = ConversationalRetrievalChain.from_llm(llm = openaiLLM, chain_type = "map_reduce", 
                                                                    retriever = baseDeDatosFAISS_DirectoryLoader.as_retriever(),
                                                                    return_source_documents = True)

#El concepto de búsqueda de proximidad se refiere a un algoritmo de filtrado que se puede utilizar para encontrar los 
#documentos más similares a una consulta realizada. Para ello se puede utiliza la siguiente herramienta:
# - FAISS_o_Chroma.from_documents().similarity_search(): El método similarity_search() utiliza el VECTOR STORE FAISS o 
#   Chroma para realizar una búsqueda de proximidad.
#Pregunta hecha al documento ingresado al programa a través de la librería PyPDFLoader de langchain.
preguntaDocumento_PyPDFLoader = "Dime algunos usos del lenguaje de programación Python" 
busqueda_PyPDFLoader = baseDeDatosFAISS_PyPDFLoader.similarity_search(preguntaDocumento_PyPDFLoader)
#Pregunta hecha al documento ingresado al programa a través de la librería PdfReader de PyPDF2.
preguntaDocumento_PdfReader = "Cómo decae la amplitud al modificar la frecuencia en un filtro pasa bajas?"
busqueda_PdfReader = baseDeDatosFAISS_PdfReader.similarity_search(preguntaDocumento_PdfReader)
#Pregunta hecha a los documentos ingresados al programa a través de la librería DirectoryLoader de langchain.
historialChat = []
preguntaDocumento_DirectoryLoader = "Cuales son las variables utilizadas para calcular la matriz de rigidez de un elemento?"
busquedaDirectoryLoader = baseDeDatosFAISS_DirectoryLoader.similarity_search(preguntaDocumento_DirectoryLoader)

#load_qa_chain().run(): El método run() se aplica a la cadena de búsqueda load_qa_chain, recibiendo como parámetros 
#el resultado del método similarity_search() y la pregunta realizada para que así se busque en la VECTOR STORE y se
#obtenga el resultado de la pregunta realizada en base a la información del documento txt, word, pdf, etc.
resultado_PyPDFLoader = cadenaBusquedaPreentrenada.run(
                                                    input_documents = busqueda_PyPDFLoader, 
                                                    question = preguntaDocumento_PyPDFLoader)
print("Cadena de Búsqueda load_qa_chain con base de datos vectorial FAISS al documento cargado con PyPDFLoader (langchain):\n", 
      str(resultado_PyPDFLoader), "\n\n")

#RetrievalQA.from_chain_type()({"query": pregunta}): A través de un diccionario con la key "query" se realiza una 
#pregunta a una cadena de búsqueda RetrievalQA.
resultado_PdfReader = cadenaBusquedaPersonalizada({"query" : preguntaDocumento_PdfReader})
print("Cadena de Búsqueda RetrievalQA con base de datos vectorial Chroma al documento cargado con PdfReader (PyPDF2):\n", 
      str(resultado_PdfReader), "\n\n")

#ConversationalRetrievalChain.from_llm()({"query": pregunta, "chat_history": listaHistorial}): A través de un 
#diccionario con la key "question" y "chat_history" se realiza una pregunta a una cadena de búsqueda de chat 
#ConversationalRetrievalChain y luego se almacena en una lista el historial de preguntas y respuestas.
resultado_DirectoryLoader = cadenaBusquedaHistorialChat({"question" : preguntaDocumento_DirectoryLoader, "chat_history" : historialChat})
print("Cadena de Búsqueda ConversationalRetrievalChain con base de datos vectorial FAISS al documento cargado con DirectoryLoader (langchain):\n", 
      str(resultado_DirectoryLoader), "\n\n")
print("Fuente de donde le cadena de búsqueda extrajo la respuesta de la pregunta hecha a los documentos DirectoryLoader:\n", 
      str(resultado_DirectoryLoader['source_documents']), "\n\n", 
      str(resultado_DirectoryLoader['source_documents'][0]), "\n\n", 
      str(resultado_DirectoryLoader['source_documents'][0].page_content))