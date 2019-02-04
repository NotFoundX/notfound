#!/usr/bin/env python
#
#
from colorama import Fore
import time, sys
print (Fore.WHITE + ' _   _  ___ _____   _____ ___  _   _ _   _ ____')
print (Fore.WHITE + '| \ | |/ _ \_   _| |  ___/ _ \| | | | \ | |  _ \ ')
print (Fore.WHITE + '|  \| | | | || |   | |_ | | | | | | |  \| | | | |')
print (Fore.WHITE + '| |\  | |_| || |   |  _|| |_| | |_| | |\  | |_| |')
print (Fore.WHITE + '|_| \_|\___/ |_|   |_|   \___/ \___/|_| \_|____/')
time.sleep(5)
 
def menu():
    print("")
    print (Fore.RED + 'Selecciona una opción')
    print ("")
    print (Fore.GREEN + '1) ???????????????')
    print ("2) ???????????????")
    print ("3) ???????????????")
    print ("4) ???????????????")
    print ("5) ???????????????")
 
 
while True:
    menu()
    print("")
    opcionMenu = input(Fore.YELLOW + 'Elije una opcion >> ')
    
    if opcionMenu =="1":
        print("")
        print(" presionaste la tecla 1")
        time.sleep(5)
        print("")
        print(" HAY QUE CONFIGURAR ESTA OPCION")
        time.sleep(5)
        sys.exit()
    elif opcionMenu =="2":
        print("")
        print(" presionaste la tecla 2")
        time.sleep(5)
        print("")
        print(" HAY QUE CONFIGURAR ESTA OPCION")
        time.sleep(5)
        sys.exit()
    elif opcionMenu =="3":
        print("")
        print(" presionaste la tecla 3")
        time.sleep(5)
        print("")
        print(" HAY QUE CONFIGURAR ESTA OPCION")
        time.sleep(5)
        sys.exit()
    elif opcionMenu =="4":
        print("")
        print(" presionaste la tecla 4")
        time.sleep(5)
        print("")
        print(" HAY QUE CONFIGURAR ESTA OPCION")
        time.sleep(5)
        sys.exit()
    elif opcionMenu =="5":
        print("")
        print(" presionaste la tecla 5")
        time.sleep(5)
        print("")
        print(" HAY QUE CONFIGURAR ESTA OPCION")
        time.sleep(5)
        sys.exit()
    else:
        print(" opcion incorrecta")

