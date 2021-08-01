## Table of contents
* [Setup](#setup)
* [Usage](#usage)
* [Sources](#sources)


## Setup

To run this you will need selenium, firefox and geckodriver, youtube-dl

You can get geckodriver here: https://github.com/mozilla/geckodriver/releases   
Download release for your operating system, unpack it and move it somewhere where it can be easily added to your path.

You can install selenium with pip (globally):
```
pip install selenium
```
or for current user
```
pip install --user selenium
```
You can get youtube-dl here: https://github.com/ytdl-org/youtube-dl   
And install it via command line:   
```
sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl
```
OR
```
sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl
```
(source youtube-dl [github](https://github.com/ytdl-org/youtube-dl#installation))   
    
Or you can download it via your package manager

## Usage

Run main.py, it will ask which channel you want and then begin rolling throught the page.   
You can adjust number of times it presses page down, with my connection it reached the bottom after 190 presses.   
So default value is set to 200, as then there's a little more room if page doesn't load as fast or something like that.   

After you have the page source i ran it through online html beautifier.   
You will need to change the following:
```
cat cleaned_source | grep 'lines="1"' | tee links1.txt
```
"cleaned_source" was the name i used for the file that came out of online html beautifier, change that to the name you have for that file.
```
cat links1.txt | grep -Po 'href="([^"]*)?filter' | sed -e 's/href="//g' -e 's/?filter//g' -e 's/\/channelname\/clip\///g' | uniq | tee $links
```
You will need to change this parts text "channelname" ("'s/\/channelname\/clip\///g'") to channel which page source you have.   
    
Then execute the bash script to get clip names for urls and start downloading the clips via youtube-dl.
    
## Sources

youtube-dl: https://github.com/ytdl-org/youtube-dl   
geckodriver: https://github.com/mozilla/geckodriver   
selenium: https://github.com/SeleniumHQ/selenium   
