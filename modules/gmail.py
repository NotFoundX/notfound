import smtplib
import config
import time
from colorama import Fore
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(config.correo, config.password)
mensaje = 'From: %s\nTo: %s\n\n' % (config.correo, config.vic)
mensaje += input(Fore.RED + 'INSERTA EL TEXTO >> ')
server.sendmail(config.correo, config.vic,mensaje)
time.sleep(3)
print()
print (Fore.GREEN + 'SUCESSUL DONE!!!')
server.quit()
