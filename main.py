#!/usr/bin/python

# Typical imports
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

list_link = raw_input('Inserte url de lista de youtube a descargar (pegar con Ctrl+Shit+V o con click derecho:\n')

# Get request to youtube list
req = requests.get(list_link)
data = req.text
soup = BeautifulSoup(data, "html.parser")

# Prepare variables for loop
song_links = []
first = True
header = "www.youtube.com"

for link in soup.find_all('a'):
	if link.get('href')[:9:1] == "/watch?v=":
		if first == True:
			song_links.append(link.get('href'))
			first = False
		elif link.get('href') != song_links[-1][len(header)::]:
			song_links.append(header + link.get('href'))

# Remove list link and first link of page list image
song_links.pop(0)
song_links.pop(0)

'''
for link in song_links:
	print link.split('&')[0]
'''

# Select browser (Chrome), url(mp3 downloader page) and assert(check everything right)
driver = webdriver.Chrome()
driver.get("http://www.youtube-mp3.org/es")
assert "Convertidor YouTube a mp3" in driver.title

# Get current handle to avoid pop-ups

# Make magic
not_downloaded = []

for link in song_links:
	try:
		textinput = driver.find_element_by_id("youtube-url")
		textinput.clear()
		textinput.send_keys(link.split('&')[0])
		textinput.send_keys(Keys.RETURN)

		time.sleep(2)
		
		download_link = driver.find_element_by_link_text("Descargar").click()

	except Exception as e:
		not_downloaded.append(link)
		driver.refresh()

	time.sleep(1)

not_not_downloaded = []

if len(not_downloaded) > 0:
	print "Hubo un problema y algunas no se descargaron."
	print "Vamos a intentar volver a descargarlas de nuevo"
	for link in not_downloaded:
		try:
			textinput = driver.find_element_by_id("youtube-url")
			textinput.clear()
			textinput.send_keys(link.split('&')[0])
			textinput.send_keys(Keys.RETURN)

			time.sleep(2)
			
			download_link = driver.find_element_by_link_text("Descargar").click()

		except Exception as e:
			not_not_downloaded.append(link)
			driver.refresh()

		time.sleep(1)

if len(not_not_downloaded) > 0:
	print "No se han podido descargar las siguientes canciones: "
	for link in not_not_downloaded:
		# Get request to youtube list
		req = requests.get("https://"+link)
		data = req.text
		soup = BeautifulSoup(data, "html.parser")

		print link + ' -- ' + soup.find(id='eow-title').string.strip()

driver.close()
