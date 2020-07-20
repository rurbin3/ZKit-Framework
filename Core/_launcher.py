"Instead of having lots of lines of code in zkit.py diffrent files in launcher_core"


def start():
    try:
        # Doing some imports
        from os import popen, path, name as os_name, system
        from Core import Notify, Color, Generate, Dos, Ctrler, HelpBanner, Init, PrintBanner
    except ImportError as value:
        # Ops ! Sth is missing

        print(
            "One Or Some On Requirments Not Found . Please Install Them And Try Again ."
            + "Python Threw : "
            + str(value)
        )
        raise SystemExit

    # Printing A Banner More Comming Soon
    black, red, green, yellow, blue, magenta, cyan, grey, reset = Color().GetAllColors()
    Init()
    PrintBanner()
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
                print(HelpBanner)
            elif CHOICE == "1":
                Generate("rootkit")
            elif CHOICE == "4":
                Dos.main()
            elif CHOICE == "5":
                Ctrler.main()
            elif CHOICE != None:
                Notify(
                    "problem", "Invalid Input {" + "{}".format(CHOICE) + "}")
        except (KeyboardInterrupt, EOFError):
            try :
                print("\nPlease Type '000' To Exit ZKit-Framework\n")
                CHOICE = None
            except(KeyboardInterrupt, EOFError):
                pass
