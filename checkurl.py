import requests
import os

if os.path.exists("statuscodes.txt"):
    os.remove("statuscodes.txt")

with open(r"complete_list.txt", 'r') as file:
	urls = file.read().splitlines()

for url in urls:
    print(f"checking URL: {url}")
    try: 
        response = requests.get('https://' + url, verify=False, timeout=10)
    except:
         continue
    print("should open file")
    with open(r"statuscodes.txt", 'a') as outFile:
        outFile.write(f"{str(response.status_code)};{url}\n")