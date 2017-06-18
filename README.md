# YoutubeListDownloaderMP3
Program to automatically download whole list of youtube in mp3.

<h1>Working</h1>
It must be launch by command line:
	<pre>/download_path/./main</pre>

<h1>How does it works</h1>
When you give a YouTube list link to this program, it would launch an Google Chrome session. 
The program will access to the website <pre>http://www.youtube-mp3.org/es</pre>.
Then automatically, it would give to this site the links of the songs of the list you enter, one by one. 
All this songs would be donwload in your "Download" folder. 
If there were songs not available to donwload, it would print the list of names of this songs when it finished.

<h1>Requirements</h1>
<h2>Operative systems</h2>
Now it is only working on LINUX (Ubuntu, Debian...)
<h2>Browser</h2>
You must have installed Google Chrome, and you have to let that 
<h2>Dependencies</h2>
You must have in system installed the following packages:
<pre>python-bs4; python-selenium; chromium-chromedriver; </pre>
But you can easyly install them:
<pre>sudo apt-get install python-bs4 python-selenium chromium-chromedriver</pre>

<h1>Spotify list downloading</h1>
For Spotify list downloading, you must convert this list to a youtube list in order to get then the list link.
There are many options in Google, but I suggest: 
<a href="http://www.playlistbuddy.com">http://www.playlistbuddy.com</a>
In this site, you can login with your Spotify user and select any of your list to convert it in a YouTube list.
Then you can use this program in order to get all mp3 songs.