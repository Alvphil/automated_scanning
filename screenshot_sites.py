from selenium import webdriver
from time import sleep

#with open(r"statuscodes.txt", 'r') as file:
#    lines = file.read().splitlines()

def screenshot(url):
    driver = webdriver.Firefox()    
    driver.get(f"{url}")
    sleep(2)
    tmp = url.split("://")
    driver.get_screenshot_as_file(f"./screenshots/{tmp[1]}.png")
    driver.quit()


def main():
    with open(r"statuscodes copy.txt", 'r') as file:
        lines = file.read().splitlines()
    
    for line in lines:
        url = line.split(";")
        if url[0] == "200":
            print(url[1])
            try:
                screenshot(url[1])
            except:
                continue

if __name__ == "__main__":
    main()