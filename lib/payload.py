import random
import sys
from importlib import import_module as imp
from os import path

import lib._errors as _errors
from lib.interacting import Interact
from lib.randoms import random_str
from lib.os_stubs import get_os_stub
from release import version
from ui_core.coloring import Color


PayloadConfigError = _errors.PayloadConfigError
BASIC_LEVEL = "basic"
APACHE_LICENSE = "Apache Software License 2.0"
REQUIRED_VARS = ("name", "version", "author", "description", "payloads")
OPTIONAL_VARS = {"license": APACHE_LICENSE, "required_version": version,
                 "homepage": "", "profile": "", "level": BASIC_LEVEL, 'fields': ["host", "port"], 
                 'fulldescription': "","language": "python", "ext" : ".pyw"
                 }
CONFIG_FILE = "zkit.yml"
CONFIG_FILE_EX = "zkit.yaml"

# relative posix python path
def rpp_path(path):
    return path.replace(sys.path[0].replace('\\', '/'), '').replace('/', '.')[1:-1]
'''
class AntiMalware:
    def __init__(self, file):
        self.file = file
        self.f = open(file, 'r')
        self.fd = self.f.read()
        self.fd = self._remove_comments(self.fd)
        self.check_for_threats()
    @staticmethod
    def _remove_comments(string : str) -> str:
        out = []
        for line in string.split('\n'):
            line += "\n"
            h_pos = line.find('#') 
            if h_pos == -1:
                out.append(line)
            else:
                out.append(line[:h_pos])
        
        return "\n".join(out)[:-1] # striping the end new line
            
    def _check_for_malicious_code(self):
        # with import an attacker can easily import the malicious code
        # or with exec can read the data of the malicious file and execute 
        # if you are a developer user-payload or want to develop one 
        # please put all of your code in one file dont split it in several
        # files     
        if "import" in self.fd or "exec" in self.fd:
            # Hard security
            raise SystemExit(f"{self.file} Is A Possible Malware . (trys attacking you)\n"
                             "Exiting because of your safety. If the payload is yours\n"
                             "avoid using import and exec. or if you have downloaded it from zkit-market\n"
                             "plese report to me to check it and if its a real threat . it will be removed\n")
 
    def _check_for_phishing(self):
        # with print or input they can easily print message that looks
        # like zkits one and steal data from user
        # if you are a developer user-payload or want to develop one 
        # you can get whatever your payload needs with specifing it in zkit.yml
        if "print" in self.fd or "input" in self.fd:
            raise SystemExit(
                             f"{self.file} Is A Possible Phishing Attack.(trys attacking you)\n"
                             "Exiting because of your safety. If the payload is yours\n"
                             "avoid using print and input. or if you have downloaded it"
                             "from zkit-market\n"
                             "plese report to me to check it and if its a real threat"
                             "it will be removed\n")

    def check_for_threats(self)-> bool:
        """Checks for threats in python file . has noreturn if anything was found else returns True

        Args:
            file (str): path to the file to check
        Returns:
            bool: Returns True if nothing was detected . if anything was detected rasies SystemExit
        """
        self._check_for_malicious_code()
        self._check_for_phishing()
        return True
''' # Fix this in new release
class PayloadGenerator(Interact, required_vars=REQUIRED_VARS, optional_vars=OPTIONAL_VARS):
    def __init__(self, root: str):
        self.root = root
        self.root.replace("\\", "/")
        if not self.root.endswith(('\\', "/")):
            self.root += "/"
        self.CONFIG_FILE = path.abspath(self.root + CONFIG_FILE)
        self.CONFIG_FILE_EX = path.abspath(self.root + CONFIG_FILE_EX)
        self.info = self.load_info(self.CONFIG_FILE)
        self.info = self.validate_vars(self.info)
        self.payloads = {}
        for payload in self.info['payloads']:
            
            # AntiMalware(self.root + payload + ".py") It will be uncommeted after fix
            self.payloads[payload] = imp(
                "." + payload, rpp_path(self.root))
    
    def get_random_strs(self, size=4, count=7) -> str:
        return [random_str(size) for _ in range(count)]

    def get_fields(self) -> list:
        return self.info['fields']

    def get_language(self) -> str:
        return self.info['language']

    def handle_version(self):
        if self.info['version'] > version:
            raise PayloadConfigError(f"This payload requires {self.info['version']} or upper but"  
                                     f" your zkit-framework version is {version}"
                                     "Please upgrade your ZKit-Framework using updater.py")


    def _handle_levels(self, payload: str, level: str, platform: str) -> str:
        if level.lower() == "basic":
            # User wants zkit to handle hiding
            hider = get_os_stub(platform.lower(), self.get_language())
            if not hider :
                print("The payload platform is not supported and level is basic ."
                      "if your payloads are for windows linux name them windows.py , linux.py"
                      "if you payloads platforms are not linux or windows please change level to "
                      "advanced"
                      "If the payload is not yours . please report it to developer of it for now zkit will"
                      "ignore it")
                hider = ""
        else :
            hider = ""
            return random.choice(["", "\n", "\n\n"]) +\
                hider + payload + random.choice(["", "\n", "\n\n"])

    def interact(self, data) -> str:
        "Generates the payload"
        info = self.info
        print("\n{} By {}\nDescription : {}\nplease write '-1' for more info".format(
            self.info['name'], info['author'], info['description']))
        if str(input("Or press enter : ")) == "-1":
            [print(Color().RandomColor() + f"{key} : {info[key]}"
                   + Color().GetColor('reset'), end="\n\n") for key in info]

        if len(self.payloads) > 1:
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

        self.strs = self.get_random_strs()
        payload = self.payloads[choice].Payload(*data, self.strs[1:]).create()
        payload = self._handle_levels(payload, info['level'], choice)

        # sweet now payload is generated . lets return the result
        return payload
