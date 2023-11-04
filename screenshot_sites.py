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


#def __main__():
#    screenshot(f"https://adressesok.posten.no")

#__main__()