import sys, os
import banner
from colorama import Fore
print()
def menu():
    print (Fore.YELLOW + '1) CONTINUE')
    print()
    print (Fore.GREEN + '2) SMTPAuthenticationError (SOLUTION) ')

while True:
    menu()
    print("")
    opcionMenu = input(" Choose an Option >> ")
    print("")
    if opcionMenu =="1":
        print("")
        os.system('clear')
        os.system("python modules/gmail.py")
    elif opcionMenu =="2":
        print("")
        os.system('clear')
        os.system("python modules/ERROR.py")
    else:
        print ("Option not valide")
