import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys

def send_email(subject, body):
    sender_email = "rjuandavid2002@gmail.com"
    receiver_email = "rjuandavid2002@gmail.com"
    password = "gdce uvja oaqp ojgr"

    # Configurar el servidor SMTP
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)

    # Construir el mensaje
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Agregar cuerpo del correo
    message.attach(MIMEText(body, "plain"))

    # Enviar el correo
    server.sendmail(sender_email, receiver_email, message.as_string())

    # Cerrar la conexión
    server.quit()

if __name__ == "__main__":
    subject = f"Notificación: {sys.argv[1]}"  # Job Name (success, fail, etc.)
    body = f"El estado del job es: {sys.argv[2]}\nVer detalles: {sys.argv[3]}"
    send_email(subject, body)
