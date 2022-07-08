import time
import colorama
import pyautogui
import subprocess
from colorama import Fore
colorama.init(autoreset = True)

msg = input("Message: ")
amt = int(input("Amount: "))

for i in range(amt):
    pyautogui.write(msg)
    pyautogui.press("enter")

print("Spam complete!!")
print(f"""
What do you wanna do?
{Fore.WHITE}[ {Fore.YELLOW}1 {Fore.WHITE}] SpamBot
{Fore.WHITE}[ {Fore.YELLOW}2 {Fore.WHITE}] Go to main
{Fore.WHITE}[ {Fore.YELLOW}3 {Fore.WHITE}] Exit
""")
checker = int(input(f"{Fore.YELLOW}> "))

if checker == 1:
    subprocess.call("spambot.py", shell = True)
elif checker == 2:
    subprocess.call("main.py", shell = True)
else:
    exit
