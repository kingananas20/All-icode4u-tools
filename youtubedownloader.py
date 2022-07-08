from time import time
import colorama
import pytube 
from pytube import YouTube
import rich
from rich.progress import track
import time
from time import sleep
import subprocess
from colorama import Fore
colorama.init(autoreset = True)

def start():
    sleep(0.1)

link = input("Url: ")
yt = YouTube(link)

ys = yt.streams.get_highest_resolution()
for _ in track(range(100), description='[green]Downloading...'):
    start()
ys.download()
print("Download Complete!")
print(f"""
What do you wanna use?
{Fore.WHITE}[ {Fore.YELLOW}1 {Fore.WHITE}] Download Youtube Video
{Fore.WHITE}[ {Fore.YELLOW}2 {Fore.WHITE}] Go to main
{Fore.WHITE}[ {Fore.YELLOW}3 {Fore.WHITE}] Exit
""")
checker = int(input(f"{Fore.YELLOW}> "))

if checker == 1:
    subprocess.call("youtubedownloader.py", shell = True)
elif checker == 2:
    subprocess.call("main.py", shell = True)
else:
    exit
