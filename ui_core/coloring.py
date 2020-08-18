import os
import random
class Color:
    'ANSI Color codes'

    def __init__(self):
        # seperating terminals . Windows and Non-Windows

        if os.name == 'nt':  # i dont know what is the problem of windows that doesnt support ANSI codes
            # Windows
            # related to a zkit project . (making interface look more beautiful)
            self.colors = {
                "black": "\033[90m",
                "red": "\033[91m",
                "green": "\033[92m",
                "yellow": "\033[93m",
                "blue": "\033[94m",
                "magenta": "\033[95m",
                "cyan": "\033[96m",
                "grey": "\033[97m",
                "reset": "\033[0m",
            }
        # because colors are a bit darker in CMD . its better to use LIGHT colors . so they get more colorful

        else:  
            # Non-Windows
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
        if stat == status.lower():
            temp = all_stats[stat].split('|')
            first = col.GetColor(temp[0]) + temp[1] + reset
            break
    if flush:
        flusher = '\r'
    else:
        flusher = ""
    print(f"{flusher}{first}{message}", end=ending)

def get_value(type_, message):
        notify('question', message, '')
        if type_ == list:
            value = str(input("")).split()

        else:
            value = type_(input(""))
        return value

def replace(value, default):
        if value == default[0]:
            if callable(default[1]):
                value = default[1]()
            else:
                value = default[1]
        return value

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
    if default is None:
        default = ['', '']
    value = get_value(type,message)
    value = replace(value, default)


    notify('report', report.replace('\\|', str(value), 1))
    return value
