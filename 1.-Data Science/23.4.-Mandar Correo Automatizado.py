# Programa para enviar un correo electrónico a una hora específica
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import time

def send_email():
    sender_email = "tucorreo@gmail.com"
    receiver_email = "destinatario@gmail.com"
    password = "tucontraseña"

    subject = "Asunto del correo"
    body = "Contenido del correo"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def send_email_at_specific_time(hour, minute):
    while True:
        now = datetime.datetime.now()
        if now.hour == hour and now.minute == minute:
            send_email()
            break
        else:
            time.sleep(30)  # Comprueba cada 30 segundos

# Uso: Enviar correo a las 10:30 AM
send_email_at_specific_time(10, 30)