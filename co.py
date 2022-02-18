from colorama import init
from colorama import Fore, Back, Style
import time
init()
def g(text):
    a=Fore.GREEN+Style.BRIGHT + str(text) + Style.RESET_ALL
    return a
def r(text):
    a=Fore.RED+Style.BRIGHT+str(text)+Style.RESET_ALL
    return a
def cy(text):
    a=Fore.CYAN+Style.BRIGHT+str(text)+Style.RESET_ALL
    return a
def bg(text):
    a = Back.GREEN+Fore.BLACK + Style.BRIGHT + str(text) + Style.RESET_ALL
    return a