#!/usr/bin/python

# Other typical inputs
import unittest
import time
import re
import sys
import os

#Always this two imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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
