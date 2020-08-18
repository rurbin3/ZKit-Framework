###################################
# Version
###################################

version_major = '1'
version_minor = '4'
version_patch = '9'

version_as_list = [version_major,version_minor,version_patch]
version = '.'.join(version_as_list)

__version__ = version
###################################
# Updater's Needed Info
###################################

files = ["CHANGELOG", "CODE_OF_CONDUCT.md", "CONTRIBUTING.md", "Errors.log", "LICENSE", 
         "README.md", "SECURITY.md", "requirements.txt", "updater.py", "zkit.py", "release.py"]
dirs = ['ui_core', 'lib', '.github']

###################################
# Python Payloads
###################################
py_payloads = 18

py_rootkits = 8
py_keyloggers = 6
py_ransomware = 4


#XXX These info below are not for now . maybe used later
###################################
# Ruby Payloads
###################################
rb_payloads = 0

rb_rootkits = 0
rb_keyloggers = 0
rb_ransomwares = 0

####################################
# General Info
####################################
payloads = py_payloads + rb_payloads

###################################
# Payload's Info
###################################
rootkits = py_rootkits + rb_rootkits
keyloggers = py_keyloggers + rb_keyloggers
ransomwares = py_ransomware + rb_ransomwares

####################################
# Other Info
####################################
encryption_methods = 2
dos_methods = 4