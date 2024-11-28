#IMPORTACIÓN DE LIBRERÍAS:
#1.-MODELOS (Models): El modelo se refiere a la red neuronal que se va a utilizar para procesar el texto de entrada y 
#generar una respuesta, los Large Language Model (LLM) responden preguntas sin guardar un historial, mientras que los 
#Chats si guardan las preguntas y respuestas realizadas para crear una conversación. Existen varios modelos dentro de 
#una misma compañía, por ejemplo, OpenAI cuenta con gpt3, gpt4, gpt3.5 turbo, etc.
print("------------------------------------------LANGCHAIN-------------------------------------------")
print("------------------------------------------1.-MODELOS------------------------------------------")
#ChatOpenAI: Clase de la librería langchain que permite utilizar el modelo de chat (ChatGPT) de OpenAI con Python, este
#puede contestar preguntas adoptando un rol y guardar un historial durante la conversación.
from langchain.chat_models import ChatOpenAI    #ChatOpenAI: Modelo de Chat.

#2.-PROMPTS: Es el texto que se le envía al modelo para generar una respuesta y en este es donde se utilizan las 
#técnicas de Prompt Engineering, para ello la librería LangChain cuenta con diferentes clases que permiten utilizar 
#dichas técnicas, dependiendo de si se está mandando el Prompt a un LLM o a un Chat.
print("------------------------------------------2.-PROMPTS------------------------------------------")
#PromptTemplate: Clase de la librería langchain que permite mandar instrucciones o preguntas personalizadas a un modelo 
#LLM (Large Language Model) previamente invocado con Python, que no guarda un historial.
from langchain import PromptTemplate            #PromptTemplate: Pregunta mandada a un modelo LLM.
#ChatPromptTemplate: Clase de la librería langchain que permite mandar instrucciones o preguntas personalizadas a un 
#modelo de Chat, este puede contestar preguntas adoptando un rol a través de las siguientes clases:
#   - SystemMessagePromptTemplate: Con esta clase se indica el rol que interpretará ChatGPT al responder las preguntas 
#     del usuario.
#   - HumanMessagePromptTemplate: Con esta clase se representa el rol del usuario que manda preguntas a ChatGPT.
from langchain.prompts import ChatPromptTemplate #ChatPromptTemplate: Instrucciones mandadas a un modelo de chat.
from langchain.prompts import  SystemMessagePromptTemplate, HumanMessagePromptTemplate

#4.-CADENAS (Chains): Con esta herramienta se permite enlazar un modelo con un Prompt, también con ella se pueden 
#conectar varios modelos entre sí, hasta cuando son de distintos tipos, permitiéndonos así realizar varias iteraciones 
#entre modelos durante una consulta para obtener un mejor procesamiento final de los datos cuando este se busca aplicar 
#a tareas muy complejas.
print("------------------------------------------4.-CADENAS------------------------------------------")
#PROCESAMIENTO DE LLM: Permite encadenar un prompt con varios modelos de forma secuencial, uniendo así varias cadenas.
#   - TransformChain: Con esta clase se implementa una cadena de transformación, que se aplica a una entrada para 
#     producir una salida con un formato personalizado. Las transformaciones pueden ser representadas por cualquier 
#     función que tome una secuencia como entrada y devuelva una secuencia como salida.
#Por lo tanto, para que una cadena TransformChain funcione, se debe declarar una función propia que cambie el formato 
#de la salida de otra cadena.
from langchain.chains import TransformChain    #TransformChain: Librería que crea una cadena de cadenas.

