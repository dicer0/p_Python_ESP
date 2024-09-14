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
import openai #openai: Librería que permite utilizar el LLM (Large Language Model) de ChatGPT con Python.
#Cabe mencionar que, al utilizar la API en su modo gratuito, solo se podrán realizar 100 llamadas a la API por día, 
#si se excede ese límite, se recibirá el error RateLimitError al intentar ejecutar el programa de Python.

#IMPORTACIÓN DE LLAVE: Cuando se quiera utilizar una API que utiliza un key, por seguridad es de buenas prácticas 
#declararla en un archivo externo, además cabe mencionar que el nombre de dicho archivo y constante no pueden empezar 
#con un número, sino cuando la quiera importar obtendré un error y se va accediendo a las carpetas por medio de puntos:
# - Directorio normal:      carpeta1/carpeta2/carpeta3
# - Directorio paquetes:    carpeta1.carpeta2.carpeta3
#La parte del directorio se coloca después de la palabra reservada from y la llave a importar después de import.
from API_Keys.Llaves_ChatGPT_Bard_etc import LlaveChatGPT

#openai.api_key: A través de este atributo perteneciente a la librería openai, se declara la API key, que previamente 
#debió ser creada y extraída de la página oficial de OpenAI, asociada a nuestro usuario: 
#https://platform.openai.com/account/api-keys 
openai.api_key = LlaveChatGPT

#INTRODUCIR POR MEDIO DE CÓDIGO UNA SOLA PREGUNTA QUE QUIERO QUE RESPONDA CHATGPT:
#openai.ChatCompletion.create(): El método create() aplicado al objeto ChatCompletion perteneciente a la librería 
#openai se encarga de crear chats que se puedan mandar a ChatGPT. Este recibe los siguientes parámetros:
# - model: Describe el modelo de lenguaje que se utilizará para generar la salida. Los modelos disponibles son 
#   gpt-3, gpt-4 y el más reciente es gpt-3.5-turbo. Todos se encuentran mencionados en la 
#   documentación de OpenAI: https://platform.openai.com/docs/models/overview
# - messages: Representa la lista de mensajes que se utilizarán para generar la salida del chat. Cada mensaje es un 
#   objeto con los siguientes campos:
#       - role: El rol del mensaje ayuda al modelo de lenguaje a entender el contexto de la conversación. Los roles 
#         posibles son system, user y assistant, indicándole así de forma separada a quién está interpretando ChatGPT 
#         para que de esta manera pueda dar respuestas de forma específica:
#           - system: Por medio de este rol se le indica a ChatGPT a quién está interpretando cuando responda las 
#             preguntas del usuario.
#           - user: En este rol se está indicando las preguntas que está realizando el usuario a ChatGPT.
#           - assistant: Este rol es adoptado por ChatGPT siempre que responda a la pregunta de un usuario y se 
#             observa en el resultado retornado por el objeto ChatCompletion después de usar el método create().
#             Su mayor uso es el de permitir que el chat recuerde entradas y salidas anteriores.
#       - content: Indica el contenido del mensaje mandado a ChatGPT.
# - max_tokens: Limita el número máximo de tokens que se devolverán en la salida, los tokens son considerados como 
#   trozos de palabras, donde 1.000 tokens corresponden a unas 750 palabras. Por default el límite es de 4096, por 
#   lo tanto, se pueden recibir y/o devolver como máximo más o menos 3,072 palabras, pero esto varía porque un token
#   no es igual a una palabra, sino a trozos de ellas.
# - temperature: A través de un valor entre 0.0 y 2.0 se controla la creatividad de la respuesta dada. Cuanto más 
#   alto sea el valor, más creativa será la salida, pero si es muy alto la respuesta puede ser muy aleatoria y no 
#   tener sentido. Esto sucede con temperaturas arriba de 1.
# - n: El parámetro n indica el número de respuestas que queremos obtener por cada pregunta.
# - functions: Permite al modelo invocar funciones específicas durante una conversación. Puede utilizar una lista de 
#   variables en formato JSON que definen las funciones y sus parámetros, o una lista de clases que hereden de 
#   pydantic.BaseModel para validar los datos de entrada de las funciones.
#Todos los parámetros se pueden consultar en este enlace: https://platform.openai.com/docs/api-reference/chat/create
completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo", 
    messages = [
        {"role": "user", "content": "Cuéntame un chiste muy gracioso"}
    ],
    max_tokens = 2000,
    temperature = 1.1,
    n = 2
)
#openai.ChatCompletion: El objeto ChatCompletion recibe una lista de mensajes como entrada a través del método 
#create() y devuelve un diccionario generado por el LLM como salida, que se almacena en la posición 0 del parámetro 
#choices, luego dentro del parámetro message existirá el key content y role, el primero describe el mensaje devuelto 
#por ChatGPT, mientras que el segundo describe el rol con el que contestó (que siempre será assistant).
print(completion.choices[0].message.content)





