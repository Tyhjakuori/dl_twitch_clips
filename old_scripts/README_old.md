## Table of contents
* [Setup](#setup)
* [Usage](#usage)
* [Sources](#sources)


## Setup

To run this you will need selenium, firefox and geckodriver, yt-dlp

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
You can get yt-dlp here: https://github.com/yt-dlp/yt-dlp   
And install it via command line:   
```
sudo curl -L https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -o /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp
```
OR
```
sudo wget https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -O /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp
```
(source yt-dlp [github](https://github.com/yt-dlp/yt-dlp#installation))   
    
Or you can download it via your package manager

## Usage

Run main.py, it will ask which channel you want and then begin rolling throught the page.   
You can adjust number of times it presses page down, with my connection it reached the bottom after 190 presses.   
So default value is set to 200, as then there's a little more room if page doesn't load as fast or something like that.   
   
I've added "top30d.py" file that uses "range=30d" to get the clips from the past month.   
Default value on that is set to "25", during my usage it took 17-20 to get to the bottom of the page.   
   
After you have the page source i ran it through online html beautifier.   
You will need to change the following:
```
cat cleaned_source | grep 'lines="1"' | tee links1.txt
```
"cleaned_source" was the name i used for the file that came out of online html beautifier, change that to the name you have for that file.
```
channelname=
```
You will need to add here the channel which page source you have.   
    
Then execute the bash script to get clip names for urls and start downloading the clips via yt-dlp.
    
## Sources

yt-dlp: https://github.com/yt-dlp/yt-dlp    
geckodriver: https://github.com/mozilla/geckodriver   
selenium: https://github.com/SeleniumHQ/selenium   
