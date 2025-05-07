import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys

def send_email(subject, body):
    sender_email = "rjuandavid2002@gmail.com"
    receiver_email = "rjuandavid2002@gmail.com"
    password = "gdce uvja oaqp ojgr"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    server.sendmail(sender_email, receiver_email, message.as_string())

    server.quit()

if __name__ == "__main__":
    subject = f"Notificación: {sys.argv[1]}"
    body = f"El estado del job es: {sys.argv[2]}\nVer detalles: {sys.argv[3]}"
    send_email(subject, body)
