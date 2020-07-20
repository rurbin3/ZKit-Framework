import random
def random_string(size=4):
    """
    Generates A Random String with given size.
    Arguments :
         size (int) : is optional can be omitted . if omitted size is 4
    Returns a random string with lenght of Argument size
    example :
        random_string(2)
        returns [A-Z a-z][A-Z a-z]
    in simple : two letters that can be
        either lowercase or uppercase like : Aa or bZ or bz or Bz or BZ
        or if you increase the lenght it would be longer
    """
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(size))

def random_int(min_: int, max_: int):

    """
    generates a random int in a given range (min_...max_)  
    max_ and min_ must be integer


    Arguments:
        min_ (int) : minimum generated int
        max_ (int) : maximum generated int

    Returns result (int) =  a random int

    example :
        random_int(1 , 3)
        returns 1 or 2 or 3
    """
    return int(random.choice(range(min_, max_+1)))

def random_ip():
    """
    builds a random ip . it may not exist .

    Returns:
        ip (str) : a random ip in correct form
    example :
        123.233.5.11
    """
    return  str(random_int(20, 255)) + "." + str(random_int(15, 255)) + "." + \
        str(random_int(6, 255)) + "." + str(random_int(1, 255))