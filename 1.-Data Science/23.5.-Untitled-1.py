import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def send_email_with_attachment():
    sender_email = "diego-rko@live.com.mx"
    receiver_email = "diego-rko@live.com.mx"
    subject = "Olis crayolis automatizado"
    body = "Contenido del correo"
    attachment_path = "C:/Users/diego/OneDrive/Documents/The_MechaBible/p_Python_ESP/1.-Data Science/0.-Archivos_Ejercicios_Python/23.-GUI PyQt5 Conexion DataBase/23.-Reporte Analisis de Datos 2.xlsx"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    # Open the file in binary mode
    with open(attachment_path, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {os.path.basename(attachment_path)}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    try:
        # Log in to SMTP server and send email
        with smtplib.SMTP("smtp.office365.com", 587) as server:
            server.starttls()
            # Replace 'password' with your corporate email password or app password
            server.login(sender_email, "password")
            server.sendmail(sender_email, receiver_email, text)
        print("Email sent successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

send_email_with_attachment()