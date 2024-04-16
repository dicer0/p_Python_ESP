# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime
import time

def send_email():
    message = MIMEMultipart()
    sender_email = "diego-rko@live.com.mx"
    password = "tucontraseña"
    receiver_email = "diego-rko@live.com.mx"
    subject = "Olis crayolis automatizado"
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    
    body = "Contenido del correo"
    emailPlainContent = MIMEText(_text = body, _subtype = "plain", _charset = "utf-8")
    message.attach(emailPlainContent)

    try:
        with smtplib.SMTP("smtp-mail.outlook.com", 587) as server:
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

send_email_at_specific_time(14, 11)


import socket
def test_port_connection(host, port):
    try:
        # Create a TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout for connection attempt (adjust as needed)
        sock.settimeout(2)
        # Attempt to connect to the host and port
        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"Success: Port {port} is open on {host}")
        else:
            print(f"Failed: Port {port} is not open on {host}")
        sock.close()
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# Replace "example.com" and the port numbers with the ones you want to test
test_port_connection("https://dicer0.com/", 80)  # Test HTTP port
test_port_connection("https://dicer0.com/", 443)  # Test HTTPS port
test_port_connection("smtp.office365.com", 587)  # Test SMTP port for Office365