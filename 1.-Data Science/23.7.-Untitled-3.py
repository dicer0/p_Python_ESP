import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import time

def send_email():
    message = MIMEMultipart()
    print(message)
    sender_email = "tucorreo@gmail.com"
    receiver_email = "destinatario@gmail.com"
    password = "tucontraseña"

    subject = "Asunto del correo"
    body = "Contenido del correo"
    
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    print(message)
    message.attach(MIMEText(body, "plain"))

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
            time.sleep(5)
            print("Intento número", intentosEmail, "de mandar el correo...")
            intentosEmail += 1

send_email_at_specific_time(1, 55)