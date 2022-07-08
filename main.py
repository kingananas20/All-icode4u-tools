import colorama
from colorama import Fore
import subprocess 
import time
from time import sleep
import rich
from rich.progress import track
import pyfiglet
colorama.init(autoreset = True)


speed = 0.1
ascii_banner = pyfiglet.figlet_format("Tools")



print(f"{Fore.RED}{ascii_banner} created by kingananas2.0 with tools from icode4u")
print(f"""
What do you wanna use:
{Fore.WHITE}[ {Fore.YELLOW}1 {Fore.WHITE}] Minecraft Server Creater                          credits icode4u   |   improved by kingananas2.0
{Fore.WHITE}[ {Fore.YELLOW}2 {Fore.WHITE}] SpamBot                                           credits icode4u   |   improved by kingananas2.0
{Fore.WHITE}[ {Fore.YELLOW}3 {Fore.WHITE}] YouTube Downloader                                credits icode4u   |   improved by kingananas2.0
{Fore.WHITE}[ {Fore.YELLOW}4 {Fore.WHITE}] Py to exe Converter with icon                     credits icode4u   |   improved by kingananas2.0
{Fore.WHITE}[ {Fore.YELLOW}5 {Fore.WHITE}] Py to exe Converter without a icon                credits icode4u   |   improved by kingananas2.0
{Fore.WHITE}[ {Fore.YELLOW}6 {Fore.WHITE}] Image Downloader                                  credits icode4u   |   improved by kingananas2.0
{Fore.WHITE}[ {Fore.YELLOW}7 {Fore.WHITE}] Url Checker                                       credits icode4u   |   improved by kingananas2.0
""")
start = int(input(f"{Fore.YELLOW}> "))

if start == 1:
    subprocess.call("autoserver.py", shell = True)
elif start == 2:
    subprocess.call("spambot.py", shell = True)
elif start == 3:
    subprocess.call("youtubedownloader.py", shell = True)
elif start == 4:
    subprocess.call("pytoexewithico.py", shell = True)
elif start == 5:
    subprocess.call("pytoexe.py", shell = True)
elif start == 6:
    subprocess.call("imagedownloader.py", shell = True)
elif start == 7:
    subprocess.call("urlchecker.py", shell = True)
else:
    exit

