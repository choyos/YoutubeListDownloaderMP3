#!/usr/bin/python

# Other typical inputs
import time
import re
import sys
import os

#Always this two imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# BeautifulSoup imports
from bs4 import BeautifulSoup
import requests

###### Get urls from youtube list ######
# Get request to youtube list
req = requests.get("https://www.youtube.com/playlist?list=PLUY0yjvHWf2EWHtfV0x7F6JXpFLbgB_ah")
data = req.text
soup = BeautifulSoup(data, "html.parser")

# Prepare variables for loop
song_links = []
count = 0
first = True

for link in soup.find_all('a'):
	if link.get('href')[:9:1] == "/watch?v=":
		if first == True:
			song_links.append(link.get('href'))
			first = False
		elif link.get('href') != song_links[-1]:
			song_links.append(link.get('href'))
			count += 1
# Remove list link
song_links.pop(0)

for link in song_links:
	print link
'''
# Select browser, url and assert
driver = webdriver.Chrome()
driver.get("http://www.youtube-mp3.org/es")
assert "Convertidor YouTube a mp3" in driver.title

win_handle = driver.current_window_handle
# Make magic
# First page, input youtube query
textinput = driver.find_element_by_id("youtube-url")
textinput.clear()
textinput.send_keys("https://www.youtube.com/watch?v=y8ogicK89T0")
textinput.send_keys(Keys.RETURN)

driver.switch_to_window(win_handle)
# Second page, click "Descargar" url
download_link = driver.find_element_by_link_text("Descargar").click()

#driver.close()
'''
