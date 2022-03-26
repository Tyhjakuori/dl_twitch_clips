import os
import time
from time import sleep
from random import choice
from yt_dlp import YoutubeDL
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def random_headers():
    """Returns random choice user-agent"""
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
    return choice(agents)


# Getting channelname
name = input("Channels name: ")
url = "https://www.twitch.tv/{}/clips?filter=clips&range=all".format(name)

# Defining a profile
capabilities = DesiredCapabilities.FIREFOX
capabilities['platform'] = "LINUX"
# capabilities['platform'] = "WINDOWS"

# Defining options
options = Options()
# options.add_argument('--headless')
options.add_argument("window-size=1400,600")
options.set_preference("dom.webdriver.enabled", False)
options.set_preference("useAutomationExtension", False)
options.set_preference("general.useragent.overdrive", random_headers())

driver = webdriver.Firefox(capabilities=capabilities, options=options)

original_path = os.getcwd()
new_path = "./clips_{}".format(name)
if not os.path.exists(new_path):
    os.makedirs(new_path)
os.chdir(new_path)

removal_list = ["/{}/clip/".format(name), "?filter=clips&range=all&sort=time"]

driver.get(url)
time.sleep(3)

# Clicks players mute button to get window active
body = driver.find_element(By.XPATH, '/html/body')
body.click()
time.sleep(1)

i = 1
for i in range(50):
    body.send_keys(Keys.END)
    time.sleep(1)
    i += 1
    print(i)

# Get page source after everything is loaded in
sorsa = driver.page_source
soup = BeautifulSoup(sorsa, 'lxml')
driver.quit()
links1 = soup.select('a[href^=\/{}\/clip\/]'.format(name))

clip_list = []

with open('clips_{}.txt'.format(name), 'w') as clip_file:
    for clip_name in links1:
        clip_name = clip_name.attrs['href']
        for word in removal_list:
            clip_name = clip_name.replace(word, '')
        if clip_name not in clip_list:
            clip_list.append(clip_name)
            clip_file.write("{}\n".format(clip_name))
o = 1
total_clips = len(clip_list)
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best'}
with YoutubeDL(ydl_opts) as ydl:
    for dl_clip in clip_list:
        print("> Downloading {} out of {}".format(o, total_clips))
        ydl.download(['https://clips.twitch.tv/{}'.format(dl_clip)])
        o += 1

os.chdir(original_path)
