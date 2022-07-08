import os 
import shutil
import time
import subprocess
from colorama import Fore
import colorama
colorama.init(autoreset = True)

print("Drag and drop your python file in here!")
pyPath = input()
print("Drag and drop your icon in here!!")
ico = input()
os.system(f"pyinstaller --onefile -w {pyPath} --ico {ico}")
time.sleep(2)
os.remove("main.spec")
shutil.rmtree("build")
print("Succesfully converted to exe!!")
print(f"""
What do you wanna do?
{Fore.WHITE}[ {Fore.YELLOW}1 {Fore.WHITE}] Go back to main
{Fore.WHITE}[ {Fore.YELLOW}2 {Fore.WHITE}] Convert py to exe
{Fore.WHITE}[ {Fore.YELLOW}3 {Fore.WHITE}] Exit
""")
checker = int(input(f"{Fore.YELLOW}> "))

if checker == 1:
    subprocess.call("main.py", shell = True)
elif checker == 2:
    subprocess.call("pytoexewithico.py", shell = True)
else:
    exit