import colorama
import virustotal_python
from pprint import pprint
from base64 import urlsafe_b64encode
import subprocess
from colorama import Fore
colorama.init(autoreset = True)

url = input("URL: ")

with virustotal_python.Virustotal("22d84727ea6889265a9f9cbdbf977c42d0908e683aca2bde5ea94dbbf5368fd0") as vtotal:
    try:
        resp = vtotal.request("urls", data={"url": url}, method="POST")
        # Safe encode URL in base64 format
        # https://developers.virustotal.com/reference/url
        url_id = urlsafe_b64encode(url.encode()).decode().strip("=")
        report = vtotal.request(f"urls/{url_id}")
        print(f"""
URL: {report.data["attributes"]["url"]}
Final URL: {report.data["attributes"]["last_final_url"]}
Thread names: {report.data["attributes"]["threat_names"] if report.data["attributes"]["threat_names"] else "None"}
Times submitted {report.data["attributes"]["times_submitted"]}
Response Code: {report.data["attributes"]["last_http_response_code"]}

Votings:
harmless: {report.data["attributes"]["total_votes"]["harmless"]}
malicious: {report.data["attributes"]["total_votes"]["malicious"]}

Scan:
harmless: {report.data["attributes"]["last_analysis_stats"]["harmless"]}
malicious: {report.data["attributes"]["last_analysis_stats"]["malicious"]}
sus: {report.data["attributes"]["last_analysis_stats"]["suspicious"]}
timeout: {report.data["attributes"]["last_analysis_stats"]["timeout"]}
undetected: {report.data["attributes"]["last_analysis_stats"]["undetected"]}
""")
        #pprint(report.data)
    except virustotal_python.VirustotalError as err:
        print(f"Failed to send URL: {url} for analysis and get the report: {err}")

print(f"{url} succesfully checked!!")
print(f"""
What do you wanna do?
{Fore.WHITE}[ {Fore.YELLOW}1 {Fore.WHITE}] Check another url
{Fore.WHITE}[ {Fore.YELLOW}2 {Fore.WHITE}] Go to main
{Fore.WHITE}[ {Fore.YELLOW}3 {Fore.WHITE}] Exit
""")
checker = int(input(f"{Fore.YELLOW}> "))

if checker == 1:
    subprocess.call("urlchecker.py", shell = True)
elif checker == 2:
    subprocess.call("main.py", shell = True)
else:
    exit
