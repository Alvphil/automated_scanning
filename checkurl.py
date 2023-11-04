import requests, concurrent.futures, os, urllib3
from datetime import date, time, datetime
import screenshot_sites

urllib3.disable_warnings()

if os.path.exists("statuscodes.txt"):
    os.remove("statuscodes.txt")

with open(r"complete_list.txt", 'r') as file:
    urls = file.read().splitlines()

# url_checker checks the respons from sites in the complete_list and writes the status code it receives back from the server to a file.
def url_checker(url):
    print(f"checking URL: {url}")
    protcol = ""
    try: 
        protcol = "https://"
        response = requests.get(protcol + url, allow_redirects=True, timeout=5, verify=False)
    except requests.exceptions.RequestException:
        try: 
            protcol = "http://"
            response = requests.get(protcol + url, allow_redirects=True, timeout=10)
        except requests.exceptions.RequestException:
             return
    response_code = f"{str(response.status_code)};{protcol}{url}"
    return response_code

def sort_file():
    with open(r"statuscodes_u.txt", 'r') as file:
        urls = file.read().splitlines()
    sorted_urls = sorted(urls)

    with open(r"statuscodes.txt", 'a') as outFile: #adding date to the top of the file.
        outFile.write(f"{datetime.today()}\n\n")
    for url in sorted_urls:
        with open(r"statuscodes.txt", 'a') as outFile:
            outFile.write(f"{url}\n")
    if os.path.exists("statuscodes_u.txt"):
        os.remove("statuscodes_u.txt")

def main():
    sites_array = []
    # using multiple threads to look through the list of domains. 
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as exeutor:
        for tmp in exeutor.map(url_checker, urls):
            if tmp is not None:
                sites_array.append(tmp)
    
    sorted_array = sorted(sites_array)
    for url in sorted_array:
        with open(r"statuscodes.txt", 'a') as outFile:
            outFile.write(f"{url}\n")
    for line in sorted_array:
        url = line.split(";")
        if url[0] == "200":
            try:
                screenshot_sites.screenshot(url[1])
            except:
                continue



    

main()