#INTRODUCIR POR MEDIO DE CONSOLA EL ROL DE CHATPGPT Y EL TEXTO QUE QUIERO QUE RESPONDA, ADEMÁS DE QUE ALMACENA 
#SU RESULTADO PARA CREAR UNA CONVERSACIÓN:
#LISTAS: Las listas en Python son tipos de datos estructurados, parecido a lo que son los arrays en otros 
#lenguajes de programación, aunque no es el único tipo de dato agrupado que existe en Python, existen además las 
#tuplas, diccionarios y numpy arrays.
rolMensajesRespuestaChat = []   #Lista que almacenará el rol, mensajes y respuesta de ChatGPT.
#input(): Método que sirve para imprimir en consola un mensaje y que luego se permita al usuario ingresar un valor 
#por consola, que será de tipo String y podrá ser almacenado en una variable.
rolChatGPT = input("Indica a quién quieres que interprete ChatGPT cuando conteste tus preguntas:")
#append(): Método que sirve para agregar valores a una lista, array o diccionario. 
#Al indicarle a ChatGPT el rol que está interpretando no basta con solo decir el nombre de quién es, se debe 
#específicar lo más posible y a mayor detalle a quién está representando y/o qué función va a llevar a cabo durante 
#el chat a través de la siguiente sintaxis:
#Eres un entrevistador de TI que responde de forma muy dura mis contestaciones, Eres el famoso personaje de Marvel 
#Iron Man, Eres la guapísima Alexandra Dadario y estamos en una cita, etc.
rolMensajesRespuestaChat.append({"role": "system", "content": rolChatGPT})      #Rol de ChatGPT al responder.
#print(): Método para imprimir un mensaje en consola y después dar un salto de línea (Enter), además si se quiere 
#concatenar un mensaje (mostrar resultados de variables junto con texto estático), este se debe separar entre 
#comillas o signos de +, declarando los mensajes estáticos entre comillas y los nombres de variables sin comillas.
print("Introduce el mensaje que le quieres hacer al rol de ChatGPT que ingresaste: ")
#Bucle indeterminado while que se ejecuta hasta que lo introducido en consola sea el mensaje Adiosito para cerrar 
#el chat.
preguntaChat = ""           #Variable vacía tipo String.
while(preguntaChat != "Bye"):
    preguntaChat = input()  #Variable que almacena la pregunta introducida en consola.
    rolMensajesRespuestaChat.append({"role": "user", "content": preguntaChat})  #Pregunta del usuario hecha a ChatGPT.
    #openai.ChatCompletion.create(): El método create() aplicado al objeto ChatCompletion perteneciente a la librería 
    #openai se encarga de crear chats que se puedan mandar a ChatGPT. Este recibe los siguientes parámetros:
    # - model: Describe el modelo de lenguaje que se utilizará para generar la salida. Los modelos disponibles son 
    #   gpt-3.5, gpt-4 y el más reciente es gpt-3.5-turbo.
    # - messages: Representa la lista de mensajes que se utilizarán para generar la salida del chat. Cada mensaje es 
    #   un objeto con los siguientes campos:
    #       - role: El rol del mensaje ayuda al modelo de lenguaje a entender el contexto de la conversación. Los 
    #         roles posibles son system, user y assistant, indicándole así de forma separada a quién está 
    #         interpretando ChatGPT para que de esta manera pueda dar respuestas de forma específica:
    #           - system: Por medio de este rol se le indica a ChatGPT a quién está interpretando cuando responda las 
    #             preguntas del usuario.
    #           - user: En este rol se está indicando las preguntas que está realizando el usuario a ChatGPT.
    #           - assistant: Este rol es adoptado por ChatGPT siempre que responda a la pregunta de un usuario y se 
    #             observa en el resultado retornado por el objeto ChatCompletion después de usar el método create().
    #             Su mayor uso es el de permitir que el chat recuerde entradas y salidas anteriores.
    #       - content: Indica el contenido del mensaje mandado a ChatGPT.
    contestacion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = rolMensajesRespuestaChat
    )
    #openai.ChatCompletion: El objeto ChatCompletion recibe una lista de mensajes como entrada a través del método 
    #create() que pueden indicar el rol del Chat y las preguntas que le hace el usuario al modificar su parámetro 
    #role; posteriormente devuelve un mensaje generado por el LLM como salida, que se almacena en la posición 0 del 
    #parámetro choices, dentro de este existirá un key message que a su vez contiene un key content y role, el 
    #primero describe el mensaje devuelto por ChatGPT, mientras que el segundo describe el rol con el que contestó, 
    #que siempre será el de assistant. Esto se puede realizar con alguna de las siguientes sintaxis:
    #   - openai.ChatCompletion.choices[0].message.content.
    #   - openai.ChatCompletion["choices"][0]["message"]["content"]
    #Ambas sintaxis realizan la misma función.
    respuestaChatGPT = contestacion["choices"][0]["message"]["content"]
    #respuestaChatGPT = contestacion.choices[0].message.content
    rolMensajesRespuestaChat.append({"role": "assistant", "content": respuestaChatGPT})
    print("\n" + respuestaChatGPT + "\n")
    """La forma en la que el objeto openai.ChatCompletion devuelve la respuesta del chat es la siguiente:
    {
        #Siempre se usa choices[0], ya que solo tiene una posición y ahí es donde se encuentra message y role.
        "choices": [      
            {
                "finish_reason": "stop",
                "index": 0,
                "message": {
                    "content": "The 2020 World Series was played in Texas at Globe Life Field in Arlington.",
                    "role": "assistant"
                }
            }
        ],
        "created": 1677664795,
        
        "id": "chatcmpl-7QyqpwdfhqwajicIEznoc6Q47XAyW",
        
        "model": "gpt-3.5-turbo-0613",
        
        "object": "chat.completion",
        
        #La forma en la que se cobra al utilizar la API de ChatGPT es a través de Tokens, que son considerados como 
        #trozos de palabras, donde 1.000 tokens corresponden a unas 750 palabras. Esta información también es 
        #devuelta en el resultado del objeto openai.ChatCompletion al utilizar el método create(). Para contar los 
        #tokens de un texto se puede utilizar el siguiente enlace: https://platform.openai.com/tokenizer
        #Y debemos tomar en cuenta que el máximo número de Tokens que se pueden mandar son de 4096, si esto se excede
        #se nos lanzará una excepción.
        "usage": {
            "completion_tokens": 17,
            "prompt_tokens": 57,
            "total_tokens": 74
        }
    }"""