class cerebro_OpenAI:
    #CONSTRUCTOR O INICIALIZADOR DE LA CLASE: En él se declaran los parámetros que recibe la clase, que además se 
    #utilizarán en los demás métodos, estos a fuerza deben tener un valor.
    #self: La instrucción self se utiliza para hacer referencia al objeto que se está manipulando cuando se instancía 
    #la clase. Por eso es que a través de la misma nomenclatura de un punto se accede a los distintos atributos y/o 
    #métodos con un objeto desde fuera de la clase.
    def __init__(self, parametro_de_la_clase):
        #ChatGPT API key
        self.LlaveApi = parametro_de_la_clase

    #POO: En Python cuando al nombre de una función se le ponen dos guiones bajos antes de su nombre es porque 
    #se está refiriendo a un método privado, es una buena práctica de sintaxis.
    #__ChatbotLangchain(preguntaUsuario): Función propia y con modificador de acceso privado que se encarga de recibir 
    #el texto de la pregunta realizada al modelo de Chat de OpenAI para contestar una pregunta según un rol asignado.
    def __ChatbotLangchain(self, preguntaUsuario):
        #ChatOpenAI(): En el constructor de la clase ChatOpenAI del paquete chat_models de la librería langchain se 
        #indica: 
        # - model_name: Parámetro que indica el modelo que se quiere utilizar, en este caso se utilizará gpt-3.5-turbo 
        #   que pertenece a GPT-3.5.
        # - openai_api_key: Con este parámetro se proporciona la API key, que por buenas prácticas debe provenir de 
        #   otro archivo.
        # - prompt_length: Longitud del prompt.
        # - max_tokens: Número máximo de tokens que se pueden generar.
        # - stop_token: El token de parada.
        # - temperature: La temperatura es un valor entre 0 y 1 que indica la creatividad con la que contesta el LLM, 
        #   si es demasiado grande, puede responder con algo totalmente aleatorio y si es muy bajo responderá lo mismo 
        #   siempre, función que podría ser deseada cuando por ejemplo se contestan problemas matemáticos.
        #Todos los modelos disponibles para usarse con OpenAI estan enlistados en el siguiente enlace y cada uno es 
        #mejor en ciertas funciones que el otro:
        #https://platform.openai.com/docs/models
        openaiChatGPT = ChatOpenAI(model_name = "gpt-3.5-turbo", openai_api_key = self.LlaveApi, temperature = 0.4)#Chat.

        #SYSTEM - ROL DEL CHAT AL RESPONDER PREGUNTAS DEL USUARIO: Para ello se utiliza un objeto PromptTemplate.
        #PromptTemplate(): En el constructor de la clase PromptTemplate perteneciente a la librería langchain se 
        #indica: 
        # - template: Parámetro que indica la pregunta del prompt.
        # - input_variables: Indica a través de una lista todos los nombres de las variables incluidas en la plantilla 
        #   del prompt, que se declararon dentro del template entre llaves {}.
        plantillaPromptSistema = PromptTemplate(
            template = "Tu nombre es Timmy, eres una asistente virtual carismática, burlona y experta en chistes de Chihuahueños." +
                       "Puedes contestar las preguntas del usuario espontáneamente de forma sarcástica y otras veces de forma " +
                       "seria y lógica para resolver sus problemas. El nombre del usuario es di0." + 
                       "Tu como asistente virtual puedes establecer alarmas, escribir en tu archivo NotasTimmy.txt, reproducir " +
                       "videos en YouTube, mandar mensajes por WhatsApp, mostrar imagenes con mapas de rutas, crear eventos en " +
                       "calendarios de Google Calendar y utilizar visión artificial para identificar colores o reconocimiento " +
                       "facial.",
            input_variables = []
        )
        #SystemMessagePromptTemplate(): Esta clase recibe como parámetro un objeto PromptTemplate, que previamente ya 
        #tiene diseñado el template que se mandará en el Prompt, indicándole al Chat el rol que está interpretando al 
        #responder.
        promptSistema = SystemMessagePromptTemplate(prompt = plantillaPromptSistema)

        #HUMAN - PREGUNTAS QUE EL USUARIO LE HACE AL MODELO: Para ello se utiliza un objeto PromptTemplate.
        plantillaPromptHumano = PromptTemplate(
            template = "Con tu basto conocimiento que te vuelve una genio contesta la siguiente pregunta del usuario:\n"
                       "{pregunta}",
            input_variables = ["pregunta"]
        )
        #HumanMessagePromptTemplate(): Esta clase recibe como parámetro un objeto PromptTemplate, que previamente ya 
        #tiene diseñado el template de la pregunta que hace el usuario al chat.
        promptHumano = HumanMessagePromptTemplate(prompt = plantillaPromptHumano)
        
        #ChatPromptTemplate.from_messages(): Método que sirve para unificar los templates previamente creados para el 
        #sistema (que le dice al modelo el rol que debe interpretar al responder mis preguntas), para el humano (que 
        #indica tal cual la pregunta realizada por el usuario) y de la AI (que es un rol adoptado por el modelo para 
        #guardar las preguntas y respuestas realizadas en un historial), creando así una conversación. El parámetro que 
        #recibe el método es una lista que incluye todas las plantillas de Prompt mencionadas previamente.
        plantillaChatPrompt = ChatPromptTemplate.from_messages([promptSistema, promptHumano])
        #ChatPromptTemplate().format_prompt().to_messages(): Método que rellena las variables del template mandado al 
        #Chat con valores de entrada para el prompt del sistema, del humano y de la AI, retornando una lista.
        promptMandadoChat = plantillaChatPrompt.format_prompt(pregunta = preguntaUsuario).to_messages()
        #str(): Método que convierte un número, lista, diccionario, etc. en un string para que pueda ser impreso en 
        #consola.
        print("Personalidad de Chatbot:\n" + str(promptMandadoChat[0].content) + "\n\n" +
              "Pregunta hecha al Chatbot:\n" + str(promptMandadoChat[1].content) + "\n")
        #ChatOpenAI(ChatPromptTemplate().format().to_messages()): Prompt mandado al modelo de Chat.
        respuestaChat = openaiChatGPT(promptMandadoChat)
        #Del diccionario retornado, el key de content es el que contiene la respuesta de la pregunta.
        print("Respuesta del Chatbot:\n", respuestaChat.content + "\n\n")
        return respuestaChat.content

    #__formatoHablarRespuesta(respuestaChat): Función propia y con modificador de acceso privado que se encarga de 
    #recibir la respuesta proporcionada por el modelo de Chat de OpenAI, para luego a través de una cadena de formato
    #llamada TranformChain(), quitar los saltos de línea del texto para que pueda hablar de forma fluida el asistente 
    #virtual.
    def __formatoHablarRespuesta(self, respuestaChat):
        #Función propia que cambia el formato de cualquier salida proporcionada por un modelo de Chat o LLM.
        def eliminarSaltosDeLinea(entrada):
            #Función que intercambia los saltos de línea por espacios.
            texto = entrada["texto"]    #Recibe una lista con un diccionario interno de key = texto.
            #lista.replace(): Método que reemplaza dentro de una lista un string por otro.
            return {"texto_limpio" : texto.replace("\n", " ")}
        #TransformChain(): Objeto que recibe un prompt, cambia su formato de una forma personalizada y lo retorna en 
        #una variable nueva.
        # - input_variables: Indica a través de una lista los prompts de entrada.
        # - output_variables: Indica a través de una lista el nombre de la variable de salida ya con el formato 
        #   deseado.
        # - transform: Recibe el nombre de la función propia que transforma el formato de la variable de entrada.
        cadenaTransformarFormato = TransformChain(input_variables = ["texto"],
                                                  output_variables = ["texto_limpio"],
                                                  transform = eliminarSaltosDeLinea)
        transformChainHablar = cadenaTransformarFormato.run(respuestaChat)
        return transformChainHablar
    
    #__formatoMensajeRespuesta(respuestaChat): Función propia y con modificador de acceso privado que se encarga de 
    #recibir la respuesta proporcionada por el modelo de Chat de OpenAI, para luego a través de una cadena de formato
    #llamada TranformChain() transformar la salida en una lista, con el fin de que el formato de la respuesta que se 
    #mandará por mensaje a WhatsApp se respete.
    def __formatoMensajeRespuesta(self, respuestaChat):
        def listaSaltosDeLinea(entrada):
            texto = entrada["texto"]
            return {"texto_lista_mensaje" : texto.split("\n")}
        cadenaTransformarFormato = TransformChain(input_variables = ["texto"],
                                                  output_variables = ["texto_lista_mensaje"],
                                                  transform = listaSaltosDeLinea)
        transformChainMensaje = cadenaTransformarFormato.run(respuestaChat)
        return transformChainMensaje
    
    #preguntarChatbot(preguntaUsuario): Método con modificador de acceso público que permite ejecutar los métodos 
    #privados __ChatbotLangchain(), __formatoHablarRespuesta y __formatoMensajeRespuesta para procesar la pregunta 
    #hecha por el usuario y responder en forma de lista que separa las líneas de texto de la respuesta y en forma de 
    #texto sin saltos de línea para que el asistente virtual pueda decir la respuesta y además la pueda mandar por 
    #medio de Whatsapp y que su formato se respete.
    def preguntarChatbot(self, preguntaUsuario):
        respuestaArchivo = self.__ChatbotLangchain(preguntaUsuario)          #Respuesta del método __ChatbotLangchain. 
        respuestaHablar = self.__formatoHablarRespuesta(respuestaArchivo)    #Formato de respuesta sin saltos de línea.
        respuestaMensaje = self.__formatoMensajeRespuesta(respuestaArchivo)  #Formato de respuesta en forma de lista.
        #return variable_1, variable_2, ..., variable_n: Cuando después de un método return se tiene más de 1 
        #variable, al ejecutar el método se deberán declarar dos variables que reciban cada resultado de forma 
        #correspondiente a través de la siguiente sintaxis:
        #   variable_1, variable_2, variable_n = objetoDeClase.métodoVariasVariables()
        return respuestaHablar, respuestaArchivo, respuestaMensaje