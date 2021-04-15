from selenium import webdriver
import time

from datetime import datetime

from test import driver

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
string8 = driver.find_element_by_id("server_time").text
print(string8)
print(current_time)

assert string8 == current_time