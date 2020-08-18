"ZKit-Framework Github : https://github.com/000Zer000/ZKit-Framework"
# Copyright (c) 2020, Zer0 . All rights reserved.
# This Work Is Licensed Under Apache Software License 2.0
# More Can Be Found In The LICENSE File.
__author__ = "Zer0"
__license__ = "Apache Software License 2.0"
__status__ = "Production"
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
try:
    # Doing some imports
    from ui_core.coloring import notify, Color
    from ui_core._core import Generate, init, print_banner, crash_handler
    from ui_core.payload_helper import list_builtin_payloads, search_for_payloads, list_payloads
    import ui_core.controller as ctrler
    from release import version
    from lib._errors import BackToMainMenu
    import ui_core.dos as dos
    from updater import API as updater
except (ImportError, ModuleNotFoundError) as e:
    # Ops ! Sth is missing

    print(
        "One Or Some On Requirments Not Found . Please Install Them And Try Again ."
        + "Python Threw : "
        + str(e)
    )
    raise

__version__ = version

def list_builtin_payloads_helper(type_):
    payloads = list_builtin_payloads(type_)
    index = input("")
    if index == "000":
        raise BackToMainMenu
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
        if index == "000":
            raise BackToMainMenu
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
        print("\t " * 5 + f"Hacking is {red}C {green}O {blue}L {yellow}O {magenta}R {green}F {red}U {magenta}L {reset}")
        print("Available options:\n"
              f"{red}{{1}} --> Create a rootKit\n"
              f"{green}{{2}} --> Create a ransomware\n"
              f"{blue}{{3}} --> Create a keyLogger \n"
              f"{yellow}{{4}} --> Run a DOS attack\n"
              f"{magenta}{{5}} --> Connect to a victim\n"
              f"{red}{{6}} --> Generate your user payloads\n"
              f"{cyan}{{000}} --> Exit ZKit-Framework\n{reset}")

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
                "problem", f"Invalid Input '{choice}'")

    def main_loop(self):
        try:
         while True:

            choice = str(input("..> "))

            if choice == "000":
                break
            self.execute(choice)
        except BackToMainMenu:
            self.main_loop()


starter = Start()
try:
    starter.main_loop()
except (KeyboardInterrupt, EOFError):
    print("\nPlease Type '000' To Exit ZKit-Framework\n")
except BaseException as e:
    crash_handler(e)