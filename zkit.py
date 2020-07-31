"ZKit-Framework Github : https://github.com/000Zer000/ZKit-Framework"
# Copyright (c) 2020, Zer0 . All rights reserved.
# This Work Is Licensed Under Apache Software License 2.0 More
# Can Be Found In The LICENSE File.
__author__ = "Zer0"
__github__ = "https://github.com/000Zer000/ZKit-Framework"
__version__ = "1.3.5"
__license__ = "Apache Software License 2.0"
__status__ = "Production"

def start():
    try:
        # Doing some imports
        from os import popen, path, name as os_name, system
        import core.helper_core
        from core.helper_core import notify, Color, generate, dos, ctrler, helpbanner, init, print_banner
    except (ImportError,ModuleNotFoundError) as value:
        # Ops ! Sth is missing

        print(
            "One Or Some On Requirments Not Found . Please Install Them And Try Again ."
            + "Python Threw : "
            + str(value)
        )
        raise 

    # Printing A Banner More Coming Soon
    black, red, green, yellow, blue, magenta, cyan, grey, reset = Color().GetAllColors()
    init()
    print_banner()
    # Hard And Boring Code
    print(
        "\t \t \t \t \t    Hacking is" + red + " C " + green + "O " + blue + "L " +
        yellow + "O " + magenta + "R " + green +
        "F " + red + "U " + magenta + "L " + reset
    )
    print(
        "Available Options Are or Enter '?' To get a summery about notes of using this framework:\n" "* = Not Supported right now\n"
        + red + "  {1} --> Create A RootKit\n"
        + green + "  {2} --> Create A Ransomware *\n"
        + blue + "  {3} --> Create A KeyLogger *\n"
        + yellow + "  {4} --> Run A Dos Attack\n"
        + magenta + "  {5} --> Connect To A Victim\n"
        + cyan + "  {000}" + "--> Exit ZKit-Framework\n" + reset
    )
    while True:
        try:
            CHOICE = str(input("..> "))

            if CHOICE == "000":
                break
            elif CHOICE == "?":
                print(helpbanner)
            elif CHOICE == "1":
                generate("rootkit")
            elif CHOICE == "4":
                dos.main()
            elif CHOICE == "5":
                ctrler.main()
            elif CHOICE != None:
                notify(
                    "problem", "Invalid Input {" + "{}".format(CHOICE) + "}")
        except (KeyboardInterrupt, EOFError):
            try :
                print("\nPlease Type '000' To Exit ZKit-Framework\n")
                CHOICE = None
            except(KeyboardInterrupt, EOFError):
                pass
start()