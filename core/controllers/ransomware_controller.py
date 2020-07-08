import socket
from colorama import Fore
from typing import N

def Connect(self):
    Connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("[" + Fore.LIGHTBLUE_EX + '+' + "]  Making Connection")
    try:
        Victim, Address = Connection.accept()
        Connected = True
        while Connected:
            print(Connection.recv(1024).decode("UTF-8"))
    except:
        Connected = False
        print("[" + Fore.LIGHTRED_EX + '-' +
              "] Connection Failed.Victim Might Be Offline Try Again Later")
        return False
