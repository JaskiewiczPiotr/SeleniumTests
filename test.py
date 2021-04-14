from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


driver = webdriver.Firefox(executable_path="C:\TestFiles\geckodriver.exe")
driver.get('http://eve.ii.pw.edu.pl:9007/#/start_page')
time.sleep(2)
button = driver.find_element_by_id("showHelpWindowButton")
button.click()
time.sleep(2)

string1 = driver.find_element_by_tag_name("h1").text
assert string1 == "DnaAssembler - Help"
string2 = driver.find_element_by_tag_name("h3").text
assert string2 == "Authors"
string3 = driver.find_element_by_id("file_formats_href").text
assert string3 == "Input and output file formats"
string4 = driver.find_element_by_id("algorithms_href").text
assert string4 == "Parameters and algorithms used in application"


string6 = driver.find_element_by_id("client_version_val").text
print(string6)

string7 = driver.find_element_by_id("right_col").text
print(string7)











