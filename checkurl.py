import requests, concurrent.futures, os, urllib3


urllib3.disable_warnings()

if os.path.exists("statuscodes.txt"):
    os.remove("statuscodes.txt")

with open(r"complete_list.txt", 'r') as file:
	urls = file.read().splitlines()

# url_checker checks the respons from sites in the complete_list and writes the status code it receives back from the server to a file.
def url_checker(url):
    print(f"checking URL: {url}")
    try: 
        response = requests.get('https://' + url, allow_redirects=True, timeout=5, verify=False)
    except requests.exceptions.RequestException:
        try: 
            response = requests.get('http://' + url, allow_redirects=True, timeout=10)
        except requests.exceptions.RequestException:
             return
    with open(r"statuscodes.txt", 'a') as outFile:
        outFile.write(f"{str(response.status_code)};{url}\n")

def main():
    # using multiple threads to look through the list of domains. 
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as exeutor:
         exeutor.map(url_checker, urls)

    

main()