# Vamos a construir un pequeño servicio de mensajería con FastAPI.
# La idea es que se puedan **crear borradores de mensajes** que queden guardados y más adelante puedan ser enriquecidos mediante IA.
# ### Requerimientos generales
# 1. El servicio debe permitir **crear un borrador de mensaje** que incluya:
#     - el cliente al que va dirigido,
#     - el canal (email, sms o whatsapp),
#     - un identificador de template,
#     - contexto del cliente (es buen pagador?, se enoja mucho? es cliente antiguo o nuevo?),
#     - y un conjunto de variables para personalizar el mensaje (fecha de cobro por ejemplo).
# 2. Este borrador debe quedar **guardado en memoria dentro del propio proceso** (por ejemplo, en un diccionario o lista global en el código). Para 
# simplificar el caso, no es necesario persistirlo. Cómo estructures esto (modelos, endpoints, funciones, nombres, etc.) queda a tu criterio.
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any, List

app = FastAPI()

class MessageDraft(BaseModel):
    client: str
    channel: str
    template_id: str
    client_context: str
    variables: Dict[str, Any]

drafts: List[MessageDraft] = []

@app.post("/drafts")
def create_draft(draft: MessageDraft):
    drafts.append(draft)
    return {"message": "Draft created", "draft": draft}

@app.get("/drafts")
def get_drafts():
    return drafts



# Ahora queremos transformar un borrador creado en la Parte 1 en un **mensaje final traducido por un LLM**, y luego enviarlo.
# Disponemos de un conjunto de plantillas base (por ejemplo, mensajes de cobranza) que contienen textos con variables como 
# `{{customer_name}}` y `{{amount}}.`
# - Ejemplos
#     """
#     Hola {{customer_name}}, esperando que estés bien te contacto para
#     recordarte que tienes un pago pendiente de {{amount}} pesos.
#     """
#     """
#     Estimado(a) {{customer_name}}, ya puedes pagar el monto de {{amount}} pesos
#     en nuestra página web. Por favor hazlo lo antes posible para regularizar
#     tu situación.
#     """
#     """
#     Hola {{customer_name}}, te contacto porque tu mensualidad de {{due_date}}
#     ya venció y es necesario que pagues para continuar con el servicio.
#     """
# La tarea es:
# 1. **Tomar un borrador existente en memoria** (por su id) usando la estructura que definiste en la Parte 1.
# 2. **Armar un prompt para un LLM** que:
#     - incluya el texto base del template,
#     - incorpore las variables del borrador,
#     - y pida al modelo redactar un mensaje final listo para enviar en un idioma que el usuario quiera.    
# La finalidad de esto es que podamos enriquecer el mensaje, es decir, dado el template personalizarlo y brindarle un tono 
# para que sea una “cobranza suave” en otro idioma.
# 3. **Simular la llamada al LLM** y obtener un texto final. Puedes usar este request y pedirnos la api key.
# import requests
# import json
# response = requests.post(
#   url="https://openrouter.ai/api/v1/chat/completions",
#   headers={
#     "Authorization": "Bearer <OPENROUTER_API_KEY>",
#     "Content-Type": "application/json",
#     "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
#     "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
#   },
#   data=json.dumps({
#     "model": "google/gemma-3n-e4b-it:free",
#     "messages": [
#       {
#         "role": "user",
#         "content": "<PROMPT>"
#       }
#     ]
#   })
# )
# 4. **Enviar el mensaje final: simular el envío de un mensaje de una forma sencilla** (por ejemplo, una función que reciba canal, 
# destinatario y contenido, imprima el mensaje, y devuelva un estado).
# Eres libre de decidir:
# - cómo construir el prompt,
# - cómo representar las plantillas base (por ejemplo, un diccionario en el código),
# - cómo manejar errores,
# - cómo organizar las funciones,
# - qué forma tiene el “mensaje final”
# - y cómo integras todo el flujo.
# Te recomiendo que pienses en una solución sencilla, nos interesa que nos vayas diciendo que vas pensando.
import requests
@app.post("/generate-message")
def template(template_text, variables):
    final_prompt = template_text.format(**variables)
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "Eres un asistente para enriquecer mensajes y brindarle un tono  para que sea una “cobranza suave” en otro idioma"},
            {"role": "user", "content": final_prompt},
        ]
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post("https://openrouter.ai/api/v1/chat/completions", json = payload, headers = headers)
    return response.json()["choices"][0]["message"]["content"]

template_text =  """Hola {customer_name}, esperando que estés bien te contacto para recordarte que tienes un pago pendiente de {amount} pesos."""
variables = {"customer_name": "juan", "amount": 1500}
final_message = template(template_text, variables)
print(final_message)