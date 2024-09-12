import openai
from API_Keys.Llaves_ChatGPT_Bard_etc import LlaveChatGPT

openai.api_key = LlaveChatGPT

completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo", 
    messages = [
        {"role": "user", "content": "Cuéntame un chiste muy gracioso"}
    ],
    max_tokens = 2000,
    temperature = 1.1,
    n = 2
)
print(completion.choices[0].message.content)

rolMensajesRespuestaChat = []
rolChatGPT = input("Indica a quién quieres que interprete ChatGPT cuando conteste tus preguntas:")
rolMensajesRespuestaChat.append({"role": "system", "content": rolChatGPT})      
print("Introduce el mensaje que le quieres hacer al rol de ChatGPT que ingresaste: ")
preguntaChat = ""
while(preguntaChat != "Bye"):
    preguntaChat = input()
    rolMensajesRespuestaChat.append({"role": "user", "content": preguntaChat})
    contestacion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = rolMensajesRespuestaChat
    )
    respuestaChatGPT = contestacion["choices"][0]["message"]["content"]
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