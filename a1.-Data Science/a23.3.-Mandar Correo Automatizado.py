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

#smtplib: La librería sirve para enviar correos a través del protocolo SMTP (Simple Mail Transfer Protocol), lo 
#cual implica primero establecer una conexión con un servidor de email y luego enviar el correo electrónico a 
#través de dicho servidor. Esta conexión se realiza utilizando un nombre de host y un puerto específico.
import smtplib
#email: Esta librería proporciona una serie de clases para construir, analizar, manipular, codificar, 
#decodificar y demás operaciones realizadas con correos electrónicos.
#email.mime.text - MIMEText: La clase MIMEText del paquete mime.text perteneciente a la librería email sirve 
#para crear y manipular partes de un mensaje de correo electrónico que contienen texto plano. 
from email.mime.text import MIMEText
#email.mime.multipart - MIMEMultipart: La clase MIMEMultipart del paquete mime.multipart perteneciente a la 
#librería email sirve para trabajar con las partes de un email que no sean texto plano, lo que permite enviar 
#mensajes más complejos que incluyan texto, archivos adjuntos, imágenes u otros tipos de contenido.
from email.mime.multipart import MIMEMultipart
import datetime #datetime: Librería que proporciona método para trabajar con fechas y horas en Python.
import time     #time: Librería del manejo de tiempos, como retardos, contadores, etc.

#FUNCIÓN PARA MANDAR UN EMAIL:
def send_email():
    #MIMEMultipart(): Este método constructor no recibe ningún parámetro, pero sirve para crear un objeto en 
    #forma de diccionario que represente un mensaje de correo electrónico multipartito (que puede incluir texto, 
    #archivos adjuntos, imágenes u otros tipos de contenido) y los valores que reciben las claves (keys) del 
    #diccionario en forma de parámetro son los siguientes:
    # - MIMEMultipart()["From"]: Representa el remitente del correo electrónico, osea el que lo envía.
    # - MIMEMultipart()["To"]: Es el destinatario o destinatarios del correo electrónico.
    # - MIMEMultipart()["Cc"]: Son los destinatarios en copia (CC) del correo electrónico.
    # - MIMEMultipart()["Bcc"]: Son los destinatarios en copia oculta (BCC) del correo electrónico.
    #       - Si se envía el correo a distintos destinatarios, dependiendo del servidor de correo electrónico 
    #         y del cliente utilizado para visualizar el mensaje se pueden usar comas (,) o punto y coma (;) 
    #         para indicar los distintos destinatarios.
    # - MIMEMultipart()["Subject"]: Representa el asunto del correo electrónico.
    #Se indican de esta forma los parámetros del objeto MIMEMultipart() porque este es un diccionario y se le 
    #están asignando valores a sus keys.
    message = MIMEMultipart()
    #MI CORREO, MI CONTRASEÑA, EL DESTINATARIO Y EL ASUNTO DEL CORREO SE INDICAN EN FORMA DE STRING:
    sender_email = "dcervantesr1401@alumno.ipn.mx"  #Mi correo:                     tucorreo@gmail.com
    password = "tucontraseña"                       #Mi contraseña:                 tucontraseña
    receiver_email = "diego-rko@live.com.mx"        #Correo a quién se le envía:    destinatario@gmail.com
    subject = "Olis crayolis automatizado"
    #ASIGNACIÓN DE REMITENTE, DESTINATARIO Y ASUNTO AL OBJETO MIMEMultipart:
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    
    #CONTENIDO DEL CORREO:
    body = "Contenido del correo"
    #MIMEText(): 
    emailPlainContent = MIMEText(_text = body, _subtype = "plain", _charset = "utf-8")
    message.attach(emailPlainContent)

    #MANEJO DE EXCEPCIONES: Es una parte de código que se conforma de 2 o3 partes, try, except y finally: 
    # - Primero se ejecuta el código que haya dentro del try, y si es que llegara a ocurrir una excepción 
    #   durante su ejecución, el programa brinca al código del except.
    # - En la parte de código donde se encuentra la palabra reservada except, se ejecuta cierta acción cuando 
    #   ocurra el error esperado.
    # - Por último, cuando no ocurra una excepción durante la ejecución del gestor de excepciones, se ejecutará 
    #   el código que esté incluido dentro del finally después de haber terminado de ejecutar lo que haya en el 
    #   try, pero si ocurre una excepción, la ejecución terminará cuando se llegue al except.
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Correo electrónico enviado correctamente.")
    except Exception as e:
        print(f"Error al enviar el correo electrónico: {e}")


def send_email_at_specific_time(hour, minute):
    intentosEmail = 0
    while True:
        now = datetime.datetime.now()
        if now.hour == hour and now.minute == minute:
            send_email()
            break
        else:
            time.sleep(5)  #Comprueba cada 5 segundos
            print("Intento número", intentosEmail, "de mandar el correo...")
            intentosEmail += 1

# Uso: Enviar correo a las 10:30 AM
send_email_at_specific_time(2, 26)