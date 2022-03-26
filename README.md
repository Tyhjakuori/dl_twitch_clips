## Table of contents
* [Setup](#setup)
* [Usage](#usage)
* [Sources](#sources)


## Setup

This hasn't been tested on other platforms than linux (Artix), but i will test and create scripts (if needed) for mac and windows later when i got some free time.   
If someone wants to do that, feel free to create a pull request.   

To run this you will need selenium, firefox and geckodriver, yt-dlp, lxml and BeautifulSoup

You can get geckodriver here: https://github.com/mozilla/geckodriver/releases   
Download release for your operating system, unpack it and move it somewhere where it can be easily added to your path.
I have it located in "/usr/bin/" directory.   

I've included python packages and their current version as of writing this in requirements.txt file. You can install them via the file:
```
pip install -r requirements.txt
```
for current user
```
pip install -r requirements.txt --user
```
Or you can get required packages the way you prefer.   

## Usage

Run main.py and it will ask which channel you want and then begin rolling throught the page.   
You can adjust number of times it presses end, with my connection it reached the bottom after about 40 presses.   
So default value is set to 50, as then there's a little more room if page doesn't load as fast or something like that.   
It will create a folder named as "clips_channelnameYouGave" in current directory to contain the clips and txt file containing all clip codes.  
It uses yt-dlp to download clips it found and saves those in mp4 format.   
   
"top30d.py" will work same as "main.py" but instead of all clips it will get clips from past 30 days.   
It will use the same folder created by "main.py" if used before or it will create same named folder specified earlier.   
Default value on that is set to "10", during my usage it took 5-7 to get to the bottom of the page.   
    
## Sources

yt-dlp: https://github.com/yt-dlp/yt-dlp    
geckodriver: https://github.com/mozilla/geckodriver   
selenium: https://github.com/SeleniumHQ/selenium  
Beautiful Soup: https://www.crummy.com/software/BeautifulSoup/, https://www.crummy.com/software/BeautifulSoup/bs4/doc/   
lxml: https://github.com/lxml/lxml, https://lxml.de/
