from enum import auto
import requests
import subprocess
import colorama
from colorama import Fore
colorama.init(autoreset = True)

url = input("Paste the url in here: ")
name = input("Filename: ")

r = requests.get(url)

print(r.content)
with open(f"{name}.png", "wb") as f:
    f.write(r.content)

print(f"{Fore.GREEN}Succesfully downloaded {name}.png!!")

print(f"""
What do you wann do?
{Fore.WHITE}[ {Fore.YELLOW}1 {Fore.WHITE}] Download other image
{Fore.WHITE}[ {Fore.YELLOW}2 {Fore.WHITE}] Go to main
{Fore.White}[ {Fore.YELLOW}3 {Fore.WHITE}] Exit
""")
checker = int(input(f"{Fore.YELLOW}> "))

if checker == 1:
    subprocess.call("imagedownloader.py", shell = True)
elif checker == 2:
    subprocess.call("main.py", shell = True)
else:
    exit