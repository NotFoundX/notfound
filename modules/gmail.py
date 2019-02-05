import smtplib
import config
import time
from email.mime.text import MIMEText
from colorama import Fore
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(config.correo, config.password)
mensaje = input(Fore.GREEN + 'INSERT EL TEXTO >> ')
print()
mime_message = MIMEText(mensaje, "plain", _charset="utf-8")
mime_message["From"] = config.correo
mime_message["To"] = config.vic
mime_message["Subject"] = input(Fore.GREEN + 'INSERT ASUNT >> ')
server.sendmail(config.correo, config.vic, mime_message.as_string())
time.sleep(3)
print()
print (Fore.GREEN + 'SENT WITH SUCCESS!!!')
server.quit()
