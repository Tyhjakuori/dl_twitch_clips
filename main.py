import time
from time import sleep
from random import choice
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def random_headers():
    """Returns random choice user-agent"""
    return choice(agents)

# Defining random user-agents
agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']

# Getting channelname
name = input("Channels name: ")
url = "https://www.twitch.tv/"+name+"/clips?filter=clips&range=all"

# Defining a profile
profile = webdriver.FirefoxProfile()
profile.set_preference("dom.webdriver.enabled", False)
profile.set_preference("useAutomationExtension", False)
profile.set_preference("general.useragent.overdrive", random_headers())
profile.update_preferences()

# Defining capabilities
capabilities = DesiredCapabilities.FIREFOX
capabilities['platform'] = "LINUX"
#capabilities['platform'] = "WINDOWS"

# Defining options
options = Options()
#options.add_argument('--headless')
options.add_argument("window-size=1400,600")

driver = webdriver.Firefox(firefox_profile=profile, desired_capabilities=capabilities, options=options)
driver.get(url)
time.sleep(3)

# Clicks players mute button to get window active
body = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/main/div[2]/div[3]/div/div/div[2]/div/div[2]/div/div/div/div/div[5]/div/div[2]/div[1]/div[2]/div/div[1]/button')
body.click()
time.sleep(1)

i = 1
for i in range(200):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    i += 1
    print(i)

# Get page source after everything is loaded in
sorsa = driver.page_source
file1 = open("source.txt", "w")
file1.write(sorsa)
file1.close()
time.sleep(1)

driver.quit()
